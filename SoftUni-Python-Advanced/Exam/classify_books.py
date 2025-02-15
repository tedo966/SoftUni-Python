def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_books = {}
    for genre, title in args:
        if genre == "fiction":
            for isbn, isbn_title in kwargs.items():
                if isbn_title == title:
                    fiction_books[isbn] = title
        elif genre == "non_fiction":
            for isbn, isbn_title in kwargs.items():
                if isbn_title == title:
                    non_fiction_books[isbn] = title
    sorted_fiction_books = {k: fiction_books[k] for k in sorted(fiction_books)}
    sorted_non_fiction_books = {k: non_fiction_books[k] for k in sorted(non_fiction_books, reverse=True)}

    fiction_output = "Fiction Books:\n" + "\n".join(
        f"~~~{isbn}#{title}" for isbn, title in sorted_fiction_books.items())
    non_fiction_output = "Non-Fiction Books:\n" + "\n".join(f"***{isbn}#{title}" for isbn, title in sorted_non_fiction_books.items())
    if sorted_fiction_books and sorted_non_fiction_books:
        return fiction_output + "\n" + non_fiction_output
    elif sorted_fiction_books:
        return fiction_output
    else:
        return non_fiction_output

# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("non_fiction", "The Art of War"),
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "The Art of War"),
#     ("fiction", "The Great Gatsby"),
#     ("non_fiction", "A Brief History of Time"),
#     ("fiction", "Brave New World"),
#     FF1234HH="The Great Gatsby",
#     NF3845UU="A Brief History of Time",
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))

# print(classify_books(
#     ("non_fiction", "Sapiens"),
#     ("non_fiction", "Homo Deus"),
#     ("non_fiction", "The Selfish Gene"),
#     NF123ABC="Sapiens",
#     NF987XYZ="Homo Deus",
#     NF456DEF="The Selfish Gene"
# ))
