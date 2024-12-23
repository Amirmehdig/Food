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
                 "is_active = ?,"
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
                 "owner_id = ?,"
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


