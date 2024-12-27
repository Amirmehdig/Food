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
def vCustomers():
    rows = db_handler.get_vCustomers() 
    table = [{"user_id": row.user_id, "username": row.name, "phone_number": row.phone_number, 
              "favorite_food": row.favorite_food, "favorite_restaurant": row.favorite_restaurant, 
              "total_amount": row.total_amount, "total_order": row.total_order} for row in rows]    
    return render_template('view_data.html', data=table, title="vCustomers")

@app.route('/admin/view_users', methods=['GET'])
def vDeliveryPersonSummary():
    rows = db_handler.get_vDeliveryPersonSummary() 
    table = [{"delivery_person_id": row.delivery_person_id, "delivery_person_name": row.name,
              "phone_number": row.phone_number, "most_serviced_restaurant": row.most_serviced_restaurant,
              "total_order_delivered": row.total_order_delivered, "loyalty": row.loyalty} for row in rows]
    return render_template('view_data.html', data=table, title="vDeliveryPersonSummary")
