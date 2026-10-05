# Notes · Opening & Reading Files

`righe` = lines (a **list** of strings, one per line of the file)

## strip() and split(",")
- `strip()` removes spaces and the hidden `\n` at the start/end of a string
- `split(",")` cuts a string at every comma and returns a list
- Together: `"tempo,spazio\n".strip().split(",")` -> `['tempo', 'spazio']`

## Where to use them
They are **string** methods, so they work on **one line**, not on the whole `righe` list:
- `righe[0].strip().split(",")` -> the headers
- `riga.strip().split(",")` -> the values, inside the loop

## Order
1. `print(righe)` first, just to check what was read
2. build the dictionary after that

## Dictionary
```python
dati = {chiave: [] for chiave in intestazioni}
```
- dictionary comprehension = a one-line `for` loop that builds a dict
- at this point it only has **keys**, each with an empty list: `{'tempo': [], 'spazio': []}`
- this is **initialization**: creating an empty container (variable, list, dict) to store something in later
- the real `for` loops come next and `append` the values into the lists
