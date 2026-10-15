# AccuKnox AI/ML Trainee Assignment

## Overview

This repository contains my solutions for the AccuKnox AI/ML Trainee assignment. It demonstrates REST API integration, Python data processing, SQLite database operations, data visualization, and CSV data import.

## Technologies Used

- Python 3
- REST APIs and JSON
- Requests
- SQLite and SQL
- CSV processing
- Matplotlib

## Problem Statement 1: Python Programming Tasks

### Task 1: API Data Retrieval and Storage

**File:** `task1_books.py`

- Fetches book data from the Open Library REST API.
- Extracts book titles, authors, and publication years from JSON.
- Removes duplicate book titles.
- Stores book information in an SQLite database.
- Retrieves and displays the stored records.

**Concepts:** REST APIs, HTTP requests, JSON parsing, Python sets, SQLite, and SQL queries.

### Task 2: Data Processing and Visualization

**File:** `task2_scores.py`

- Fetches student score data from a REST API.
- Processes student names and subject scores.
- Calculates each student's average score.
- Generates a bar chart to visualize the average scores.

**Concepts:** API integration, data processing, average calculation, and data visualization.

### Task 3: CSV Data Import to Database

**Files:** `task3_csv.py`, `users.csv`, `users.db`

- Reads user information from a CSV file.
- Creates a `users` table in SQLite.
- Inserts user names and email addresses using parameterized SQL queries.
- Retrieves and displays the stored records.

**Concepts:** CSV handling, SQLite database creation, SQL INSERT and SELECT operations.

**Note:** The current implementation does not automatically remove duplicate user records.

## Problem Statement 2: Theory Answers

**File:** `theory answers.pdf`

The PDF contains responses to the theoretical questions in the assignment:

- Self-assessment of LLM, Deep Learning, AI, and ML skills.
- High-level architecture of an LLM-based chatbot.
- Explanation of vector databases and selection of a suitable database for a hypothetical use case.

## Most Complex Python Project

### Advanced Python RAG System

**File:** `advanced-rag-system-main.zip`

An advanced Python project focused on retrieval-augmented generation (RAG) for document-based question answering.

The project explores retrieving relevant document information and using a language model to generate context-aware responses.

## Most Complex Database Project

### Advanced Python Database Analytics

**File:** `advanced-database-analytics-main.zip`

An advanced Python project focused on database management, data retrieval, SQL operations, and analytics.

The project demonstrates work related to structured data management and database querying.

## How to Run

### Prerequisites

- Python 3
- `requests`
- `matplotlib`

Install the required libraries:

```bash
pip install requests matplotlib
```

Run the scripts individually:

```bash
python3 task1_books.py
python3 task2_scores.py
python3 task3_csv.py
```

For the API-based tasks, an internet connection is required. For Task 3, ensure that `users.csv` is in the same directory as `task3_csv.py`.

## Assumptions

- The Open Library Search API is used as the external source for book information.
- Student score data is retrieved from the API specified in the Python script.
- The CSV file contains `name` and `email` columns.
- SQLite is used as the local database.

## Author

**Muthumula Manisha Reddy**

GitHub Profile: https://github.com/manishareddy18-2004

Assignment Repository: https://github.com/manishareddy18-2004/accuknox-python-assignment
