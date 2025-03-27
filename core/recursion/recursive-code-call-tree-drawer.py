import tkinter as tk
from tkinter import scrolledtext, messagebox, font
import inspect
import re
import ast
import math
import sys
import io # Needed for redirecting stdout if used later
import traceback # For detailed error printing

# Increase recursion depth limit
try:
    sys.setrecursionlimit(2000)
except Exception as e:
    print(f"Warning: Could not set recursion depth limit - {e}")

# --- 1. Call Tree Node ---
class CallTreeNode:
    _id_counter = 0
    def __init__(self, func_name, args, kwargs, parent_id=None, call_id=None): # Added call_id
        self.id = call_id if call_id is not None else CallTreeNode._id_counter
        if call_id is None:
             CallTreeNode._id_counter += 1
        self.func_name = func_name
        self.args = args
        self.kwargs = kwargs
        self.parent_id = parent_id
        self.children = []
        self.return_value = None
        self.display_str = self._create_display_str()
        self.x = 0
        self.y = 0
        self.width = 0
        self.subtree_width = 0

    def _create_display_str(self):
        try:
            arg_strs = [repr(a) for a in self.args]
            kwarg_strs = [f"{k}={repr(v)}" for k, v in self.kwargs.items()]
            all_args = ", ".join(arg_strs + kwarg_strs)
            if len(all_args) > 50:
                all_args = all_args[:47] + "..."
            base_str = f"{self.func_name}({all_args})"
            if self.return_value is not None and not (isinstance(self.return_value, str) and self.return_value.startswith("Error:")):
                 ret_str = repr(self.return_value)
                 if len(ret_str) > 20:
                     ret_str = ret_str[:17] + "..."
                 base_str += f" -> {ret_str}"
            return base_str
        except Exception as e:
             # Handle cases where repr() might fail on complex objects
             print(f"Error creating display string: {e}")
             return f"{self.func_name}(...)"


    def add_child(self, child_node):
        self.children.append(child_node)

    def update_display_str_with_return(self):
        """Updates the display string after return value is known."""
        self.display_str = self._create_display_str()


    def __repr__(self):
        return f"Node({self.id}, {self.display_str}, parent={self.parent_id})"

# --- 2. Recursive Tracer ---
class RecursiveTracer:
    """Manages tracing ALL decorated functions."""
    def __init__(self):
        self.call_tree_root = None
        self.call_stack = [] # Stores node IDs being executed
        self.all_nodes = {} # Map ID to Node object
        self.current_id = 0 # Simple ID counter

    def reset(self):
        """Resets state for a new visualization run."""
        self.call_tree_root = None
        self.call_stack = []
        self.all_nodes = {}
        self.current_id = 0
        CallTreeNode._id_counter = 0 # Reset node ID gen as well


    def trace_calls(self, func):
        """Decorator factory to wrap any function it's applied to."""
        if not callable(func): # Allow decorating methods etc.
            raise TypeError("Decorator can only wrap callables.")

        func_name = func.__name__ # Get name at decoration time

        def wrapper(*args, **kwargs):
            call_id = self.current_id
            self.current_id += 1

            parent_id = self.call_stack[-1] if self.call_stack else None

            # Create the node for this call
            # Use the captured func_name from the outer scope
            node = CallTreeNode(func_name, args, kwargs, parent_id, call_id=call_id)
            self.all_nodes[node.id] = node

            # Link to parent and set root if necessary
            if parent_id is not None:
                parent_node = self.all_nodes.get(parent_id)
                if parent_node:
                    parent_node.add_child(node)
                # else: This case (parent ID on stack but not in all_nodes) shouldn't happen
            elif self.call_tree_root is None:
                # The first decorated function called when stack is empty is the root
                self.call_tree_root = node

            # --- Execute the actual function ---
            self.call_stack.append(node.id)
            result = None
            try:
                result = func(*args, **kwargs)
                node.return_value = result
            except Exception as e:
                print(f"Error during execution of {func_name}: {e}") # Debug print
                traceback.print_exc() # Print full traceback to console
                node.return_value = f"Error: {type(e).__name__}"
                # Decide whether to raise or just record error and return
                raise # Re-raise the exception by default to stop potentially broken execution
            finally:
                # Ensure stack is popped correctly even if errors occurred
                # We pop the *last* element, assuming it's the current call finishing
                if self.call_stack:
                    finished_id = self.call_stack.pop()
                    if finished_id != node.id:
                        # This indicates a potential issue in stack management, maybe due to exceptions?
                        print(f"Warning: Call stack mismatch! Expected {node.id}, popped {finished_id}")
                        # Attempt recovery if possible, or just log
                        # We might need to search and remove node.id if it's still there? Risky.
            # ------------------------------------

            # Update display string *after* return value is set
            node.update_display_str_with_return()

            return result # Return the original result

        # Try to preserve original signature details if possible
        try:
             wrapper.__signature__ = inspect.signature(func)
        except ValueError: pass # Ignore if signature cannot be created
        wrapper.__name__ = func.__name__ # Keep original name if possible
        wrapper.__doc__ = func.__doc__
        return wrapper

    def get_tree(self):
        return self.call_tree_root

