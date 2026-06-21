import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

# Top Countries by Sales
country_sales = (
    df.groupby("COUNTRY")["SALES"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
country_sales.plot(kind="bar")
plt.title("Top 10 Countries by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("country_sales.png")
plt.close()

# Sales by Product Line
product_sales = (
    df.groupby("PRODUCTLINE")["SALES"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product Line")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("productline_sales.png")
plt.close()

print("Charts Generated Successfully")