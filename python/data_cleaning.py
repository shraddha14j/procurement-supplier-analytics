import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
CLEANED_DATA_DIR = Path("data/cleaned")
CLEANED_DATA_DIR.mkdir(parents=True, exist_ok=True)

procurement_file = RAW_DATA_DIR / "procurement_transactions.csv"
supplier_quality_file = RAW_DATA_DIR / "supplier_quality.csv"

procurement_df = pd.read_csv(procurement_file)
quality_df = pd.read_csv(supplier_quality_file)

# -----------------------------
# Clean procurement data
# -----------------------------
procurement_df.columns = procurement_df.columns.str.strip().str.lower()

procurement_df["invoice_date"] = pd.to_datetime(procurement_df["invoice_date"])

procurement_df["invoice_amount"] = pd.to_numeric(
    procurement_df["invoice_amount"], errors="coerce"
)

procurement_df["discount_amount"] = pd.to_numeric(
    procurement_df["discount_amount"], errors="coerce"
)

procurement_df["item_quantity"] = pd.to_numeric(
    procurement_df["item_quantity"], errors="coerce"
)

procurement_df["discount_rate"] = (
    procurement_df["discount_amount"] / procurement_df["invoice_amount"]
).round(4)

procurement_df["year"] = procurement_df["invoice_date"].dt.year
procurement_df["month"] = procurement_df["invoice_date"].dt.month
procurement_df["month_name"] = procurement_df["invoice_date"].dt.month_name()
procurement_df["quarter"] = "Q" + procurement_df["invoice_date"].dt.quarter.astype(str)

procurement_df["high_spend_flag"] = procurement_df["invoice_amount"].apply(
    lambda amount: "High Spend" if amount >= 50000 else "Normal Spend"
)

procurement_df["low_discount_flag"] = procurement_df["discount_rate"].apply(
    lambda rate: "Low Discount" if rate < 0.03 else "Normal Discount"
)

procurement_df["cost_optimization_opportunity"] = procurement_df.apply(
    lambda row: "Review Supplier"
    if row["invoice_amount"] >= 50000 and row["discount_rate"] < 0.03
    else "No Immediate Action",
    axis=1
)

procurement_df = procurement_df.drop_duplicates()
procurement_df = procurement_df.dropna(
    subset=["invoice_id", "invoice_date", "vendor_name"]
)

# -----------------------------
# Clean supplier quality data
# -----------------------------
quality_df.columns = quality_df.columns.str.strip().str.lower()

quality_df["defect_date"] = pd.to_datetime(quality_df["defect_date"])

quality_df["defect_quantity"] = pd.to_numeric(
    quality_df["defect_quantity"], errors="coerce"
)

quality_df["downtime_minutes"] = pd.to_numeric(
    quality_df["downtime_minutes"], errors="coerce"
)

quality_df["year"] = quality_df["defect_date"].dt.year
quality_df["month"] = quality_df["defect_date"].dt.month
quality_df["month_name"] = quality_df["defect_date"].dt.month_name()
quality_df["quarter"] = "Q" + quality_df["defect_date"].dt.quarter.astype(str)

quality_df["supplier_quality_risk"] = quality_df.apply(
    lambda row: "High Risk"
    if row["downtime_minutes"] >= 300 or row["defect_quantity"] >= 3000
    else "Normal Risk",
    axis=1
)

quality_df = quality_df.drop_duplicates()
quality_df = quality_df.dropna(
    subset=["defect_id", "defect_date", "vendor_name"]
)

# -----------------------------
# Create supplier scorecard
# -----------------------------
supplier_spend = procurement_df.groupby("vendor_name", as_index=False).agg(
    total_spend=("invoice_amount", "sum"),
    total_discount=("discount_amount", "sum"),
    invoice_count=("invoice_id", "count"),
    avg_discount_rate=("discount_rate", "mean")
)

supplier_quality = quality_df.groupby("vendor_name", as_index=False).agg(
    total_defects=("defect_quantity", "sum"),
    total_downtime_minutes=("downtime_minutes", "sum"),
    high_risk_events=(
        "supplier_quality_risk",
        lambda values: (values == "High Risk").sum()
    )
)

supplier_scorecard = supplier_spend.merge(
    supplier_quality,
    on="vendor_name",
    how="left"
)

supplier_scorecard["total_defects"] = supplier_scorecard["total_defects"].fillna(0)
supplier_scorecard["total_downtime_minutes"] = supplier_scorecard[
    "total_downtime_minutes"
].fillna(0)
supplier_scorecard["high_risk_events"] = supplier_scorecard[
    "high_risk_events"
].fillna(0)

supplier_scorecard["supplier_risk_score"] = (
    supplier_scorecard["total_downtime_minutes"] * 0.5
    + supplier_scorecard["total_defects"] * 0.3
    + supplier_scorecard["high_risk_events"] * 100
).round(2)

supplier_scorecard["supplier_risk_level"] = supplier_scorecard[
    "supplier_risk_score"
].apply(
    lambda score: "High Risk" if score >= 50000 else "Normal Risk"
)

# -----------------------------
# Save cleaned files
# -----------------------------
procurement_df.to_csv(
    CLEANED_DATA_DIR / "cleaned_procurement_transactions.csv",
    index=False
)

quality_df.to_csv(
    CLEANED_DATA_DIR / "cleaned_supplier_quality.csv",
    index=False
)

supplier_scorecard.to_csv(
    CLEANED_DATA_DIR / "supplier_scorecard.csv",
    index=False
)

print("Cleaned files created successfully:")
print(CLEANED_DATA_DIR / "cleaned_procurement_transactions.csv")
print(CLEANED_DATA_DIR / "cleaned_supplier_quality.csv")
print(CLEANED_DATA_DIR / "supplier_scorecard.csv")
print()
print("Procurement rows:", len(procurement_df))
print("Supplier quality rows:", len(quality_df))
print("Supplier scorecard rows:", len(supplier_scorecard))
