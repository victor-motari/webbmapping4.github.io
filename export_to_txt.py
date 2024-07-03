import psycopg2

# Database connection parameters
db_info = {
    'dbname': 'web mapping db',
    'user': 'postgres',
    'password': '1234567890',
    'host': '127.0.0.1',
    'port': '5432'
}

# Connect to the database
try:
    conn = psycopg2.connect(**db_info)
    cur = conn.cursor()
    print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Query to fetch data
query = 'SELECT "national park", "northings", "eastings", "area_sq_km", "county" FROM "coordinates of national parks"'

# Fetch data and write to a text file
try:
    cur.execute(query)
    rows = cur.fetchall()
    with open('data.txt', 'w') as f:
        for row in rows:
            f.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n')
    print("Data written to data.txt successfully!")
except Exception as e:
    print(f"Error executing query: {e}")
finally:
    cur.close()
    conn.close()
