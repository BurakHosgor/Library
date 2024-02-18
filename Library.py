class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        for line in self.file.readlines():
            book_data = line.strip().split(",")
            author = book_data[1]
            print(f"Book: {book_data[0]}, Author: {author}")


    def add_book(self):
        title = input("Enter book title: ")
        author_name = input("Enter author's full name (name and surname): ")

        # Check if the author's full name contains a space and the space is not at the end
        if " " not in author_name.strip() or author_name.strip().endswith(" "):
            print("Please enter the author's full name with a space separating name and surname.")
            return

        # Split the author's name and surname
        author_first_name, *author_last_name = author_name.strip().split(" ")

        release_date = input("Enter release date: ")
        pages = input("Enter number of pages: ")

        # Check if the book already exists in the library
        self.file.seek(0)
        for line in self.file.readlines():
            if f"{title},{author_first_name}{' ' if author_last_name else ''}{' '.join(author_last_name)}" in line:
                print("This book is already in the library.")
                return

        self.file.write(f"{title},{author_first_name}{' ' if author_last_name else ''}{' '.join(author_last_name)},{release_date},{pages}\n")
        print("Book added successfully.")

      

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")

        # Get all books with the given title
        self.file.seek(0)
        lines = self.file.readlines()
        books_with_title = []
        for line in lines:
            book_data = line.strip().split(",")
            book_title = book_data[0]
            book_author = book_data[1] if len(book_data) > 2 else ""
            if book_title == title:
                books_with_title.append(book_author)

        if not books_with_title:
            print(f"No book found with title '{title}' in the library.")
            return

        if len(books_with_title) == 1:
            author_name = books_with_title[0]
        else:
            print(f"Multiple books found with title '{title}'. Please select the author to specify which book to remove:")
            for i, author in enumerate(books_with_title, start=1):
                print(f"{i}) {author}")
            choice = input("Enter the number corresponding to the author: ")
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(books_with_title):
                    author_name = books_with_title[choice_index]
                else:
                    print("Invalid choice. Please enter a valid number.")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

        self.file.seek(0)
        with open("books.txt", "w") as file:
            removed = False
            for line in lines:
                book_data = line.strip().split(",")
                book_title = book_data[0]
                book_author = book_data[1] if len(book_data) > 2 else ""
                if book_title == title and book_author == author_name:
                    removed = True
                    print(f"Book '{title}' by {author_name} removed successfully.")
                else:
                    file.write(line)
            if not removed:
                print(f"Book '{title}' by {author_name} is not in the library.")

        self.file = open("books.txt", "a+")





lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the application...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
