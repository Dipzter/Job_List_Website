import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create the jobs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    title TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("✅ jobs.db created with 'jobs' table.")
