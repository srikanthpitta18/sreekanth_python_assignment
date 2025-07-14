from abc import ABC, abstractmethod
import mysql.connector

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_data(self, table_name):
        pass

    @abstractmethod
    def close(self):
        pass

class MySQLConnector(DatabaseInterface):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print(" Connected to MySQL Workbench database.")
        except Exception as e:
            print(" Connection failed:", e)

    def fetch_data(self, table_name):
        try:
            query = f"SELECT * FROM {table_name};"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            print(f"\n Data from table '{table_name}':")
            for row in rows:
                print(row)
        except Exception as e:
            print(" Failed to fetch data:", e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print(" Connection closed.")

# -------- Main Execution --------
if __name__ == "__main__":
    host = input("Enter MySQL host (e.g., localhost): ")
    user = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")
    table = input("Enter table name to fetch data from: ")

    db = MySQLConnector(host, user, password, database)
    db.connect()
    db.fetch_data(table)
    db.close()
