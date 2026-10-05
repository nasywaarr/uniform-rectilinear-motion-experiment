# Opening & Reading Files

Data Modeling course · Università degli Studi di Messina

Uniform rectilinear motion (MRU) experiment: read the measurements from a text file, store them in a
dictionary, modify and rewrite the file, then compute the average velocity and its propagated error.

## Files
| File | What it is |
|------|------------|
| `opening_reading_files.py` | the solution |
| `mru.pdf` | task instructions (ENG / ITA) |
| `esperimento_mru_or.txt` | original MRU data, never modified |
| `esperimento_fisica.txt` | extra data from a different experiment (uniformly accelerated motion), not used by the script |

`esperimento_mru.txt` is the working copy the script reads and rewrites. It is **not stored in the repo**:
you create it from the original (see "How to run").

## Data
| Column   | Meaning      | Instrumental error |
|----------|--------------|--------------------|
| `tempo`  | time (s)     | ± 0.1 s            |
| `spazio` | distance (m) | ± 0.2 m            |

## What the script does
1. Opens the file and reads all lines into `righe`
2. Builds a dictionary: headers as keys, data as lists of floats
3. Prints the data
4. Changes the second `spazio` value and rewrites the file
5. Computes the average velocity `v = Δs / Δt`
6. Computes the error on `v` with error propagation for a ratio
7. Prints the result and appends it to the end of the file

## Result
```
Velocità media: v = (2.00 ± 0.10) m/s
```

## How to run
Create (or reset) the working copy, then run the script.

**Windows (PowerShell)**
```powershell
Copy-Item esperimento_mru_or.txt esperimento_mru.txt -Force
python opening_reading_files.py
```

**macOS / Linux**
```bash
cp esperimento_mru_or.txt esperimento_mru.txt
python3 opening_reading_files.py
```
