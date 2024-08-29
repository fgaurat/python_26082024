import sqlite3
from Customer import Customer

class CustomerDAO:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    gender TEXT,
                    ip_address TEXT
                )
            ''')

    def insert(self, customer: Customer):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO customers (first_name, last_name, email, gender, ip_address)
                VALUES (?, ?, ?, ?, ?)
            ''', (customer.first_name, customer.last_name, customer.email, customer.gender, customer.ip_address))
            customer.id = cursor.lastrowid
        return customer

    def update(self, customer: Customer):
        with self.connection:
            self.connection.execute('''
                UPDATE customers
                SET first_name = ?, last_name = ?, email = ?, gender = ?, ip_address = ?
                WHERE id = ?
            ''', (customer.first_name, customer.last_name, customer.email, customer.gender, customer.ip_address, customer.id))

    def delete(self, customer_id: int):
        with self.connection:
            self.connection.execute('''
                DELETE FROM customers
                WHERE id = ?
            ''', (customer_id,))

    def find_by_id(self, customer_id: int) -> Customer:
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT id, first_name, last_name, email, gender, ip_address
            FROM customers
            WHERE id = ?
        ''', (customer_id,))
        row = cursor.fetchone()
        if row:
            return Customer(*row)
        else:
            return None

    def find_all(self) -> list[Customer]:
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT id, first_name, last_name, email, gender, ip_address
            FROM customers
        ''')
        rows = cursor.fetchall()
        return [Customer(*row) for row in rows]

    def __del__(self):
        self.connection.close()