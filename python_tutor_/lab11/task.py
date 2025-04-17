import psycopg2
import csv
import os
import re
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






def search_by_pattern():
    pattern = input("enter part of first name, last name or phone: ")
    sql = """
        SELECT id, first_name, last_name, phone FROM phonebook
        WHERE first_name ILIKE %s OR last_name  ILIKE %s OR phone ILIKE %s ORDER BY id;
    """
    conn = connect()
    cur  = conn.cursor()
    cur.execute(sql, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    if rows:
        print("\nMatches:")
        for r in rows:
            print(r)
    else:
        print("no matches found (")
    cur.close()
    conn.close()





def insert_or_update_user():
    fname = input("first name: ")
    lname = input("last name: ")
    phone = input("phone number: ")

    conn = connect()
    cur  = conn.cursor()

    cur.execute(
        "SELECT id FROM phonebook WHERE first_name=%s AND last_name=%s;",
        (fname, lname)
    )
    exists = cur.fetchone()
    if exists:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE id=%s;",
            (phone, exists[0] )
        )
        print("phone updated: ", fname, lname)
    else:
        cur.execute(
            "INSERT INTO phonebook(first_name, last_name, phone) VALUES (%s, %s, %s);",
            (fname, lname, phone)
        )
        print("user added : ", fname, lname)

    conn.commit()
    cur.close()
    conn.close()
    


# inserting many users
def insert_many_users():
    n = int(input("how many users to add ? "))
    invalids = []
    conn = connect()
    cur  = conn.cursor()

    for i in range(n):
        fname = input("first name: ")
        lname = input("last name: ")
        phone = input("phone: ")
        # starts with + , 10-15 digits
        if not re.match(r'^\+?\d{10,15}$', phone):
            invalids.append((fname, lname, phone))
            continue

        
        cur.execute(
            """
            INSERT INTO phonebook(first_name, last_name, phone)
            VALUES (%s, %s, %s)
            """,
            (fname, lname, phone)
        )

    conn.commit()
    cur.close()
    conn.close()

    if invalids:
        print("\ninvalid : ")
        for i in invalids:
            print(" ", i)
    else:
        print("\nall contacts added")


def paginated_query():
    limit  = int(input("Limit per page: "))
    offset = int(input("Offset (rows to skip): "))
    sql = """
        SELECT id, first_name, last_name, phone
        FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s;
    """
    conn = connect()
    cur  = conn.cursor()
    cur.execute(sql, (limit, offset))
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(r)
    else:
        print("no rows in this range (")
    cur.close()
    conn.close()



# deleting user data
def delete_user_data():
    choice = input("delete by name or phone? (n, p) ").lower()
    conn = connect()
    cur  = conn.cursor()

    if choice == 'n':
        name = input("enten your first name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name=%s;", (name,))
    elif choice == 'p':
        phone = input("enter your phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s;", (phone,))
    else:
        print("invalid choice ( ")
        cur.close()
        conn.close()
        return

    if cur.rowcount:
        print("deleted", cur.rowcount, "records.")
    else:
        print("No matching record found.")

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
        print("6 Search by pattern")
        print("7 Insert or update if exist")
        print("8 Insert many users")
        print("9 Paginated query")
        print("10 Delete user data")
        print("11 Exit")

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
            search_by_pattern()
        elif choice == "7":
            insert_or_update_user()
        elif choice == "8":
            insert_many_users()
        elif choice == "9":
            paginated_query()
        elif choice == "10":
            delete_user_data()
        elif choice == "11":
            print("bye!")
            break
        else:
            print("try again!")


main()
