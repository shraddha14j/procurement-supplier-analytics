import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
CLEANED_DATA_DIR = Path("data/cleaned")

CLEANED_DATA_DIR.mkdir(parents=True, exist_ok=True)

procurement_file = RAW_DATA_DIR / "Procurement Analysis Sample-no-PV.xlsx"
supplier_quality_file = RAW_DATA_DIR / "Supplier Quality Analysis Sample-no-PV.xlsx"

procurement_excel = pd.ExcelFile(procurement_file)
supplier_quality_excel = pd.ExcelFile(supplier_quality_file)

print("Procurement sheets:")
print(procurement_excel.sheet_names)

print("\nSupplier quality sheets:")
print(supplier_quality_excel.sheet_names)
