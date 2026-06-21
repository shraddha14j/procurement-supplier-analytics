
-- Procurement Spend & Supplier Performance Analytics
-- SQL analysis queries for cleaned datasets

-- 1. Total spend by vendor
SELECT
    vendor_name,
    ROUND(SUM(invoice_amount), 2) AS total_spend,
    COUNT(invoice_id) AS invoice_count,
    ROUND(AVG(discount_rate), 4) AS avg_discount_rate
FROM cleaned_procurement_transactions
GROUP BY vendor_name
ORDER BY total_spend DESC;

-- 2. Spend by category and sub-category
SELECT
    category,
    sub_category,
    ROUND(SUM(invoice_amount), 2) AS total_spend,
    COUNT(invoice_id) AS invoice_count
FROM cleaned_procurement_transactions
GROUP BY category, sub_category
ORDER BY total_spend DESC;

-- 3. Indirect goods and services spend
SELECT
    sub_category,
    ROUND(SUM(invoice_amount), 2) AS indirect_spend,
    COUNT(invoice_id) AS invoice_count
FROM cleaned_procurement_transactions
WHERE category = 'Indirect Goods & Services'
GROUP BY sub_category
ORDER BY indirect_spend DESC;

-- 4. Monthly procurement spend trend
SELECT
    year,
    month,
    month_name,
    ROUND(SUM(invoice_amount), 2) AS monthly_spend,
    ROUND(SUM(discount_amount), 2) AS monthly_discount
FROM cleaned_procurement_transactions
GROUP BY year, month, month_name
ORDER BY year, month;

-- 5. Cost optimization opportunities
SELECT
    vendor_name,
    category,
    sub_category,
    ROUND(SUM(invoice_amount), 2) AS total_spend,
    ROUND(AVG(discount_rate), 4) AS avg_discount_rate,
    COUNT(invoice_id) AS invoice_count
FROM cleaned_procurement_transactions
WHERE cost_optimization_opportunity = 'Review Supplier'
GROUP BY vendor_name, category, sub_category
ORDER BY total_spend DESC;

-- 6. Supplier quality performance
SELECT
    vendor_name,
    SUM(defect_quantity) AS total_defects,
    SUM(downtime_minutes) AS total_downtime_minutes,
    COUNT(defect_id) AS defect_event_count
FROM cleaned_supplier_quality
GROUP BY vendor_name
ORDER BY total_downtime_minutes DESC;

-- 7. Supplier scorecard ranking
SELECT
    vendor_name,
    ROUND(total_spend, 2) AS total_spend,
    invoice_count,
    ROUND(avg_discount_rate, 4) AS avg_discount_rate,
    total_defects,
    total_downtime_minutes,
    high_risk_events,
    supplier_risk_score,
    supplier_risk_level
FROM supplier_scorecard
ORDER BY supplier_risk_score DESC;

-- 8. High risk suppliers with high spend
SELECT
    vendor_name,
    ROUND(total_spend, 2) AS total_spend,
    total_defects,
    total_downtime_minutes,
    supplier_risk_score,
    supplier_risk_level
FROM supplier_scorecard
WHERE supplier_risk_level = 'High Risk'
ORDER BY total_spend DESC;
