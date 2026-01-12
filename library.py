# Simple Library Management System

library = []

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!")

def view_books():
    if len(library) == 0:
        print("No books in library.")
    else:
        print("Books in Library:")
        for i in range(len(library)):
            print(i + 1, ".", library[i])

def issue_book():
    view_books()
    if len(library) == 0:
        return
    choice = int(input("Enter book number to issue: "))
    if choice > 0 and choice <= len(library):
        print(library[choice - 1], "has been issued.")
        library.pop(choice - 1)
    else:
        print("Invalid choice")

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Exit")

while True:
    menu()
    ch = input("Enter your choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        view_books()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        print("Thank you for using Library System")
        break
    else:
        print("Invalid choice")
