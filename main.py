from core import Book, Library

def main():
    lib = Library()
    b1 = Book("Python 101", "John Doe", 300)
    lib.add_book(b1)

    for book in lib:
        print(book)

if __name__ == "__main__":
    main()
