from flask import Flask, render_template, request, session, redirect, url_for
from db_handler import DBHandler
from datetime import datetime


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
        session['user_id'] = db_handler.get_user_id(name)[0]
        session['role'] = 'Customer'
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('register_form.html')


@app.route('/restaurant/<restaurant_id>/')
def restaurant(restaurant_id):
    rows = db_handler.get_foods(int(restaurant_id))
    foods = [{"name": row.name, "price": row.price, "rating":row.rating, "id":row.food_id} for row in rows]
    restaurant = {"name": db_handler.get_restaurant_data(rows[0].restaurant_id)[0].name, "id": rows[0].restaurant_id}
    return render_template('restaurant.html', foods=foods)


if __name__ == '__main__':
    app.run(debug=True)
