import pyodbc

class DBHandler:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_connection(self):
        try:
            conn = pyodbc.connect(self.connection_string)
            print("Database connection successful!")
            return conn
        except Exception as e:
            print("Connection failed:", e)
            return None

    # Login:
    def insert_user(self, name, email, password, phone_number, address, registration_date, is_active, role):
        """Inserts a user into the Users table."""
        query = ("INSERT INTO Users (name, email, password, phone_number,"
                 "address, registration_date, is_active, role) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        params = (name, email, password, phone_number, address, registration_date, is_active, role)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("User inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def insert_restaurant(self, name, address, phone_number, opening_hours, rating, is_open, owner_id):
        """Inserts a restaurant into the Restaurants table."""
        query = ("INSERT INTO Restaurants (name, address, phone_number,"
                 "opening_hours, rating, is_open, owner_id) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?)")
        params = (name, address, phone_number, opening_hours, rating, is_open, owner_id)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("User inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def get_password(self, name):
        """Fetches password of a user using their name."""
        query = "SELECT password FROM Users WHERE name = ?"
        params = (name,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def get_user_id(self, name):
        """Fetches user_id of a user using their name."""
        query = "SELECT user_id FROM Users WHERE name = ?"
        params = (name,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    # Dashboard:
    def get_profile_data(self, user_id):
        """Fetches profile of a user using their user_id."""
        query = "SELECT * FROM Users WHERE user_id = ?"
        params = (user_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def update_profile_data(self, user_id, name, email, password, phone_number, address, is_active):
        """Updates a user info the using their user_id."""
        query = ("UPDATE Users"
                 "SET name = ?,"
                 "email = ?,"
                 "phone_number = ?,"
                 "address = ?,"
                 "is_active = ?"
                 "WHERE user_id = ?")
        params = (name, email, password, phone_number, address, is_active, user_id)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("User updated successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error updating data:", e)
            return None
        finally:
            conn.close()

    def delete_profile_data(self, user_id):
        """Deletes a user info the using their user_id."""
        query = "DELETE FROM Users WHERE user_id = ?"
        params = (user_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("User deleted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error deleting data:", e)
            return

    # Restaurant owner dashboard
    def get_restaurant_data(self, restaurant_id):
        """Fetches profile of a restaurant using its restaurant_id."""
        query = "SELECT * FROM Restaurants WHERE restaurant_id = ?"
        params = (restaurant_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def update_restaurant_data(self, restaurant_id, name, address,  phone_number, opening_hours, rating, is_open, owner_id):
        """Updates a restaurant info the using its restaurant_id."""
        query = ("UPDATE Restaurants"
                 "SET name = ?,"
                 "address = ?,"
                 "phone_number = ?,"
                 "opening_hours = ?,"
                 "rating = ?,"
                 "is_open = ?,"
                 "owner_id = ?"
                 "WHERE restaurant_id = ?")
        params = (name, address, phone_number, opening_hours, rating, is_open, owner_id, restaurant_id)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Restaurant updated successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error updating data:", e)
            return None
        finally:
            conn.close()

    def delete_restaurant_data(self, restaurant_id):
        """Deletes a restaurant info the using its restaurant_id."""
        query = "DELETE FROM Restaurants WHERE restaurant_id = ?"
        params = (restaurant_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Restaurant deleted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error deleting data:", e)
            return None
        finally:
            conn.close()

    # Foods of a restaurant
    def get_foods(self, restaurant_id):
        """Fetches foods of a restaurant using its restaurant_id."""
        query = "SELECT * FROM Foods WHERE restaurant_id = ?"
        params = (restaurant_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def insert_food(self, name, price, description, is_available, available_count, restaurant_id, rating):
        """Inserts food into the Foods table."""
        query = ("INSERT INTO Foods (name, price, description,"
                 "is_available, available_count, restaurant_id, rating) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?)")
        params = (name, price, description, is_available, available_count, restaurant_id, rating)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Food inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def delete_food(self, food_id):
        """Deletes a food using its food_id."""
        query = "DELETE FROM Foods WHERE food_id = ?"
        params = (food_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Food deleted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error deleting data:", e)
            return None
        finally:
            conn.close()

    def update_food(self, food_id, name, price, description, is_available, available_count, restaurant_id, rating):
        """Updates a food using its food_id."""
        query = ("UPDATE Foods"
                 "SET name = ?,"
                 "price = ?,"
                 "description = ?,"
                 "is_available = ?,"
                 "available_count = ?,"
                 "restaurant_id = ?,"
                 "rating = ?"
                 "WHERE food_id = ?")
        params = (name, price, description, is_available, available_count, restaurant_id, rating, food_id)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Food updated successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error updating data:", e)
            return None
        finally:
            conn.close()

    # Orders
    def get_orders_of_user(self, user_id):
        """Fetches orders of a user using their user_id."""
        query = "SELECT * FROM Orders WHERE user_id = ?"
        params = (user_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def get_orders_of_restaurant(self, restaurant_id):
        """Fetches orders of a restaurant using its restaurant_id."""
        query = "SELECT * FROM Orders WHERE restaurant_id = ?"
        params = (restaurant_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def insert_order(self, user_id, restaurant_id, food_id, order_date, delivery_date, status, total_price):
        """Inserts an order into the Orders table."""
        query = ("INSERT INTO Orders (user_id, restaurant_id, food_id,"
                 "order_date, delivery_date, status, total_price) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?)")
        params = (user_id, restaurant_id, food_id, order_date, delivery_date, status, total_price)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Order inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def cancel_order(self, order_id):
        """Cancels an order using its order_id."""
        query = ("UPDATE Orders"
                 "SET status = 'Cancelled' FROM Orders WHERE order_id = ?")
        params = (order_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Order cancelled successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error deleting data:", e)
            return None
        finally:
            conn.close()

    def complete_order(self, order_id):
        """Completes an order using its order_id."""
        query = ("UPDATE Orders"
                 "SET status = 'Completed' FROM Orders WHERE order_id = ?")
        params = (order_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Order completed successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error deleting data:", e)
            return None
        finally:
            conn.close()

    # Utilities
    def get_all_restaurants(self):
        """Fetches all restaurants."""
        query = "SELECT * FROM Restaurants"
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

    def 

# Test the DBHandler class
def test_db_handler():
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
    db_handler = DBHandler(connection_string)

    # Test insert_user
    db_handler.insert_user("John123", "john123@mail.com", "password", "1234567890", "123 Main St", "2021-09-01", 1, "Customer")

if __name__ == '__main__':
    test_db_handler()