import tkinter as tk
from other_file import get_string

root = tk.Tk()
root.title("Techping")
root.geometry("600x300")

header = tk.Label(root, text="Techping", font=("Arial", 24))
header.grid(row=0, column=0, columnspan=2)

stores = ["Amazon", "Canada Computers", "Memory Express", "Best Buy", "Vuugo", "Newegg"]

def create_row(text, row):
    label = tk.Label(root, text=text, font=("Arial", 16))
    label.grid(row=row, column=0, sticky="w")

for i, store in enumerate(stores, start=1):
    create_row(store, i)

log_text = get_string()
log_label = tk.Label(root, text=log_text, font=("Arial", 16), justify=tk.LEFT)
log_label.grid(row=1, column=1, rowspan=6, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

