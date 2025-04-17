import psycopg2
import csv

import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 5432)


def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
)


def search_by_pattern():
    pattern = input("enter pattern: ")
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_users(%s);", (pattern,))
    results = cur.fetchall()

    if results:
        print("results")
        for row in results:
            print(row)

    else:
        print("no match found (")
    cur.close()
    conn.close()


def insert_or_update_user():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone = input("Enter phone number: ")

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("CALL insert_or_update_user(%s, %s, %s);", (fname, lname, phone))
        conn.commit()
        print("User inserted or updated.")
    except Exception as e:
        print("Error:", e)
    cur.close()
    conn.close()





def insert_multiple_users():
    from ast import literal_eval

    raw_input = input("Enter users as [(fname, lname, phone), ...]: ")
    try:
        users = literal_eval(raw_input)  # Safely parse string into list of tuples
        first_names = [u[0] for u in users]
        last_names = [u[1] for u in users]
        phones = [u[2] for u in users]

        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM insert_multiple_users(%s, %s, %s);", (first_names, last_names, phones))
        invalids = cur.fetchall()

        if invalids:
            print("Invalid or failed inserts:")
            for row in invalids:
                print(row)
        else:
            print("All users inserted successfully.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)



insert_multiple_users()
# seeds 
"""
[("John", "Doe", "+1234567890"),("Jane", "Smith", "+1987654321"),("Alice", "Johnson", "+1122334455"),("Bob", "Williams", "+9988776655")]
"""
