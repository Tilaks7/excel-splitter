# Excel Splitter Automation

Small utility to split Excel workbooks for easier processing:
- Split a workbook into separate files per sheet.
- Split a single sheet into smaller files with a fixed number of rows.

## Features
- Command-line tool with a simple interface.
- Splits by sheet or by fixed-size row chunks.
- Outputs clean Excel (.xlsx) files.
- Cross-platform (Windows / macOS / Linux).

## Requirements
- Python 3.8+
- See `requirements.txt` (pandas, openpyxl)

## Installation
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate.bat  # Windows
pip install -r requirements.txt
