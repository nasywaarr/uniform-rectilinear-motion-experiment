# Uniform Rectilinear Motion Experiment

Experiment for the Data Modeling course (Università degli Studi di Messina): reading and writing
experiment data with Python, then computing the average velocity and its propagated error.

## Structure
```
.
├── tasks/
│   └── opening-reading-files/   solution, data and task instructions
└── notes/
    └── opening-reading-files.md notes on strip(), split() and dictionaries
```

- [`tasks/opening-reading-files`](tasks/opening-reading-files) – read a file, build a dictionary, compute v ± error
- [`notes/opening-reading-files.md`](notes/opening-reading-files.md) – my notes for this exercise

## Result
```
Velocità media: v = (2.00 ± 0.10) m/s
```

## Quick start
```powershell
cd tasks/opening-reading-files
Copy-Item esperimento_mru_or.txt -Force
python opening_reading_files.py
```
See the [task README](tasks/opening-reading-files/README.md) for details.
