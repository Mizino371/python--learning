import mysql.connector

# Establish the database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V4pnzaox13"
)

# Create a cursor object
cursor = mydb.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS payment_db")

# Use the database
cursor.execute("USE payment_db")

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        payment_date DATE NOT NULL,
        payment_time TIME NOT NULL,
        payment_method VARCHAR(50) NOT NULL,
        paid_amount DECIMAL(10, 2) NOT NULL
    )
""")

# Close the cursor and connection
cursor.close()
mydb.close()