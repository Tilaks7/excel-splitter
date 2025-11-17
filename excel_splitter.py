#!/usr/bin/env python3
from pathlib import Path
import math
import pandas as pd
def sanitize(name: str) -> str:
    return "".join(c if c.isalnum() or c in "._- " else "_" for c in name).strip().replace(" ", "_")
def split_by_sheet(input_path: Path, out_dir: Path, prefix: str = None):
    xls = pd.ExcelFile(input_path, engine="openpyxl")
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = prefix or input_path.stem
    created = []
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet, engine="openpyxl")
        out_file = out_dir / f"{prefix}__{sanitize(sheet)}.xlsx"
        df.to_excel(out_file, index=False, engine="openpyxl")
        created.append(out_file)
    return created
def split_by_rows(input_path: Path, out_dir: Path, sheet: str = None, chunk_size: int = 10000, prefix: str = None):
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = prefix or input_path.stem
    xls = pd.ExcelFile(input_path, engine="openpyxl")
    if sheet is None:
        sheet = xls.sheet_names[0]
    df = pd.read_excel(xls, sheet_name=sheet, engine="openpyxl")
    total = len(df)
    if total == 0:
        return []
    import math
    parts = math.ceil(total / chunk_size)
    created = []
    for i in range(parts):
        start = i * chunk_size
        end = min(start + chunk_size, total)
        sub = df.iloc[start:end]
        out_file = out_dir / f"{prefix}__{sanitize(sheet)}__part{i+1:03d}.xlsx"
        sub.to_excel(out_file, index=False, engine="openpyxl")
        created.append(out_file)
    return created
