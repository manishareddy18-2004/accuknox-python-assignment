# AccuKnox AI/ML Trainee Assignment

**Candidate:** Muthumula Manisha Reddy  
**Role:** AI/ML Trainee  
**Technologies:** Python, REST APIs, SQLite, SQL, CSV, Pandas, Matplotlib

## Overview

This repository contains the coding tasks completed as part of the AccuKnox AI/ML Trainee assignment. The tasks cover REST API integration, data processing, database operations, and visualization. Links to additional Python and database projects are provided below.

## Repository Structure

```text
accuknox-assignment/
├── task1_books_api/
│   └── task1_books.py
├── task2_student_scores/
│   └── task2_scores.py
├── task3_csv_sqlite/
│   ├── task3_users.py
│   └── users.csv
├── README.md
└── requirements.txt
```

*Note: Update the structure above to match the actual filenames and folders in your repository.*

## Coding Tasks

### Task 1: Books API and SQLite

**Objective:** Retrieve book information from a REST API and store the relevant data in a local SQLite database.

**Key concepts:**
- HTTP requests and JSON response handling
- Extracting relevant book details
- SQLite database and table operations
- Inserting and retrieving records using SQL

**Run:**

```bash
python3 task1_books.py
```

### Task 2: Student Scores Analysis

**Objective:** Retrieve student score data from a REST API, calculate average scores, and visualize the results using a bar chart.

**Key concepts:**
- REST API integration
- JSON data processing
- Average score calculation
- Data visualization using Matplotlib

**Run:**

```bash
python3 task2_scores.py
```

### Task 3: CSV Data Import into SQLite

**Objective:** Read user information from a CSV file and store the records in an SQLite database.

**Key concepts:**
- CSV file handling
- Structured data processing
- SQLite table creation and record insertion
- SQL-based data retrieval

**Run:**

```bash
python3 task3_users.py
```

Ensure the CSV file is available at the path expected by the Python script.

## Additional Complex Projects

### 1. RAG-Based Intelligent Document Assistant

A Python-based document question-answering project that uses a Retrieval-Augmented Generation (RAG) workflow to retrieve relevant document context and generate responses using a language model.

**Technologies:** Python, FastAPI, Large Language Models, Retrieval-Augmented Generation.

**Source code:** [Add your RAG project GitHub URL here]

### 2. Advanced Database Management System

A Python and SQLite project focused on structured data storage, database operations, and SQL-based information retrieval.

**Technologies:** Python, SQLite, SQL.

**Source code:** [Add your database project GitHub URL here]

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone YOUR_ASSIGNMENT_REPOSITORY_URL
   ```

2. Navigate to the downloaded repository:

   ```bash
   cd accuknox-assignment
   ```

3. Install the dependencies listed in `requirements.txt`:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Run each task using the commands in its respective section.

**Note:** The commands assume the Python files are in the repository root. If your files are inside separate task folders, use their actual paths when running them.

## Assumptions and Notes

- API responses are processed according to the structure returned by the respective endpoints.
- Internet connectivity is required for tasks that fetch data from external APIs.
- SQLite databases are stored locally and may be generated when the scripts run.
- Required input files, including CSV files, must be available at the paths expected by the code.
- Dependencies and execution instructions should be checked against the actual project files before running.

## Author

**Muthumula Manisha Reddy**

GitHub: https://github.com/manishareddy18-2004  
Email: venkatamanishareddymuthumula@gmail.com
