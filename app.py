import pyodbc
from flask import Flask, render_template
from db_handler import DBHandler

app = Flask(__name__)

# Replace these placeholders with your actual SQL Server details
server = '127.0.0.1'
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
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
