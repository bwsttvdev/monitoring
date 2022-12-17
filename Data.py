import MySQLdb
from datetime import datetime
import psutil
import time

# Connect to MySQL database
db = MySQLdb.connect(
    host="vultr-prod-f0a9f906-d2a1-49ec-bdfb-c643c6285640-vultr-prod-e7e4.vultrdb.com",
    port=16751,
    user="vultradmin",
    password="AVNS_jEuX8-w2cNqo2JqoXdP",
    database="defaultdb"
)
cursor = db.cursor()

# Function to collect and store CPU usage data
def collect_cpu_data():
    # Get CPU usage data using psutil
    cpu_percent = psutil.cpu_percent()
    # Insert data into MySQL database
    sql = "INSERT INTO cpu_usage (percent, timestamp) VALUES (%s, %s)"
    val = (cpu_percent, datetime.now())
    cursor.execute(sql, val)
    db.commit()

# Function to collect and store memory usage data
def collect_memory_data():
    # Get memory usage data using psutil
    memory_percent = psutil.virtual_memory().percent
    # Insert data into MySQL database
    sql = "INSERT INTO memory_usage (percent, timestamp) VALUES (%s, %s)"
    val = (memory_percent, datetime.now())
    cursor.execute(sql, val)
    db.commit()

# Function to collect and store network traffic data
def collect_network_data():
    # Get network traffic data using psutil
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_recv = psutil.net_io_counters().bytes_recv
    # Insert data into MySQL database
    sql = "INSERT INTO network_traffic (bytes_sent, bytes_recv, timestamp) VALUES (%s, %s, %s)"
    val = (bytes_sent, bytes_recv, datetime.now())
    cursor.execute(sql, val)
    db.commit()

# Function to collect and store disk usage data
def collect_disk_data():
    # Get disk usage data using psutil
    disk_percent = psutil.disk_usage('/').percent
    # Insert data into MySQL database
    sql = "INSERT INTO disk_usage (percent, timestamp) VALUES (%s, %s)"
    val = (disk_percent, datetime.now())
    cursor.execute(sql, val)
    db.commit()

# Function to regularly collect and store resource data
def collect_resource_data():
    collect_cpu_data()
    collect_memory_data()
    collect_network_data()
    collect_disk_data()

# Collect and store resource data every 5 seconds
while True:
    collect_resource_data()
    time.sleep(5)
