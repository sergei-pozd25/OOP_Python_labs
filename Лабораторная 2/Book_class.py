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


if __name__ == '__main__':
    books_list = [Book(id_=book_dict["id"], name=book_dict["name"],
             pages=book_dict["pages"]) for book_dict in BOOKS]
    for book in books_list:
        print(book)
    print(books_list)