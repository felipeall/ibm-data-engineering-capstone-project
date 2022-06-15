from datetime import datetime
# Import libraries required for connecting to mysql
import mysql.connector
# Import libraries required for connecting to DB2
import ibm_db
# Connect to MySQL
conn_mysql = mysql.connector.connect(user='root', password='Mjc3MDgtZmVsaXBl',host='127.0.0.1',database='sales')
cursor_mysql = conn_mysql.cursor()
# Connect to DB2
dsn_hostname = "19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "fsf66314"        # e.g. "abc12345"
dsn_pwd = "gvusYJmkiFuaOJdN"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "30699"                # e.g. "50000" 
dsn_database = "bludb"            # i.e. "BLUDB"
dsn_driver = "{IBM DB2 ODBC DRIVER}" # i.e. "{IBM DB2 ODBC DRIVER}"           
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              # i.e. "SSL"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

conn_db2 = ibm_db.connect(dsn, "", "")
# Find out the last rowid from DB2 data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database.

def get_last_rowid():
    query = ibm_db.exec_immediate(conn_db2, "SELECT MAX(rowid) FROM sales_data")
    while ibm_db.fetch_row(query) != False:
        return ibm_db.result(query, 0)

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    new_records_list = []
    timestamp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sql = f'''
    SELECT 
    rowid, product_id, customer_id, 0 as price, quantity, '{timestamp}' as timestamp
    FROM sales_data 
    WHERE rowid > {rowid}
    '''
    cursor_mysql.execute(sql)
    for row in cursor_mysql.fetchall():
        new_records_list.append(row)
    return new_records_list

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database.

def insert_records(records):
    for record in records:
        query = ibm_db.prepare(conn_db2, f"INSERT INTO sales_data VALUES{record}")
        ibm_db.execute(query)

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
conn_mysql.close()
# disconnect from DB2 data warehouse
ibm_db.close(conn_db2)
# End of program
