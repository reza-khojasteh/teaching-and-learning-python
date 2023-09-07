# Strings and Slicing in Python

Strings in Python are sequences of characters. We can access substrings within a string using indexing and slicing. 

## Indexing
We can access individual characters in a string using indexing. Indexes start at 0 for the first character.

```python
name = "Python"
first = name[0] # 'P'
second = name[1] # 'y'
```

## Slicing
Slicing allows accessing a substring by specifying a start and end index separated by a colon. The start index is inclusive and the end index is exclusive.

```python
name = "Python"
first_three = name[0:3] # 'Pyt'
last_three = name[3:6] # 'hon'
```
The start index is inclusive and the end index is exclusive. Omitting the end index slices to the end of the string.

```python
name[2:] # 'thon' 
```

Negative indexes slice from the end of the string. So `name[-1]` is the last character.

```python
name[-3:] # 'hon'
```

## Stride
An optional third index specifies the stride (step size) to use when slicing. The default stride is 1.

```python
name[::2] # 'Pto'
```
Slicing is a useful technique for extracting and manipulating substrings in Python. We'll see it being used in many different contexts as we learn more about Python.