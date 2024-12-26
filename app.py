from flask import Flask, render_template, request, session, redirect, url_for
from db_handler import DBHandler
from datetime import datetime
from cart import Cart
import random

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

@app.route('/')
def home():
    rows = db_handler.get_all_restaurants()
    restaurants = [{"name": row.name, "id": row.restaurant_id} for row in rows]
    #print(session)
    return render_template('home.html', restaurants=restaurants)

@app.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register/customer', methods=['POST', 'GET'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
        print(type(name))
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return render_template('register_form.html')
        phone = request.form['phone']
        address = request.form['address']
        db_handler.insert_user(name, email, password, phone, address, str(datetime.date(datetime.now())), 1, 'Customer')
        session['user_id'] = int(db_handler.get_user_id(name)[0].user_id)
        session['role'] = 'Customer'
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('register_form.html')


@app.route('/restaurant/<restaurant_id>/')
def restaurant(restaurant_id):
    if request.method == 'GET':
        rows = db_handler.get_food_by_restaurant_id(int(restaurant_id))
        foods = [{"name": row.name, "price": row.price, "rating":int(row.rating), "id":row.food_id, 'restaurant_id':row.restaurant_id, 'available_count':row.available_count} for row in rows]
        restaurant = db_handler.get_restaurant_data(int(foods[0]['restaurant_id']))
        restaurant = {"name": restaurant[0].name, "restaurant_id": restaurant[0].restaurant_id}
        return render_template('restaurant.html', foods=foods, restaurant=restaurant)

@app.route('/place_order', methods=['POST'])
def place_order():
    cart = Cart()
    foods = db_handler.get_all_foods()
    quantities = request.form
    restaurant_id = 0
    delivery_person_id = random.randint(1, 10)
    for food_id, quantity in quantities.items():
        restaurant_id = int(db_handler.get_food_by_food_id(int(food_id))[0].restaurant_id)
        if int(quantity) > 0:
            item = {"food_id": int(food_id), "quantity": int(quantity),
                     "price": next(int(quantity) * float(x.price) for x in foods if x.food_id == int(food_id)),
                     "restaurant_id": restaurant_id}
            cart.add(item)
    order_id = db_handler.insert_full_order(cart.total(), 'New', int(session['user_id']), restaurant_id, delivery_person_id)
    for item in cart.items:
        db_handler.insert_order_detail(order_id, item['food_id'], item['quantity'], item['price'])
    

    # Parse quantities from form data
    # for food_id, quantity in quantities.items():
    #     if int(quantity) > 0:  # Only include items with quantity > 0
    #         order_details[int(food_id)] = int(quantity)
    # print(order_details)
    return redirect(url_for('home'))
    # Process the order (e.g., save to database)
    # Example: {'1': 2, '3': 1} (Food ID 1 with 2 qty, Food ID 3 with 1 qty)
    # Save logic here...        



if __name__ == '__main__':
    app.run(debug=True)
