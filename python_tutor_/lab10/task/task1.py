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


def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone VARCHAR(15) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("success!")


def insert_from_csv():
    csv_filename = input("Enter CSV file path: ")
    try:
        conn = connect()
        cur = conn.cursor()
        with open(csv_filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                cur.execute("""
                    INSERT INTO phonebook (first_name, last_name, phone)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone) DO NOTHING;
                """, row)
        conn.commit()
        cur.close()
        conn.close()
        print("uploaded successfully from csv")
    except Exception as e:
        print(e)



def insert_user():
    fname = input("Enter first Name: ")
    lname = input("Enter last Name: ")
    phone = input("Enter phone number: ")

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone)
            VALUES (%s, %s, %s)
            ON CONFLICT (phone) DO NOTHING;
        """, (fname, lname, phone))
        conn.commit()
        print("User added")
    except psycopg2.Error as e:
        print(e)
    cur.close()
    conn.close()



def update_phone():
    old_phone = input("Enter old phone number: ")
    new_phone = input("Enter new phone number: ")

    conn = conn()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s;", (new_phone, old_phone))
    if cur.rowcount > 0:
        print("updated successfully!")
    else:
        print("Phone number not found")
    conn.commit()
    cur.close()
    conn.close()


def search_user():
    search_term = input("Enter name or phone to search: ")

    conn = connect()
    cur = conn.cursor()
    query = "SELECT * FROM phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone ILIKE %s;"
    cur.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
    results = cur.fetchall()
    
    if results:
        print("\nResults: ")
        for row in results:
            print(row)
    else:
        print("Not found")

    cur.close()
    conn.close()

def delete_user():
    username = input("Enter usernmae delete: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (username))
    
    if cur.rowcount > 0:
        print("User deleted")
    else:
        print("user not found")
    
    conn.commit()
    cur.close()
    conn.close()



    

# CLI Menu
def main():
    # create_table() # already created in dev (local)
    while True:
        print("\nPHONEBOOK MENU")
        print("1 Insert from CSV")
        print("2 Insert manually")
        print("3 Update phone number")
        print("4 Search contacts")
        print("5 Delete contact")
        print("6 Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_user()
        elif choice == "3":
            update_phone()
        elif choice == "4":
            search_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("bye!")
            break
        else:
            print("try again!")


main()

