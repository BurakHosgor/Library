class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        for line in self.file.readlines():
            book_data = line.strip().split(",")
            print(f"Book: {book_data[0]}, Author: {book_data[1]}")


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        pages = input("Enter number of pages: ")
        self.file.write(f"{title},{author},{release_date},{pages}\n")
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        lines = self.file.readlines()
        self.file.seek(0)
        for line in lines:
            if not title in line:
                self.file.write(line)
        self.file.truncate()
        print(f"Book '{title}' removed successfully.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
