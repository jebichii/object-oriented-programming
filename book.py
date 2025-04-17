# Base Class
class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def display_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPrice: Ksh{self.price:.2f}"

    def read(self):
        return f"You start reading '{self.title}' by {self.author}."

# Inherited Class
class Ebook(Book):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.file_size = file_size  # File size in MB

    def display_details(self):
        return (
            super().display_details()
            + f"\nFile Size: {self.file_size}MB (Digital Format)"
        )

    def read(self):
        return f"You open the ebook '{self.title}' on your device."

# Testing the classes
paper1 = Book("Kifo Kisimani", "Ken Walibora","1984", 150)
digital = Ebook("When the sun goes down", "Dan Brown", "Fantasy", 890, 5)

print(paper1.display_details())
print(paper1.read())
print(digital.display_details())
print(digital.read())
