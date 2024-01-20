import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Techping")

# Set the geometry of the window (width x height)
root.geometry("400x300")

# Create a header label
header = tk.Label(root, text="Techping", font=("Arial", 24))
header.pack()

# Names of the stores to display
stores = ["Amazon", "Canada Computers", "Memory Express", "Best Buy", "Vuugo", "Newegg"]

# Function to create rows with store names
def create_row(text):
    label = tk.Label(root, text=text, font=("Arial", 16))
    label.pack(expand=True)

# Create rows for each store
for store in stores:
    create_row(store)

# Start the GUI event loop
root.mainloop()