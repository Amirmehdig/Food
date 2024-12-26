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


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        entered_pass = request.form['password']
        real_pass = db_handler.get_password(name)
        if real_pass:
            if real_pass[0].password == entered_pass:
                id = int(db_handler.get_user_id(name)[0].user_id)
                session['user_id'] = id
                session['role'] = db_handler.get_profile_data(id)[0].role
                return redirect(url_for('home'))
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')


@app.route('/logout/', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/register/customer', methods=['POST', 'GET'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
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
    order = {"id": order_id}
    delivery = db_handler.get_delivery_person_by_id(delivery_person_id)[0]
    delivery = {'name':delivery.name, 'phone_number':delivery.phone_number, 'vehicle_type':delivery.vehicle_type}
    return render_template('order.html', order=order, delivery=delivery)       


@app.route('/delivered/<order_id>/')
def delivered(order_id):
    db_handler.complete_order(int(order_id))
    return redirect(url_for('home'))


@app.route('/canceled/<order_id>/')
def canceled(order_id):
    db_handler.cancel_order(int(order_id))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
