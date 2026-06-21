# Procurement Spend & Supplier Performance Analytics

## Project Overview
This project analyzes procurement spend, supplier performance, supplier quality, category-level purchasing trends, discounts, and cost optimization opportunities using Python, SQL, Excel/CSV, and Power BI.

## Business Objective
The goal is to support procurement and sourcing teams with data-driven insights for supplier performance tracking, category management, sourcing strategy, and cost optimization.

## Tools Used
- Python
- SQL
- Power BI
- Excel/CSV
- GitHub

## Dataset
Synthetic procurement and supplier quality datasets were created for this project, inspired by Microsoft Power BI procurement and supplier quality sample business scenarios.

## Key Features
- Procurement spend analysis
- Supplier scorecards
- Indirect goods and services analysis
- Category and sub-category spend tracking
- Supplier quality and downtime analysis
- Cost optimization opportunity identification
- Potential savings calculation

## Dashboard Pages
1. Executive Overview
2. Category Management
3. Supplier Performance
4. Cost Optimization

## Key Insights
- Hardware had the highest total spend across procurement categories.
- Rapid Freight was one of the highest-spend suppliers.
- Machine Parts and Tools were major cost-driving sub-categories.
- Supplier quality metrics identified vendors with higher downtime and defect quantities.
- Review Supplier opportunities highlighted high-spend and low-discount transactions.

## Business Recommendations
- Review high-spend vendors with low discount rates for renegotiation.
- Monitor supplier downtime and defect trends through quarterly scorecards.
- Prioritize indirect goods and services spend for category-level cost control.
- Use supplier risk levels to support sourcing and supplier management decisions.
- Track potential savings from improved discount negotiations.

## Project Files
- `python/create_raw_datasets.py` - creates synthetic raw procurement and supplier quality data
- `python/data_cleaning.py` - cleans data and creates supplier scorecard
- `sql/procurement_analysis_queries.sql` - SQL queries for spend and supplier analysis
- `powerbi/procurement_supplier_analytics_dashboard.pbix` - Power BI dashboard
- `screenshots/` - dashboard page screenshots

## Dashboard Screenshots

### Executive Overview
![Executive Overview](screenshots/Executive%20Overview.png)

### Category Management
![Category Management](screenshots/Category%20Management.png)

### Supplier Performance
![Supplier Performance](screenshots/Supplier%20Performance.png)

### Cost Optimization
![Cost Optimization](screenshots/Cost%20Optimization.png)
