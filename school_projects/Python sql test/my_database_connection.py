import mysql.connector

# Open the file containing city and country data
subor_mesta_krajiny = open("4.roč/zimne-prazdniny/mesta1.txt", "r")

# Establish the database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V4pnzaox13",
    database="payment_db"
)

# Create a cursor object
cursor = mydb.cursor()

# Initialize the ID counter
