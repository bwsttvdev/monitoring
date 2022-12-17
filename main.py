import MySQLdb
import time


# Connect to MySQL database
# Connect to MySQL database
db = MySQLdb.connect(
    host="vultr-prod-f0a9f906-d2a1-49ec-bdfb-c643c6285640-vultr-prod-e7e4.vultrdb.com",
    port=16751,
    user="vultradmin",
    password="AVNS_jEuX8-w2cNqo2JqoXdP",
    database="defaultdb"

)
cursor = db.cursor()

# Function to query and display latest resource data
# Function to query and display latest resource data
def display_resource_data():
    # Query latest CPU usage data from MySQL database
    cursor.execute("SELECT * FROM cpu_usage WHERE CONVERT_TZ(timestamp, @@session.time_zone, 'UTC') > DATE_SUB(NOW(), INTERVAL 1 MINUTE) ORDER BY timestamp DESC LIMIT 1")
    cpu_data = cursor.fetchone()
    cpu_percent = cpu_data[1]
    cpu_timestamp = cpu_data[2]

    # Query latest memory usage data from MySQL database
    cursor.execute("SELECT * FROM memory_usage WHERE CONVERT_TZ(timestamp, @@session.time_zone, 'UTC') > DATE_SUB(NOW(), INTERVAL 1 MINUTE) ORDER BY timestamp DESC LIMIT 1")
    memory_data = cursor.fetchone()
    memory_percent = memory_data[1]
    memory_timestamp = memory_data[2]

    # Query latest network traffic data from MySQL database
    cursor.execute("SELECT * FROM network_traffic WHERE CONVERT_TZ(timestamp, @@session.time_zone, 'UTC') > DATE_SUB(NOW(), INTERVAL 1 MINUTE) ORDER BY timestamp DESC LIMIT 1")
    network_data = cursor.fetchone()
    bytes_sent = network_data[1]
    bytes_recv = network_data[2]
    network_timestamp = network_data[3]

    # Query latest disk usage data from MySQL database
    cursor.execute("SELECT * FROM disk_usage WHERE CONVERT_TZ(timestamp, @@session.time_zone, 'UTC') > DATE_SUB(NOW(), INTERVAL 1 MINUTE) ORDER BY timestamp DESC LIMIT 1")
    disk_data = cursor.fetchone()
    disk_percent = disk_data[1]
    disk_timestamp = disk_data[2]

    # Display latest resource data as text
    print("CPU usage: {}% at {}".format(cpu_percent, cpu_timestamp))
    print("Memory usage: {}% at {}".format(memory_percent, memory_timestamp))
    print("Network traffic: {} bytes sent, {} bytes received at {}".format(bytes_sent, bytes_recv, network_timestamp))
    print("Disk usage: {}% at {}".format(disk_percent, disk_timestamp))

# Repeatedly query and display latest resource data
while True:
    display_resource_data()
    # Pause execution for 1 second between each query
    time.sleep(5)