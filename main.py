
import tkinter as tk
import ast
from encrypt import encrypt
from decrypt import decrypt


# ================= BOOK LOADER =================
def load_book():
    with open("book.txt", "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")
    book_index = {}

    for i, line in enumerate(lines):
        words = line.split()
        for j, word in enumerate(words):
            word = word.lower()
            if word not in book_index:
                book_index[word] = []
            book_index[word].append((i, j))

    return book_index, lines


book_index, lines = load_book()


# ================= WINDOW =================
window = tk.Tk()
window.title("Book Cipher App")
window.geometry("600x550")
window.configure(bg="#0f172a")






