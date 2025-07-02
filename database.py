import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ev_swap_db",
        user="postgres",
        password="Dechin@123",
        host="localhost",
        port="5432"
    )
