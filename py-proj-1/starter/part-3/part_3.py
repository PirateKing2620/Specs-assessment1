my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.
# Code below

def bookfunc():
    pass

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.
# Code below

def book_parser(book_dictionary):
    book_string = f"This book is written by Suzanne Collins in 2008."
    return book_string

print(book_parser(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_rating(book_dictionary):
    rating = book_dictionary['rating']
    return rating

def book_author(book_dictionary):
    author = book_dictionary['author']
    return author

def book_pages(book_dictionary):
    pages = book_dictionary['pages']
    return pages