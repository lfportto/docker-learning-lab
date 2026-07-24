from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import psycopg2
import os

# Load environment variables
load_dotenv()

# Database connection function
def get_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

app = FastAPI()

# Define the Book model
class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int

# Route 1: Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Docker Learning Lab!",
        "author": "Luis Felipe Porto"
    }

# Route 2: Create a new book
@app.post("/books")
def create_book(book: Book):

    # Connect to the database and insert the new book
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute(
        """
        INSERT INTO books (title, author, genre, year)
        VALUES (%s, %s, %s, %s)
        """,
        (book.title, book.author, book.genre, book.year)
    )

    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {
        "message": "Book created successfully!",
        "book": book
    }

# Route 3: Get all books
@app.get("/books")
def get_books():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # Fetch all books from the database
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return books

# Route 4: Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }