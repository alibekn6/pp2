import psycopg2
from config import load_config


def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (vendor_name,))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id


def insert_many_vendors(vendor_list):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, vendor_list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_many_parts(part_list):
    sql = """INSERT INTO parts(part_name) VALUES(%s) RETURNING *"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, part_list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_vendor_parts(list):
    sql = """INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s) RETURNING *"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


vendors = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
]

parts = [
        ('Antenna',),
        ('Home Button.',),
        ('LTE Modem',),
        ('SIM Tray',),
        ('Speaker.',),
        ('Camera',)
]

vendor_parts = [
        (25, 6),
        (25, 5),
        (26, 5),
        (26, 2),
        (27, 6),
        (27, 1),
        (28, 3),
        (28, 5),
        (29, 2),
        (29, 3),
        (30, 1),
        (30, 4),
        (31, 1),
        (31, 4)
]


if __name__ == '__main__':
    # print(insert_vendor("3M Co."))
    # insert_many_vendors(vendors)
    # insert_many_parts(parts)
    insert_vendor_parts(vendor_parts)