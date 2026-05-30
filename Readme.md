<div align="center">

# Diacritics Remover

### Normalize and clean Excel worker data for payment processing

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-1D6F42?style=for-the-badge&logoColor=white)
![Unidecode](https://img.shields.io/badge/Unidecode-4B8BBE?style=for-the-badge&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-2C2255?style=for-the-badge&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
[![Repo](https://img.shields.io/badge/GitHub-jackinf%2Fdiacritics__remover-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jackinf/diacritics_remover)

</div>

## Overview

Diacritics Remover is a small Python utility that reads an Excel spreadsheet of worker
and payment records and normalizes selected columns into plain ASCII. It transliterates
diacritics (via Unidecode), strips brackets and punctuation, and removes spaces from
banking fields such as IBAN and account numbers, then writes the cleaned result to a new
`*_processed.xlsx` file. It is available both as a command-line tool and as a simple
Tkinter desktop GUI.

## Features

- Transliterates accented characters to ASCII using `unidecode`.
- Per-column transformation rules: removes parenthesised content, dots/dashes, commas,
  apostrophes, slashes, and `#` from name and address fields.
- Strips spaces from `IBAN`, `Account Number`, and `Bank ID` so banking identifiers are
  contiguous.
- Safely handles empty/`NaN` cells by coercing them to empty strings.
- CLI mode (`main.py`) with optional custom output path, defaulting to `<input>_processed.xlsx`.
- GUI mode (`gui.py`) with a file picker for non-technical users.
- `generate_sample.py` to produce a sample input workbook for testing.
- Dockerfile to build a standalone Windows `.exe` via PyInstaller.

## Tech Stack

| Area        | Technology                          |
| ----------- | ----------------------------------- |
| Language    | Python                              |
| Data        | pandas, openpyxl                    |
| Text        | Unidecode                           |
| GUI         | Tkinter (standard library)          |
| Packaging   | PyInstaller, Docker (Windows image) |

## Getting Started

### Prerequisites

- Python 3.12+
- `pip` and the ability to create a virtual environment

### Installation

```bash
python -m venv .venv
source ./.venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate.bat        # Windows

pip install -r requirements.txt
```

### Running

Command-line mode (writes `your_file_processed.xlsx` next to the input):

```bash
python main.py your_file.xlsx
```

Optionally pass an explicit output path:

```bash
python main.py your_file.xlsx cleaned.xlsx
```

GUI mode (file picker dialog):

```bash
python gui.py
```

Generate a sample workbook for testing:

```bash
python generate_sample.py
```

## Project Structure

```
diacritics_remover/
├── main.py              # CLI entry point (argparse)
├── gui.py               # Tkinter GUI entry point
├── generate_sample.py   # Creates a sample input spreadsheet
├── requirements.txt     # Python dependencies
├── Dockerfile           # Windows image to build a PyInstaller .exe
└── run.sh / run.bat     # Convenience launchers for the GUI
```
