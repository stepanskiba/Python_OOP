class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        #print(key, value)
        if key == 'title' and type(value) is str:
            object.__setattr__(self, key, value)
        elif key == 'author' and type(value) is str:
            object.__setattr__(self, key, value)
        elif key == 'pages' and type(value) is int:
            object.__setattr__(self, key, value)
        elif key == 'year' and type(value) is int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(book.author)