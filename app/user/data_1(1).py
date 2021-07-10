import sqlite3


def connect():
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute(
       "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY , name text , price INTEGER )"
    )
    conn.commit()
    conn.close()


def insert(name, price):
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items VALUES (NULL ,?,?)", (name, price)
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", price=""):
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items WHERE name = ? OR price = ?", (name, price)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, price):
    conn = sqlite3.connect("items.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET name = ?, price = ? WHERE id = ?", (name, price, id)
    )
    conn.commit()
    conn.close()


connect()

