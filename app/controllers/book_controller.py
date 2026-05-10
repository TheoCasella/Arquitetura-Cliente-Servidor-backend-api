from fastapi import APIRouter
from app.models.book import Book
from app.services.book_service import book_service

router = APIRouter()

@router.get("/books")
def list_books():
    return book_service.get_all_books()

@router.post("/books")
def add_book(book: Book):
    return book_service.create_book(book)

@router.get("/books")
def list_books(search: str = None): # Aceita parâmetro ?search=nome
    return book_service.get_all_books(search)

@router.patch("/books/{book_id}/favorite") # Rota para favoritar
def toggle_book_favorite(book_id: int):
    return book_service.toggle_favorite(book_id)