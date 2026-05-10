from app.models.book import Book
from typing import List

class BookService:
    def __init__(self):
        # Simulação de banco de dados em memória
        self.books: List[Book] = [
            Book(id=1, title="Dom Casmurro", author="Machado de Assis"),
            Book(id=2, title="O Alquimista", author="Paulo Coelho")
        ]

    def get_all_books(self, search: str = None):
        if search:
            # Filtra ignorando maiúsculas/minúsculas
            return [b for b in self.books if search.lower() in b.title.lower()]
        return self.books

    def toggle_favorite(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                book.is_favorite = not book.is_favorite
                return book
            return None

    def toggle_favorite(self, book_id: int):
        for book in self.books:
            if book.id == book_id:
                book.is_favorite = not book.is_favorite
                return book
        return None

# Instanciamos aqui para que o estado da lista seja mantido durante a execução
book_service = BookService()