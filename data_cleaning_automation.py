import pandas as pd

# Load Dataset
df = pd.read_csv("data.csv", encoding="latin1")

print("Dataset Loaded Successfully")
print("Original Shape:", df.shape)

# ---------------------------
# Missing Values Before Cleaning
# ---------------------------
missing_before = df.isnull().sum().sum()

# ---------------------------
# Remove Duplicates
# ---------------------------
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# ---------------------------
# Fill Missing Values
# ---------------------------

# Numeric Columns
numeric_cols = df.select_dtypes(include=["number"]).columns

for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mean())

# Non-Numeric Columns
text_cols = df.select_dtypes(exclude=["number"]).columns

for col in text_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna("Unknown")

missing_after = df.isnull().sum().sum()

# ---------------------------
# Save Cleaned Dataset
# ---------------------------
df.to_csv("cleaned_data.csv", index=False)

# ---------------------------
# Generate Business Insights
# ---------------------------

total_sales = df["SALES"].sum()
average_sales = df["SALES"].mean()
highest_sale = df["SALES"].max()

top_country = (
    df.groupby("COUNTRY")["SALES"]
    .sum()
    .idxmax()
)

top_product = (
    df.groupby("PRODUCTLINE")["SALES"]
    .sum()
    .idxmax()
)

# ---------------------------
# Create Report
# ---------------------------

report = f"""
========================================
DATA CLEANING & REPORTING AUTOMATION
========================================

Original Rows: {2823}
Rows After Cleaning: {len(df)}

Duplicates Removed: {duplicates_removed}

Missing Values Before Cleaning: {missing_before}
Missing Values After Cleaning: {missing_after}

------------- SALES INSIGHTS -------------

Total Sales: {total_sales:.2f}

Average Sales: {average_sales:.2f}

Highest Sale: {highest_sale:.2f}

Top Performing Country: {top_country}

Best Selling Product Line: {top_product}

-------------------------------------------

Report Generated Successfully
"""

print(report)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Cleaned Dataset Saved")
print("Report Saved as report.txt")