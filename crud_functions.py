import os
import sqlite3
connection = sqlite3.connect("telegram.db" )
cursor = connection.cursor()
cex = cursor.execute

def initiate_db():
    cex("""CREATE TABLE IF NOT EXISTS Products
    (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    img BLOB
    )
    """)
    connection.commit()

def get_all_products():
    cex("SELECT * from Products")
    return cursor.fetchall()

def create_items_for_db():
    for i in range(1,5):
        with open(os.path.join("images", f"img_{i}.png"), "rb") as file:
            cex("INSERT INTO Products (title, description, price, img) VALUES(?, ?, ?, ?)", (f'Product {i}', f'lalala{i}', i * 100, file.read()))
            connection.commit()


