"""
Filename: main.py
Author: Luis Felipe Porto
Date: 28-07-2026
Version: 1.0
Description: Main entry point for the Docker Learning Lab application.
This module initializes the FastAPI application, manages the PostgreSQL
connection, and exposes the API endpoints for creating and retrieving books.
Contact: luisfelipeporto.lfp@gmail.com
"""

# Imports
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Load environment variables
load_dotenv()

# Create the FastAPI application
app = FastAPI()

# Database connection function
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Define the Book model
class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int

# Route 1: Root endpoint
@app.get("/")
def root() -> dict:
    return {
        "message": "Welcome to Docker Learning Lab!",
        "author": "Luis Felipe Porto"
    }

# Route 2: Create a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> dict:

    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Insert the new book into the database
        cursor.execute(
            """
            INSERT INTO books (title, author, genre, year)
            VALUES (%s, %s, %s, %s)
            """,
            (book.title, book.author, book.genre, book.year)
        )

        conn.commit()

        return {
            "message": "Book created successfully!",
            "book": book
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create the book: {str(e)}"
        )

    finally:
        # Always close the cursor and database connection
        if cursor:
            cursor.close()

        if conn:
            conn.close()

# Route 3: Get all books
@app.get("/books")
def get_books() -> list:

    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Fetch all books from the database
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        return books

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve books: {str(e)}"
        )

    finally:
        # Always close the cursor and database connection
        if cursor:
            cursor.close()

        if conn:
            conn.close()

# Route 4: Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    # Connect to the database and delete the selected book
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        DELETE FROM books
        WHERE id = %s
        """,
        (book_id,)
    )

    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {
        "message": "Book deleted successfully!"
    }

# Route 5: Health check endpoint
@app.get("/health")
def health_check() -> dict:
    return {
        "status": "healthy"
    }