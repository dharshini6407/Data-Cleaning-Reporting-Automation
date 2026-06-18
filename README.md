# Data Cleaning & Reporting Automation Pipeline

An automated, end-to-end Python data pipeline engineered to ingest raw, messy transaction records, fix structural integrity errors, and auto-generate comprehensive business performance summaries. This project showcases data preprocessing optimization, programmatic anomaly handling, and reporting efficiency.

## 🧹 Automated Data Cleaning Operations

The script intercepts common production-level data corruptions programmatically:

- **Deduplication**: Audits transaction identifiers to drop redundant entries, preserving data normalization.
- **Text Standardization**: Massages inconsistent inputs (e.g., trailing whitespace, structural casing discrepancies) into crisp, uniform categorical flags.
- **Null Imputation**: Replaces categorical blanks with fallback flags and restores numeric gaps using statistical dataset medians.
- **Anomaly Rectification**: Programmatically fixes logical impossibilities (such as negative purchase quantities) using mathematical absolute transformation.

## 📊 Pipeline Performance Metrics (Latest Run)

- **Initial Records Ingested**: 200
- **Duplicate Rows Removed**: 151
- **Missing Sales Values Resolved**: 10
- **Final Clean Records Retained**: 49
- **Total Automated Revenue**: $68,013.21
- **Average Transaction Value**: $1,388.02

## 📁 Programmatic Outputs Generated

1. `clean_sales_data.csv` -> Standardized, error-free dataset optimized for downstream database ingestion or Power BI connections.
2. `sales_summary_dashboard.png` -> Dual-panel visualization dashboard breaking down revenue share across product dimensions and regional territory distributions.
3. `automation_report.md` -> A dynamically compiled markdown business report detailing cleaning auditing statistics and key performance metrics.

## 🛠️ Tech Stack & Dependencies

- **Language**: Python 3
- **Libraries**: `pandas`, `numpy`, `matplotlib`

## 🏃 How to Execute the Pipeline

1. Clone this repository to your machine.
2. Install the necessary calculation and visual engines:
   ```bash
   pip install numpy pandas matplotlib
   ```
3. Run the automation pipeline script:
   ```bash
   python reporting_automation.py
   ```
