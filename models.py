from database import get_connection

def register_user(username, email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password))
    conn.commit()
    conn.close()

def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cur.fetchone()
    conn.close()
    return user

def search_stations(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stations WHERE city ILIKE %s OR pincode ILIKE %s",
                (f'%{query}%', f'%{query}%'))
    results = cur.fetchall()
    conn.close()
    return results
