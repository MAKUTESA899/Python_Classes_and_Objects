class Book:
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author=author
        self.pages=pages
        Book.total_books +=1

    def description(self):
        return (f"{self.title} by {self.author}, {self.pages} pages")