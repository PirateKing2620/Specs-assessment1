### Step 1 - Input function
## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
# Code here

fav_book = input("What is your favorite book? ")

# def create_new_book():
#     title = input("What is the title of the book? ")
#     author = input("Who is the author of the book? ")
#     year = input("What year was this book published? ")
#     rating = input("What rating out of 5 would you give this book? ")
#     pages = input("What is the page count of the book? ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#     title = input("What is the title of the book? ")
#     author = input("Who is the author of the book? ")
#     year = int(input("What year was this book published? "))
#     rating = float(input("What rating out of 5 would you give this book? "))
#     pages = int(input("What is the page count of the book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
    title = input("What is the title of the book? ")
    author = input("Who is the author of the book? ")
    try:
        year = int(input("What year was this book published? "))
    except:
        year = int(input("What year was this book published? "))  
    try:
        rating = float(input("What rating out of 5 would you give this book? "))
    except:
        rating = float(input("What rating out of 5 would you give this book? "))
    try:
        pages = int(input("What is the page count of the book? "))
    except:
        pages = int(input("What is the page count of the book? "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu(books_source):
    choice = input("\nPress 1 to add a book.\nPress 2 to exit." )
    if choice == "1":
        books_source.append(create_new_book())
    elif choice == "2":
         print("\nShutting down")
    else:
        print("\nSorry please press 1 or 2.\n")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu(books_source):
    active = True
    while active:
        choice = input("\nPress 1 to add a book.\nPress 2 to exit." )
        if choice == "1":
            books_source.append(create_new_book())
        elif choice == "2":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please press 1 or 2.\n")