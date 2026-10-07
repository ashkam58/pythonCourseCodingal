# M8L4A2: Library Management System
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 4 Activity 2

class Library:
    def __init__(self, library_name, books_list):
        self.library_name = library_name
        self.available_books = books_list
        self.borrowed_books = {}

    def display_available_books(self):
        print(f"\n--- Available Books in {self.library_name} ---")
        for i, book in enumerate(self.available_books, 1):
            print(f"{i}. {book}")

    def lend_book(self, student_name, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books[book_name] = student_name
            print(f"[OK] '{book_name}' has been successfully lent to {student_name}.")
        elif book_name in self.borrowed_books:
            print(f"[!] '{book_name}' is currently issued to {self.borrowed_books[book_name]}.")
        else:
            print(f"[!] '{book_name}' is not in the library database.")

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            del self.borrowed_books[book_name]
            self.available_books.append(book_name)
            print(f"[OK] '{book_name}' returned successfully. Thank you!")
        else:
            print(f"[!] '{book_name}' was not borrowed from this library.")

if __name__ == "__main__":
    my_lib = Library("Codingal Central Library", ["Python Crash Course", "Clean Code", "Artificial Intelligence: A Modern Approach", "Design Patterns"])
    my_lib.display_available_books()
    my_lib.lend_book("Ashkam", "Python Crash Course")
    my_lib.display_available_books()
    my_lib.return_book("Python Crash Course")
