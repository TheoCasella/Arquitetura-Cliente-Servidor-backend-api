from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    is_favorite: bool = False

    class Config:
        # Isso permite que o modelo trabalhe bem com dicionários ou objetos
        from_attributes = True