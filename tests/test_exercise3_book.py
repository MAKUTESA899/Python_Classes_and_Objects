import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exercises.exercise3_book import Book

@pytest.fixture(autouse=True)
def reset_book_count():
    # Reset the book count before each test
    Book.total_books = 0

def test_book_attributes():
    book = Book("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.pages == 328

def test_description():
    book = Book("1984", "George Orwell", 328)
    assert book.description() == "'1984' by George Orwell, 328 pages"

def test_total_good_books():
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("Brave New World", "Aldous Huxley", 268)
    assert Book.total_books == 2