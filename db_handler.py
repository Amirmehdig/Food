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
            print("Restaurant inserted successfully!")
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
        query = ("UPDATE Users "
                 "SET name = ?, "
                 "email = ?, "
                 "password = ?, "
                 "phone_number = ?, "
                 "address = ?, "
                 "is_active = ? "
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
        query = ("UPDATE Restaurants "
                 "SET name = ?, "
                 "address = ?, "
                 "phone_number = ?, "
                 "opening_hours = ?, "
                 "rating = ?, "
                 "is_open = ?, "
                 "owner_id = ? "
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
    def get_food_by_food_id(self, food_id):
        """Fetches food using its food_id."""
        query = "SELECT * FROM Food WHERE food_id = ?"
        params = (food_id,)
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

    def get_food_by_restaurant_id(self, restaurant_id):
        """Fetches foods of a restaurant using its restaurant_id."""
        query = "SELECT * FROM Food WHERE restaurant_id = ?"
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
        """Inserts food into the Food table."""
        query = ("INSERT INTO Food (name, price, description,"
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
        query = "DELETE FROM Food WHERE food_id = ?"
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
        query = ("UPDATE Food "
                 "SET name = ?, "
                 "price = ?, "
                 "description = ?, "
                 "is_available = ?, "
                 "available_count = ?, "
                 "restaurant_id = ?, "
                 "rating = ? "
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
    def get_order_headers_of_user(self, user_id):
        """Fetches order headers of a user using their user_id."""
        query = "SELECT * FROM OrderHeader WHERE user_id = ?"
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

    def get_order_details(self, order_id):
        """Fetches order details using its order_id."""
        query = "SELECT * FROM OrderDetail WHERE order_id = ?"
        params = (order_id,)
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

    def get_order_headers_of_restaurant(self, restaurant_id):
        """Fetches order headers of a restaurant using its restaurant_id."""
        query = "SELECT * FROM OrderHeader WHERE restaurant_id = ?"
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

    def get_order_headers_of_delivery_person(self, delivery_person_id):
        """Fetches order headers of a delivery person using their delivery_person_id."""
        query = "SELECT * FROM OrderHeader WHERE delivery_person_id = ?"
        params = (delivery_person_id,)
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

    def insert_full_order(self, total_amount, status, user_id, restaurant_id, delivery_person_id):
        """Inserts an order into the Orders table."""
        query = ("INSERT INTO OrderHeader (order_date, total_amount, delivery_time,"
                 "status, user_id, restaurant_id, delivery_person_id) "
                 "VALUES (GETDATE(), ?, NULL, ?, ?, ?, ?);"
                 "SELECT SCOPE_IDENTITY();")
        params = (total_amount, status, user_id, restaurant_id, delivery_person_id)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            cursor.execute("SELECT @@IDENTITY;")
            order_id = int(cursor.fetchone()[0])
            conn.commit()
            print("Order inserted successfully!")
            return order_id
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def insert_order_detail(self, order_id, food_id, quantity, subtotal):
        """Inserts an order detail into the OrderDetail table."""
        query = ("INSERT INTO OrderDetail (order_id, food_id, quantity, subtotal) "
                 "VALUES (?, ?, ?, ?)")
        params = (order_id, food_id, quantity, subtotal)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Order detail inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def cancel_order(self, order_id):
        """Cancels an order using its order_id."""
        query = ("UPDATE OrderHeader "
                 "SET status = 'Canceled' WHERE order_id = ?")
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
        query = ("UPDATE OrderHeader "
                 "SET status = 'Delivered', delivery_time = GETDATE() WHERE order_id = ?")
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

    # Comments
    def post_comment(self, order_id, rating, comment_text):
        """Posts a comment into the Comments table."""
        query = ("INSERT INTO Comments (order_id, rating, comment_text, comment_date) "
                 "VALUES (?, ?, ?, GETDATE())")
        params = (order_id, rating, comment_text)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Comment posted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def get_comments_of_user(self, user_id):
        """Fetches comments of a user using their user_id."""
        query = ("SELECT comment_id, order_id, rating, comment_text, comment_date "
                 "FROM "
                 "Comments INNER JOIN OrderHeader ON Comments.order_id = OrderHeader.order_id")
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

    def get_comments_of_restaurant(self, restaurant_id):
        """Fetches comments of a restaurant using its restaurant_id."""
        query = ("SELECT comment_id, order_id, rating, comment_text, comment_date "
                 "FROM "
                 "Comments INNER JOIN OrderHeader ON Comments.order_id = OrderHeader.order_id")
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

    # Delivery People
    def insert_delivery_person(self, name, phone_number, vehicle_type, vehicle_number, availability_status):
        """Inserts a delivery person into the DeliveryPerson table."""
        query = ("INSERT INTO DeliveryPerson (name, phone_number, vehicle_type,"
                 "vehicle_number, availability_status) "
                 "VALUES (?, ?, ?, ?, ?)")
        params = (name, phone_number, vehicle_type, vehicle_number, availability_status)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Delivery person inserted successfully!")
            return cursor.rowcount
        except Exception as e:
            print("Error inserting data:", e)
            return None
        finally:
            conn.close()

    def get_delivery_person_by_id(self, delivery_person_id):
        """Fetches delivery person using their delivery_person_id."""
        query = "SELECT * FROM DeliveryPerson WHERE delivery_person_id = ?"
        params = (delivery_person_id,)
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

    # Admin and Utilities
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

    def get_all_users(self):
        """Fetches all users."""
        query = "SELECT * FROM Users"
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

    def get_all_foods(self):
        """Fetches all foods."""
        query = "SELECT * FROM Food"
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

    def get_vRestaurantCustomers(self):
        query = "SELECT * FROM vDeliveryPersonSummary"
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

    def get_vCustomers(self):
        query = "SELECT * FROM vCustomers"
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

    def get_vDeliveryPersonSummary(self):
        query = "SELECT * FROM vDeliveryPersonSummary"
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
        

# Test the DBHandler class
def test_db_handler():
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
    order_id = db_handler.insert_full_order(20.98, 'Delivered', 1, 1, 1)
    print(order_id)


if __name__ == '__main__':
    test_db_handler()
