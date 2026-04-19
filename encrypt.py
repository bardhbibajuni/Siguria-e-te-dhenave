
def encrypt(message, book_index):
    words = message.strip().lower().split()

    encrypted = []

    for word in words:
        if word in book_index and len(book_index[word]) > 0:
            # gjithmone merr te paren
            encrypted.append(book_index[word][0])
        else:
            encrypted.append("NOT FOUND")

    return encrypted
