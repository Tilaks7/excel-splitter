#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
from excel_splitter import split_by_sheet, split_by_rows
def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("--mode", choices=["by-sheet","by-rows"], default="by-sheet")
    p.add_argument("--sheet")
    p.add_argument("--chunk-size", type=int, default=10000)
    p.add_argument("--out-dir", default="output")
    p.add_argument("--prefix")
    p.add_argument("--quiet", action="store_true")
    a = p.parse_args()
    input_path = Path(a.input)
    if not input_path.exists():
        print("Input not found", file=sys.stderr)
        sys.exit(2)
    out_dir = Path(a.out_dir)
    if a.mode == "by-sheet":
        created = split_by_sheet(input_path, out_dir, prefix=a.prefix)
    else:
        created = split_by_rows(input_path, out_dir, sheet=a.sheet, chunk_size=a.chunk_size, prefix=a.prefix)
    if not a.quiet:
        for c in created:
            print("[+] Wrote", c)
if __name__ == "__main__":
    main()
