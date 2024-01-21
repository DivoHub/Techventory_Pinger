import tkinter as tk
from other_file import get_string  # Importing the function from the other file

# Create the main window
root = tk.Tk()
root.title("Techping")

# Set the geometry of the window
root.geometry("600x300")  # Increased width to accommodate the log

# Create a header label
header = tk.Label(root, text="Techping", font=("Arial", 24))
header.grid(row=0, column=0, columnspan=2)  # Span across both columns

# Names of the stores
stores = ["Amazon", "Canada Computers", "Memory Express", "Best Buy", "Vuugo", "Newegg"]

# Function to create rows with store names
def create_row(text, row):
    label = tk.Label(root, text=text, font=("Arial", 16))
    label.grid(row=row, column=0, sticky="w")  # Align to the west (left)

# Create rows for each store
for i, store in enumerate(stores, start=1):
    create_row(store, i)

# Retrieve the string from the other file and display it in a Label
log_text = get_string()
log_label = tk.Label(root, text=log_text, font=("Arial", 16), justify=tk.LEFT)
log_label.grid(row=1, column=1, rowspan=6, sticky="nsew")  # Align to fill the cell

# Configure grid row/column weights
root.grid_rowconfigure(1, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)