import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

random.seed(42)

vendors = [
    "Alpha Industrial Supplies",
    "Global Parts Co",
    "Metro Logistics",
    "Prime Hardware",
    "Summit Packaging",
    "NexGen Maintenance",
    "BlueLine Services",
    "Vertex Components",
    "Rapid Freight",
    "Omega Office Supplies"
]

categories = {
    "Indirect Goods & Services": [
        "Maintenance & Repair",
        "Office Supplies",
        "Sales & Marketing",
        "Professional Services"
    ],
    "Logistics": [
        "Freight",
        "Warehousing",
        "Transportation"
    ],
    "Hardware": [
        "Fasteners",
        "Tools",
        "Machine Parts"
    ],
    "Packaging": [
        "Corrugate",
        "Labels",
        "Plastic Packaging"
    ]
}

countries_cities = [
    ("United States", "Troy", "North America"),
    ("United States", "Detroit", "North America"),
    ("United States", "Atlanta", "North America"),
    ("Mexico", "Mexico City", "North America"),
    ("Canada", "Toronto", "North America")
]

vendor_tiers = ["Tier 1", "Tier 2", "Tier 3"]

# -----------------------------
# Create procurement transactions
# -----------------------------
procurement_rows = []

start_date = datetime(2024, 1, 1)

for i in range(1, 501):
    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])
    country, city, region = random.choice(countries_cities)

    invoice_amount = round(random.uniform(1000, 85000), 2)
    discount_rate = random.uniform(0.01, 0.12)
    discount_amount = round(invoice_amount * discount_rate, 2)

    procurement_rows.append({
        "invoice_id": f"INV-{i:05d}",
        "invoice_date": start_date + timedelta(days=random.randint(0, 364)),
        "vendor_name": random.choice(vendors),
        "category": category,
        "sub_category": sub_category,
        "country": country,
        "city": city,
        "region": region,
        "vendor_tier": random.choice(vendor_tiers),
        "invoice_amount": invoice_amount,
        "discount_amount": discount_amount,
        "item_quantity": random.randint(10, 5000)
    })

procurement_df = pd.DataFrame(procurement_rows)

# -----------------------------
# Create supplier quality data
# -----------------------------
plants = ["Troy Plant", "Detroit Plant", "Atlanta Plant", "Toronto Plant", "Mexico City Plant"]
material_types = ["Raw Materials", "Packaging", "Hardware", "Corrugate", "Machine Parts"]
defect_types = ["Rejected", "Impact", "No Impact", "Rework"]
impact_levels = ["Low", "Medium", "High"]

quality_rows = []

for i in range(1, 301):
    defect_quantity = random.randint(1, 5000)
    downtime_minutes = random.randint(0, 600)

    quality_rows.append({
        "defect_id": f"DEF-{i:05d}",
        "defect_date": start_date + timedelta(days=random.randint(0, 364)),
        "vendor_name": random.choice(vendors),
        "plant": random.choice(plants),
        "material_type": random.choice(material_types),
        "defect_type": random.choice(defect_types),
        "defect_quantity": defect_quantity,
        "downtime_minutes": downtime_minutes,
        "impact_level": random.choice(impact_levels)
    })

quality_df = pd.DataFrame(quality_rows)

# -----------------------------
# Save CSV files
# -----------------------------
procurement_df.to_csv(RAW_DATA_DIR / "procurement_transactions.csv", index=False)
quality_df.to_csv(RAW_DATA_DIR / "supplier_quality.csv", index=False)

print("CSV files created successfully:")
print(RAW_DATA_DIR / "procurement_transactions.csv")
print(RAW_DATA_DIR / "supplier_quality.csv")
print()
print("Procurement rows:", len(procurement_df))
print("Supplier quality rows:", len(quality_df))