# --- 3. Tree Drawing Logic ---
# (layout_tree, position_nodes, draw_tree, constants remain the same as the previous version with CANVAS_TOP_PADDING)
NODE_V_SPACE = 60
NODE_H_SPACE = 20
NODE_PADDING_X = 8
NODE_PADDING_Y = 4
NODE_BORDER_WIDTH = 1
NODE_FONT = ("Courier", 10)
CANVAS_TOP_PADDING = 30 # Space from the top edge

def get_text_width(canvas, text, font_obj):
    return font_obj.measure(text)

def layout_tree(node, current_depth, node_font):
    if not node: return 0
    # Update width based on potentially changed display string (with return value)
    node.width = get_text_width(None, node.display_str, node_font) + 2 * NODE_PADDING_X
    node.y = current_depth * NODE_V_SPACE + CANVAS_TOP_PADDING
    if not node.children:
        node.subtree_width = node.width
        return node.subtree_width
    children_subtree_widths = [layout_tree(child, current_depth + 1, node_font) for child in node.children]
    total_children_width = sum(children_subtree_widths) + max(0, len(node.children) - 1) * NODE_H_SPACE
    node.subtree_width = max(node.width, total_children_width)
    return node.subtree_width

def position_nodes(node, current_x, node_font):
    if not node: return
    node.x = current_x + (node.subtree_width / 2)
    if node.children:
        children_total_width = sum(child.subtree_width for child in node.children) + max(0, len(node.children) - 1) * NODE_H_SPACE
        start_x = node.x - (children_total_width / 2)
        current_child_x = start_x
        for child in node.children:
            position_nodes(child, current_child_x, node_font)
            current_child_x += child.subtree_width + NODE_H_SPACE

def draw_tree(canvas, node, node_font):
    if not node: return
    text_height = node_font.metrics("linespace")
    half_node_h = text_height / 2 + NODE_PADDING_Y
    half_node_w = node.width / 2
    x0, y0 = node.x - half_node_w, node.y - half_node_h
    x1, y1 = node.x + half_node_w, node.y + half_node_h
    canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black", width=NODE_BORDER_WIDTH)
    canvas.create_text(node.x, node.y, text=node.display_str, font=node_font, anchor=tk.CENTER)
    for child in node.children:
        if child:
             child_text_height = node_font.metrics("linespace")
             child_half_h = child_text_height / 2 + NODE_PADDING_Y
             child_y0 = child.y - child_half_h
             canvas.create_line(node.x, y1, child.x, child_y0, fill="black", width=1)
             draw_tree(canvas, child, node_font)


