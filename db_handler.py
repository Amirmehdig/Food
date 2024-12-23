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

    def insert_to_food_table(self, name, price, category_id):
        """Inserts a new item into the food table."""
        query = "INSERT INTO food (name, price, category_id) VALUES (?, ?, ?)"
        params = (name, price, category_id)
        conn = self.get_connection()
        if not conn:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("Insert successful!")
            return True
        except Exception as e:
            print("Error inserting data:", e)
            return False
        finally:
            conn.close()

    def get_food_by_category(self, category_id):
        """Fetches food items based on category."""
        query = "SELECT id, name, price FROM food WHERE category_id = ?"
        params = (category_id,)
        conn = self.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "price": row[2]} for row in results]
        except Exception as e:
            print("Error fetching data:", e)
            return None
        finally:
            conn.close()

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
        params = (name)
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
        params = (name)
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
        params = (user_id)
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
                 "WHERE id = ?")
        params = (name, email, password, phone_number, address, is_active, user_id)
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

    def 




