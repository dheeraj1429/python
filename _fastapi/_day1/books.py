from fastapi import FastAPI, Path, Query
from typing import List, Optional
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., min_length=1, max_length=100, example="The Hobbit")
    author: str = Field(..., min_length=1, example="J.R.R. Tolkien")
    category: str = Field(..., example="fantasy")

class UpdateBook(BaseModel):
  id: int = Field(..., example=1)
  title: Optional[str] = None
  author: Optional[str] = None
  category: Optional[str] = None

books: List[Book] = [
  Book(id=1, title="Title one", author="Author one", category="science"),
  Book(id=2, title="Title two", author="Author two", category="science"),
  Book(id=3, title="Title three", author="Author three", category="math"),
  Book(id=4, title="Title four", author="Author four", category="math"),
  Book(id=5, title="Title five", author="Author five", category="science"),
  Book(id=6, title="Title six", author="Author six", category="science"),
]

@app.get('/books')
async def get_books():
  return books

@app.get('/book/')
async def get_book_by_id_query(
  book_id: str | None = Query(
    default=None,
    description="The unique ID of the book to retrieve",
  )
):
  if book_id:
    for book in books:
      if book.id == int(book_id): return book
  return None

@app.get('/book/category/')
async def get_book_by_id_query(
  category: str | None = Query(
    default=None,
    description="The unique ID of the book to retrieve",
  )
):
  if not category:
    return None
  return list(filter(lambda book: book.category == category, books))

@app.get("/book/{book_id}")
async def get_book_by_id(
  book_id: int = Path(
    ...,
    ge=1,
    le=6,
    description="The unique ID of the book to retrieve",
  )
):
  for book in books:
    if book.id == book_id: return book

  return None

@app.post('/book')
async def add_book(book: Book):
  books.append(book)
  return True

@app.put("/book/update")
async def update(update_book_payload: UpdateBook):
  for book in books:
    if book.id == update_book_payload.id:
      book.title =  update_book_payload.title or book.title
      book.category = update_book_payload.category or book.category
      book.title = update_book_payload.title or book.title
  return True