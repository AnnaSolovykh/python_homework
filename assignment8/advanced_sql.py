import sqlite3
import pandas as pd
import traceback

# Task 3 
def create_order_for_customer(conn, customer_name, employee_name, quantity=10, product_limit=5):
    """
    Creates a new order for the given customer and employee.
    The order includes 'quantity' of each of the 'product_limit' least expensive products.
    Returns the newly created order_id.
    """
    try:
        cursor = conn.cursor()

        # Get the customer_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?;", (customer_name,))
        customer_id = cursor.fetchone()
        if customer_id is None:
            raise ValueError(f"Customer '{customer_name}' not found.")
        customer_id = customer_id[0]

        # Get the employee_id
        first_name, last_name = employee_name.split()
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?;", (first_name, last_name))
        employee_id = cursor.fetchone()
        if employee_id is None:
            raise ValueError(f"Employee '{employee_name}' not found.")
        employee_id = employee_id[0]

        # Get product_ids of cheapest products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT ?;", (product_limit,))
        product_ids = [row[0] for row in cursor.fetchall()]
        if len(product_ids) < product_limit:
            raise ValueError("Not enough products found.")

        # Insert order
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id;
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        # Insert line items
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?);
            """, (order_id, product_id, quantity))

        return order_id

    except Exception as e:
        raise RuntimeError(f"Failed to create order: {e}")

try:
    with sqlite3.connect('../db/lesson.db') as conn:
        conn.execute("PRAGMA foreign_keys = 1")

        # Task 1
        sql1 = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """
        df1 = pd.read_sql_query(sql1, conn)
        print("Task 1 — Total price of first 5 orders:")
        print(df1)

        # Task 2
        sql2 = """
        SELECT 
            c.customer_name,
            AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT 
                o.customer_id AS customer_id_b,
                SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS sub ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id;
        """
        df2 = pd.read_sql_query(sql2, conn)
        print("\nTask 2 — Average order price per customer:")
        print(df2)

        # Task 3 — insert and display new order
        order_id = create_order_for_customer(
            conn,
            customer_name="Perez and Sons",
            employee_name="Miranda Harris"
        )

        df3 = pd.read_sql_query("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?;
        """, conn, params=(order_id,))
        
        print("\nTask 3 — New order contents:")
        print(df3)

        # Task 4 — employees with more than 5 orders
        sql4 = """
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5;
        """
        df4 = pd.read_sql_query(sql4, conn)
        print("\nTask 4 — Employees with more than 5 orders:")
        print(df4)


except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = [
        f'File: {trace.filename}, Line: {trace.lineno}, Function: {trace.name}, Code: {trace.line}'
        for trace in trace_back
    ]
    print("An exception occurred.")
    print(f"Type: {type(e).__name__}")
    print(f"Message: {str(e)}")
    print("Traceback:")
    for line in stack_trace:
        print("  ", line)
