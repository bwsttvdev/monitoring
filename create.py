import MySQLdb

# Connect to MySQL database
db = MySQLdb.connect(
    host="vultr-prod-f0a9f906-d2a1-49ec-bdfb-c643c6285640-vultr-prod-e7e4.vultrdb.com",
    port=16751,
    user="vultradmin",
    password="AVNS_jEuX8-w2cNqo2JqoXdP",
    database="defaultdb"
)
cursor = db.cursor()

# Drop old network traffic table
cursor.execute("DROP TABLE network_traffic")

# Create new network traffic table with primary key and larger data type for bytes_recv column
cursor.execute("CREATE TABLE network_traffic (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, bytes_sent BIGINT, bytes_recv BIGINT, timestamp DATETIME)")