from models import Book
from sqlalchemy.orm import session
from schemas import BookCreate

def create_book(db:session,data:BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_book(db:session):
    return db.query(Book).all()

def get_books(db:session, book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db:session, book:BookCreate, book_id:int):
    book_query = db.query(Book).filter(Book.id == book_id).first()
    if book_query:
        for key, value in book.model_dump().items():
            setattr(book_query, key, value)
        db.commit()
        db.refresh(book_query)
    return book_query

def delete_book(db:session, id:int):
    book_queryset = db.query(Book).filter(Book.id == id).first()
    if book_queryset:
        db.delete(book_queryset)
        db.commit()
    return book_queryset