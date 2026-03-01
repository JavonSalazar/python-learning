# Homework 4
# Name: Javon Salazar
# Date: 2/27/26
#Description: This code goes over Creating classes and objects, Using encapsulation to protect data, Building inheritance hierarchies 

# Problem 1: Libary Book System
class Book:
    def __init__(self, title, author, total_pages, isbn):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.isbn = isbn
        self._current_page = 0  

    @property
    def current_page(self):
        return self._current_page

    @property
    def progress(self):
        percentage = (self._current_page / self.total_pages) * 100
        return f"{percentage:.1f}%"

    def read(self, pages):
        if pages <= 0:
            print("Error: pages must be positive")
            return self._current_page

        self._current_page += pages

        if self._current_page > self.total_pages:
            self._current_page = self.total_pages

        return self._current_page

    def reset(self):
        self._current_page = 0

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Page {self._current_page}/{self.total_pages}"


class TextBook(Book):
    def __init__(self, title, author, total_pages, isbn, subject, edition):
        super().__init__(title, author, total_pages, isbn)
        self.subject = subject
        self.edition = edition
        self._highlights = {}  

    def highlight(self, page, text):
        if page < 1 or page > self.total_pages:
            print("Error: page number out of range")
            return

        if page not in self._highlights:
            self._highlights[page] = []

        self._highlights[page].append(text)

    def get_highlights(self, page):
        return self._highlights.get(page, [])

    def __str__(self):
        return f"'{self.title}' by {self.author} (Edition {self.edition}, {self.subject}) - Page {self.current_page}/{self.total_pages}"


# Testing my code
if __name__ == "__main__":
    
    print("=== Book Tests ===")
    novel = Book("1984", "George Orwell", 328, "978-0451524935")
    print(novel)

    novel.read(50)
    print(f"Current page: {novel.current_page}")
    print(f"Progress: {novel.progress}")

    novel.read(-10)  

    novel.read(400)  
    print(f"Current page: {novel.current_page}")
    print(f"Progress: {novel.progress}")

    novel.reset()
    print(f"After reset: page {novel.current_page}")

    print("\n=== TextBook Tests ===")

    cs_book = TextBook("Intro to Python", "Deitel", 880, "978-0135404676",
                       "Computer Science", 1)
    print(cs_book)

    cs_book.read(120)
    print(f"Progress: {cs_book.progress}")

    cs_book.highlight(45, "Dictionaries store key-value pairs")
    cs_book.highlight(45, "Keys must be immutable")
    cs_book.highlight(72, "Sets cannot contain duplicates")
    cs_book.highlight(0, "Important note")  

    print(f"Page 45 highlights: {cs_book.get_highlights(45)}")
    print(f"Page 72 highlights: {cs_book.get_highlights(72)}")
    print(f"Page 1 highlights: {cs_book.get_highlights(1)}")
