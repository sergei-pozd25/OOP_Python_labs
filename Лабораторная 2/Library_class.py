from typing import List

BOOKS = [
    {
        "id": 1,
        "name": "book_1",
        "pages": 100,
    },
    {
        "id": 2,
        "name": "book_2",
        "pages": 150,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id - int")
        if not isinstance(name, str):
            raise TypeError("name - str")
        if not isinstance(pages, int):
            raise TypeError("pages - int")
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}'

    def __repr__(self):
        return f"Book: id_={self.id}, name={self.name}, pages={self.pages})"

class Library:
    def __init__(self, books: List[Book] = []) -> None:
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int):
        if not isinstance(id_, int):
            raise TypeError("id - int")
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index
        raise ValueError('The book with the requested id does not exist')


if __name__ == '__main__':
    new_lib = Library()
    print(new_lib.get_next_book_id())

    books_list = [Book(id_=dict["id"], name=dict["name"],
                       pages=dict["pages"]) for dict in BOOKS]
    lib = Library(books=books_list)
    print(lib.get_next_book_id())
    print(lib.get_index_by_book_id(2))