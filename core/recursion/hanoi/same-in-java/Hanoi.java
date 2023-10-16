
// Recursive solution to the Towers of Hanoi problem.
import java.util.Scanner;

public class Hanoi {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of disks: ");
        int n = sc.nextInt();
        hanoi('f', 's', 't', n);
        sc.close();
    }

    // Parameters:
    // f (str): Starting rod
    // s (str): Spare rod
    // t (str): Ending rod
    // n (int): Number of disks

    // Functionality:
    // Moves n disks from rod f to rod t using rod s.
    // If n <= 0, returns.
    // If n == 1, prints the move from f to t.
    // Otherwise:
    // - Moves n-1 disks from f to s using t.
    // - Prints the move from f to t.
    // - Moves n-1 disks from s to t using f.
    public static void hanoi(char f, char s, char t, int n) {
        // Base case(s)
        if (n <= 0)
            return;
        if (n == 1)
            System.out.println(f + " -> " + t);
        // recursive case:
        else {
            hanoi(f, t, s, n - 1);
            System.out.println(f + " -> " + t);
            hanoi(s, f, t, n - 1);
        }
    }
}