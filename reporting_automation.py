import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. GENERATE MESSY RAW DATASET (Simulating real-world errors)
# -------------------------------------------------------------
print("Creating messy raw dataset...")
np.random.seed(10)
n_rows = 200

categories = [" Electronics", "electronics", "Furniture ", "FURNITURE", "Office Supplies", "Office supplies"]
regions = ["North", "South", "East", "West", None] # Includes missing regions

raw_data = {
    "Transaction_ID": np.random.randint(1000, 1050, n_rows), # Will create natural duplicates
    "Date": pd.date_range(start="2026-01-01", periods=n_rows, freq="h"),
    "Category": np.random.choice(categories, n_rows),
    "Region": np.random.choice(regions, n_rows),
    "Sales": np.random.uniform(10, 500, n_rows),
    "Quantity": np.random.randint(1, 10, n_rows)
}

df_raw = pd.DataFrame(raw_data)

# Inject intentional missing values and anomalies
df_raw.loc[df_raw.sample(frac=0.05, random_state=42).index, "Sales"] = np.nan
df_raw.loc[df_raw.sample(n=3, random_state=7).index, "Quantity"] = -5 # Negative quantity anomaly

df_raw.to_csv("raw_sales_data.csv", index=False)
print("-> Saved messy data to 'raw_sales_data.csv'")

# -------------------------------------------------------------
# 2. AUTOMATED DATA CLEANING PIPELINE
# -------------------------------------------------------------
print("\nExecuting automated data cleaning...")

# Load the raw data
df = pd.read_csv("raw_sales_data.csv")

# Record baseline stats for reporting
initial_count = len(df)
duplicate_count = df.duplicated(subset=["Transaction_ID"]).sum()
missing_sales = df["Sales"].isna().sum()

# A. Handle Duplicates: Drop duplicate transactions, keep the first occurrence
df = df.drop_duplicates(subset=["Transaction_ID"], keep="first")

# B. Standardize Inconsistent Text: Remove spaces and force Title Case
df["Category"] = df["Category"].str.strip().str.title()

# C. Handle Missing Values
df["Region"] = df["Region"].fillna("Unknown")                     # Categorical imputation
df["Sales"] = df["Sales"].fillna(df["Sales"].median())             # Numeric imputation with median

# D. Fix Inconsistent/Anomalous Data: Force absolute values on negative quantities
df["Quantity"] = df["Quantity"].abs()

# E. Feature Engineering: Calculate Total Revenue
df["Total_Revenue"] = df["Sales"] * df["Quantity"]

# Save clean dataset
df.to_csv("clean_sales_data.csv", index=False)
print("-> Saved perfectly cleaned data to 'clean_sales_data.csv'")

# -------------------------------------------------------------
# 3. AUTOMATED VISUAL SUMMARY GENERATION
# -------------------------------------------------------------
print("\nGenerating automated charts...")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Chart 1: Revenue by Product Category
category_summary = df.groupby("Category")["Total_Revenue"].sum().sort_values(ascending=False)
category_summary.plot(kind="bar", color="#4F46E5", ax=axes[0], edgecolor="black")
axes[0].set_title("Total Revenue by Category", fontsize=14, fontweight="bold")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Revenue ($)")
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis="y", linestyle="--", alpha=0.7)

# Chart 2: Regional Sales Distribution
region_summary = df.groupby("Region")["Quantity"].sum()
axes[1].pie(region_summary, labels=region_summary.index, autopct="%1.1f%%", 
         colors=["#10B981", "#3B82F6", "#F59E0B", "#EF4444", "#6B7280"], startangle=140)
axes[1].set_title("Sales Quantity Share by Region", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("sales_summary_dashboard.png", dpi=300)
plt.close()
print("-> Saved visualization dashboard to 'sales_summary_dashboard.png'")

# -------------------------------------------------------------
# 4. AUTOMATED EXECUTION SUMMARY REPORT (Text/Markdown Output)
# -------------------------------------------------------------
final_count = len(df)
total_company_revenue = df["Total_Revenue"].sum()

report_content = f"""# AUTOMATED DATA CLEANING & PERFORMANCE REPORT
Generated Automatically on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🧹 Data Cleaning Execution Summary
* **Initial Records Ingested**: {initial_count}
* **Duplicate Rows Removed**: {duplicate_count}
* **Missing Sales Values Resolved**: {missing_sales}
* **Structural Anomalies Corrected**: Fixed negative value quantities and standardized text variations in 'Category'.
* **Final Clean Records Retained**: {final_count}

## 📊 Business Performance Metrics
* **Total Automated Revenue**: ${total_company_revenue:,.2f}
* **Top Performing Category**: {category_summary.index[0]} (${category_summary.values[0]:,.2f})
* **Average Transaction Value**: ${df["Total_Revenue"].mean():,.2f}

## 📂 Output Files Generated Successfully
1. `clean_sales_data.csv` -> Standardized, error-free dataset for production or Power BI.
2. `sales_summary_dashboard.png` -> High-resolution performance metrics visualization chart.
"""

with open("automation_report.md", "w", encoding="utf-8") as f:

    f.write(report_content)

print("\n=== SYSTEM EXECUTION COMPLETE ===")
print(report_content)
