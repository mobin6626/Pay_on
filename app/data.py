import sqlite3


def connect():
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
       "CREATE TABLE IF NOT EXISTS salary (id INTEGER PRIMARY KEY , name text, age INTEGER , price INTEGER )"
    )
    conn.commit()
    conn.close()


def insert(name, age, price):
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO salary VALUES (NULL ,?,?,?)", (name ,age ,price)
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM salary"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", age="", price=""):
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM salary WHERE name = ? OR age = ? OR price = ?", (name, age, price)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(name, age, price):
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
        "DELETE * FROM salary WHERE name = ? OR age = ? OR price = ?", (name, age, price)
    )
    conn.commit()
    conn.close()

def update(id, name, age, price):
    conn = sqlite3.connect("waiters.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE salary SET name = ?, age = ?, price = ? WHERE id = ?", (name, age, price, id)
    )
    conn.commit()
    conn.close()



connect()

