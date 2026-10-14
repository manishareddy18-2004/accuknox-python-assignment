import requests
import sqlite3

r = requests.get('https://openlibrary.org/search.json?q=python')

print(r.status_code)

data = r.json()

print(data.keys())

books = data["docs"]

print("Total books:", len(books))

for book in data["docs"]:
    print(book.get("title"))
    print(book.get("author_name"))
    print(book.get("first_publish_year"))

seen_titles = set()
unique_books = []

for book in data["docs"]:
    title = book.get("title")

    if title and title not in seen_titles:
        print(title)
        seen_titles.add(title)
        unique_books.append(book)

print("Original books:", len(books))
print("Unique books:", len(unique_books))

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publication_year INTEGER
)
""")

connection.commit()

print("Database and table created successfully")

cursor.execute("DELETE FROM books")

for book in unique_books:
    title = book.get("title")

    authors = book.get("author_name", [])
    author = ", ".join(authors) if authors else "Unknown author"

    year = book.get("first_publish_year")

    cursor.execute("""
        INSERT INTO books (title, author, publication_year)
        VALUES (?, ?, ?)
    """, (title, author, year))

connection.commit()

print("Books inserted successfully")


cursor.execute("""
SELECT title, author, publication_year
FROM books
""")

rows = cursor.fetchall()

print("\nBooks retrieved from database:")

for row in rows:
    print("Title:", row[0])
    print("Author:", row[1])
    print("Publication year:", row[2])
    print("-" * 30)

connection.close()