# --- Helper Function to Add Decorator ---
def add_decorator_to_defs(code_string, decorator_name):
    """
    Parses python code string and adds a decorator before each function definition.
    Handles basic indentation.
    """
    lines = code_string.splitlines()
    modified_lines = []
    func_def_pattern = re.compile(r"^(\s*)def\s+\w+\s*\(") # Matches start of func def

    for line in lines:
        match = func_def_pattern.match(line)
        if match:
            indentation = match.group(1) # Capture existing indentation
            modified_lines.append(f"{indentation}@{decorator_name}")
        modified_lines.append(line)

    return "\n".join(modified_lines)


# --- 4. GUI Application ---
class CallTreeVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recursive Call Tree Visualizer")
        self.geometry("900x700")
        # Tracer instance belongs to the App
        self.tracer = RecursiveTracer()

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1) # Code editor row
        self.grid_rowconfigure(3, weight=3) # Canvas row
        self.grid_columnconfigure(0, weight=1)

        # --- Code Input Area ---
        tk.Label(self, text="Enter Python Code (including recursive functions):").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.code_text = scrolledtext.ScrolledText(self, height=10, width=80, wrap=tk.WORD, font=("Consolas", 10))
        self.code_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        # Default text updated
        self.code_text.insert(tk.END, """# Example: Palindrome Check (with nested function)
def is_palindrome(word):
    # Nested recursive helper function
    def check_two_sides(left, right):
        # Base case: Indices meet or cross
        if left >= right:
            return True
        # Recursive step: Check characters and move inwards
        elif word[left] == word[right]:
            # Make the recursive call
            return check_two_sides(left + 1, right - 1)
        # Base case: Mismatch found
        else:
            return False

    # Initial call to the helper
    if not word: # Handle empty string case
        return True
    return check_two_sides(0, len(word) - 1)

# You can add other functions here too
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

""")

        # --- Initial Call Input ---
        control_frame = tk.Frame(self)
        control_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        tk.Label(control_frame, text="Initial Call (e.g., is_palindrome('racecar')):" ).pack(side=tk.LEFT, padx=5)
        self.call_entry = tk.Entry(control_frame, width=40, font=("Consolas", 10)) # Wider entry
        self.call_entry.pack(side=tk.LEFT, padx=5)
        self.call_entry.insert(tk.END, "is_palindrome('level')")

        # --- Run Button ---
        self.run_button = tk.Button(control_frame, text="Visualize Call Tree", command=self.run_visualization)
        self.run_button.pack(side=tk.LEFT, padx=10)

        # --- Clear Button ---
        self.clear_button = tk.Button(control_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)


        # --- Canvas for Drawing ---
        canvas_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        canvas_frame.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.canvas = tk.Canvas(canvas_frame, bg="white")
        self.v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.node_font = font.Font(family=NODE_FONT[0], size=NODE_FONT[1])

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas.configure(scrollregion=(0, 0, 100, 100))
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def run_visualization(self):
        self.clear_canvas()
        self.tracer.reset() # Reset tracer state for this run

        user_code = self.code_text.get("1.0", tk.END)
        initial_call = self.call_entry.get().strip()

        if not user_code or not initial_call:
            messagebox.showerror("Error", "Please provide both Python code and an initial call.")
            return

        # Define the name under which the decorator will be available in exec
        decorator_internal_name = "__recursive_tracer_decorator"

        # Prepare the execution namespace, injecting the decorator method
        exec_namespace = {
            decorator_internal_name: self.tracer.trace_calls
        }

        try:
            # --- Modify the user code to add the decorator ---
            print("--- Original Code ---")
            print(user_code)
            modified_code = add_decorator_to_defs(user_code, decorator_internal_name)
            print("\n--- Modified Code (with decorators) ---")
            print(modified_code)
            print("-" * 20)

            # --- Execute the modified code (defines decorated functions) ---
            # Compile first to potentially catch syntax errors earlier
            compiled_code = compile(modified_code, '<string>', 'exec')
            exec(compiled_code, exec_namespace)

            # --- Execute the initial call (triggers the decorated functions) ---
            print(f"--- Executing Initial Call: {initial_call} ---")
            # We execute the initial call in the *same namespace*
            # so it finds the decorated versions of the functions.
            exec(initial_call, exec_namespace)
            print("--- Execution Finished ---")


        except SyntaxError as e:
            messagebox.showerror("Syntax Error", f"Error parsing code (potentially after adding decorators):\n{e}")
            print(f"Syntax Error: {e}")
            traceback.print_exc()
            return
        except Exception as e:
            messagebox.showerror("Runtime Error", f"Error during execution:\n{type(e).__name__}: {e}")
            print(f"Runtime Error: {e}")
            traceback.print_exc()
            # Continue to attempt drawing partial tree below

        # --- Get the call tree ---
        call_tree_root = self.tracer.get_tree()

        if not call_tree_root:
             # Check if any nodes were created at all, even without a root link
             if not self.tracer.all_nodes:
                 messagebox.showinfo("Info", "No decorated function calls were traced. Was the initial call correct?")
             else:
                 # This might happen if exec(initial_call) raised an error *before* any decorated func was entered
                 messagebox.showwarning("Warning", "Execution finished, but no call tree root was established. Drawing may be empty or incomplete.")
             return


        # --- Layout and Draw the Tree ---
        try:
            # 1. Calculate layout (this now updates node widths too)
            layout_tree(call_tree_root, 0, self.node_font)

            # 2. Position nodes (X coordinates)
            canvas_width_offset = 20 # Start drawing 20px from the left edge
            position_nodes(call_tree_root, canvas_width_offset, self.node_font) # Pass offset only once

            # 3. Find overall bounds *after* positioning
            min_x, max_x = float('inf'), float('-inf')
            min_y, max_y = float('inf'), float('-inf')
            if not self.tracer.all_nodes: # Handle case where root exists but no nodes (shouldn't happen?)
                messagebox.showerror("Error","No nodes found for drawing despite having a root.")
                return

            for node_id, node in self.tracer.all_nodes.items():
                 # Check if node has valid position (might not if disconnected and not reached by position_nodes)
                 if node.x == 0 and node.y == 0 and node is not call_tree_root:
                     # This node might be orphaned, skip for bounds calculation? Or log warning.
                     # print(f"Warning: Node {node.id} ({node.display_str}) has default position, may be disconnected.")
                     continue # Skip disconnected nodes for bounds calculation

                 text_height = self.node_font.metrics("linespace")
                 half_node_h = text_height / 2 + NODE_PADDING_Y
                 half_node_w = node.width / 2 # Use the possibly updated width
                 x0 = node.x - half_node_w
                 y0 = node.y - half_node_h
                 x1 = node.x + half_node_w
                 y1 = node.y + half_node_h
                 min_x = min(min_x, x0)
                 max_x = max(max_x, x1)
                 min_y = min(min_y, y0)
                 max_y = max(max_y, y1)

            # Handle case where only root exists or bounds are weird
            if min_x == float('inf'): min_x=0
            if max_x == float('-inf'): max_x=200
            if min_y == float('inf'): min_y=0
            if max_y == float('-inf'): max_y=100

            # 4. Configure scroll region
            padding = 30
            scroll_x0 = max(0, min_x - padding)
            scroll_y0 = max(0, min_y - padding)
            scroll_x1 = max_x + padding
            scroll_y1 = max_y + padding

            self.canvas.configure(scrollregion=(scroll_x0, scroll_y0, scroll_x1, scroll_y1))

            # 5. Draw the tree
            draw_tree(self.canvas, call_tree_root, self.node_font)

        except Exception as e:
            messagebox.showerror("Drawing Error", f"Error laying out or drawing the tree:\n{type(e).__name__}: {e}")
            print(f"Drawing Error: {e}")
            traceback.print_exc()


# --- Main Execution ---
if __name__ == "__main__":
    app = CallTreeVisualizer()
    app.mainloop()