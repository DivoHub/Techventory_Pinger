import tkinter as tk


class GUI:
    def __init__(self):
        self.root = tk.TK()
        self.entry1 = tk.Entry(self)

root = tk.Tk()
root.geometry("600x600")
root.title("Techping")

heading = tk.Label(root, text="Techping", font=('Courier New', 16))
heading.pack(pady=10)

root.mainloop()