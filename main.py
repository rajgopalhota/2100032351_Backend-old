import psycopg2

dbname = 'Saifertek'
user = 'postgres'
password = '2003'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()
# Query with JOIN
query_with_join = """
SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM locations l
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name = 'Canada'
"""

cur.execute(query_with_join)

print("Query with JOIN:")
for row in cur.fetchall():
    print(row)

# Query without JOIN
query_without_join = """
SELECT location_id, street_address, city, state_province, 
    (SELECT country_name FROM countries WHERE countries.country_id = locations.country_id) AS country_name
FROM locations
WHERE country_id = 'CA';
"""

cur.execute(query_without_join)

print("\nQuery without JOIN:")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
