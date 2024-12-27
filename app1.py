from flask import Flask, render_template, request, session, redirect, url_for
from db_handler import DBHandler
from datetime import datetime
from cart import Cart

app = Flask(__name__)
app.secret_key = '1234'  # Required for session-based features like flash

# Replace these placeholders with your actual SQL Server details
server = '.\SQLDEVELOPER'
database = 'FoodsDB'
username = 'foodapp'
password = 'ghaza'

# Create the connection string
connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};"
    f"UID={username};PWD={password}"
)
# Attention!!!!!!!!!
# Use the class like below to handle detabase requests
db_handler = DBHandler(connection_string)


@app.route('/admin')
def admin_dashboard():
    return render_template('admin.html')

@app.route('/admin/view_restaurants', methods=['GET'])
def vRestaurantCustomers():
    rows = db_handler.get_vRestaurantCustomers()
    table = [{"restaurant_id": row.restaurant_id, "restaurant_name": row.name,
              "user_id": row.user_id, "phone_number": row.phone_number, "total": row.total
              "total_order": row.total_order, "loyalty": row.loyalty, "favorite_food": row.favorite_food} for row in rows]
    return render_template('view_data.html', data=table, title="vRestaurantCustomers")

@app.route('/admin/view_orders', methods=['GET'])
def view_orders():
    rows = db_handler.get_all_orders()  # Replace with actual method to fetch orders
    orders = [{"id": row.order_id, "customer": row.customer_name, "date": row.date} for row in rows]
    return render_template('view_data.html', data=orders, title="Orders")

@app.route('/admin/view_users', methods=['GET'])
def view_users():
    rows = db_handler.get_all_users()  # Replace with actual method to fetch users
    users = [{"id": row.user_id, "name": row.name, "email": row.email} for row in rows]
    return render_template('view_data.html', data=users, title="Users")
