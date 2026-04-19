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

# ================= HEADER =================
header = tk.Label(
    window,
    text="🔐 BOOK CIPHER",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
header.pack(pady=15)


# ================= INPUT =================
input_label = tk.Label(
    window,
    text="Shkruaj mesazhin ose kodin:",
    font=("Arial", 12),
    bg="#0f172a",
    fg="white"
)
input_label.pack()


input_box = tk.Text(window, height=5, width=60, font=("Arial", 11))
input_box.pack(pady=10)

result_label = tk.Label(
    window,
    text="📦 REZULTATI",
    font=("Arial", 12, "bold"),
    bg="#0f172a",
    fg="white"
)
result_label.pack()


result_box = tk.Text(window, height=8, width=60, font=("Arial", 11))
result_box.pack(pady=10)


# ==== e====
def do_encrypt():
    msg = input_box.get("1.0", tk.END).strip()


    if msg.startswith("[") and msg.endswith("]"):
        result_box.insert(tk.END, "❌ Error: format i gabuar!\n\n")
        return

    result = encrypt(msg.lower(), book_index)


    clean = []
    for x in result:
        clean.append(str(x))

    result_box.insert(tk.END, f"Encrypted:\n{' '.join(clean)}\n\n")

# ==== de====
def do_decrypt():
    try:
        raw = input_box.get("1.0", tk.END).strip()

     
        raw = raw.replace("\n", "")

        data = ast.literal_eval(raw)

        result = decrypt(data, lines)

        result_box.insert(tk.END, f"Decrypted:\n{result}\n\n")

    except:
        result_box.insert(tk.END, "❌ Error: format i gabuar!\n\n")


# ====== btn====
btn_frame = tk.Frame(window, bg="#0f172a")
btn_frame.pack(pady=10)


encrypt_btn = tk.Button(
    btn_frame,
    text="🔐 ENCRYPT",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="white",
    width=15,
    command=do_encrypt
)
encrypt_btn.grid(row=0, column=0, padx=10)


decrypt_btn = tk.Button(
    btn_frame,
    text="🔓 DECRYPT",
    font=("Arial", 12, "bold"),
    bg="#ef4444",
    fg="white",
    width=15,
    command=do_decrypt
)
decrypt_btn.grid(row=0, column=1, padx=10)


# ====== footer===
footer = tk.Label(
    window,
    text="Cryptography Project - Book Cipher",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#64748b"
)
footer.pack(pady=10)


window.mainloop()



