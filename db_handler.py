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
