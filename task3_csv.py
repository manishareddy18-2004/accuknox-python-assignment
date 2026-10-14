import csv
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

# Read data from the CSV file
with open("users.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

# Save the changes
connection.commit()

# Display the stored data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)

# Close the database connection
connection.close()