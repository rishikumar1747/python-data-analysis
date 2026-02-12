import pandas as pd

# 2. Load CSV dataset into Pandas DataFrame
# Example dataset: sample sales data
data = {
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Sales": [250, 300, None, 450, 500, 200],
    "Quantity": [5, 7, 6, None, 10, 4]
}

# Save sample dataset to CSV for demonstration
df_sample = pd.DataFrame(data)
df_sample.to_csv("sales_data.csv", index=False)

# Load dataset
df = pd.read_csv("sales_data.csv")

# 3. Explore dataset
print("Head:\n", df.head(), "\n")
print("Info:\n")
print(df.info())
print("\nDescribe:\n", df.describe(), "\n")

# 4. Handle missing values
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Quantity"].fillna(df["Quantity"].median(), inplace=True)

print("After handling missing values:\n", df, "\n")

# 5. Filter and sort data
filtered_df = df[df["Sales"] > 250].sort_values(by="Sales", ascending=False)
print("Filtered & Sorted Data:\n", filtered_df, "\n")

# 6. Group data and calculate aggregates
grouped = df.groupby("Region").agg({"Sales": "mean", "Quantity": "sum"})
print("Grouped Aggregates:\n", grouped, "\n")

# 7. Add new calculated columns
df["Revenue_per_Item"] = df["Sales"] / df["Quantity"]
print("With New Column:\n", df, "\n")

# 8. Export cleaned data to CSV
df.to_csv("cleaned_sales_data.csv", index=False)

# 9. Interpret insights
print("Insights:")
print("- Highest average sales are in the West region.")
print("- North region has the highest total quantity sold.")
print("- Customers with higher sales generally have higher revenue per item.")