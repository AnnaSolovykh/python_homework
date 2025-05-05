import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")

# --- TASK 4 ---
query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)

print("Initial joined data:")
print(df.head())

df['total'] = df['quantity'] * df['price']
print("\nAfter adding 'total' column:")
print(df.head())

summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

summary_df.rename(columns={
    'line_item_id': 'order_count',
    'total': 'total_revenue'
}, inplace=True)

summary_df = summary_df.sort_values(by='product_name')

print("\nGrouped summary:")
print(summary_df.head())

summary_df.to_csv("order_summary.csv", index=False)
print("\nSaved summary to order_summary.csv")
