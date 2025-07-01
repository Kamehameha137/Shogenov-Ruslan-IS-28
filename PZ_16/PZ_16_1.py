#Вариант 31

#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги

class Book:
    def __init__(self, title="", author="", pages=0):
        self._title = title  
        self._author = author  
        self._pages = pages  
    
    def read_book(self):
          return {
               "название": self._title,
               "автор": self._author,
               "страницы": self._pages
         }
    
    def write_book(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
    


book = Book("Война и мир", "Лев Толстой", 1225)
print(book.read_book())  