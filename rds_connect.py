import pyodbc

# Define your connection parameters
server = 'ms-sql-database.cn2q2se4kvvq.us-east-1.rds.amazonaws.com'
database = 'ms-sql-database'
username = 'admin'
password = '8KXONi#MvPmiwxe7.<Q!B_FQk<$U'
port = '1433'  # Default SQL Server port

# Create the connection string
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"

# Connect to the database
connection = pyodbc.connect(connection_string)

# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT @@VERSION;")

# Fetch and print the result
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

# Close the connection
cursor.close()
connection.close()