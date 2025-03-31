import os
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog

os.makedirs('notes', exist_ok=True)

root = ctk.CTk()
root.title("Notes App")

root.geometry("500x600")
root.resizable(False, False)

def save():
    if title.get() == "":
        title.insert(0, "Untitled")
    with open(os.path.join("notes", title.get() + ".txt"), "w") as f:
        f.write(noteInsert.get("1.0", tk.END))

def load():
    fs = filedialog.askopenfilename().split("/")[-1]
    with open(os.path.join("notes", fs), "r") as f:
        noteInsert.delete("1.0", tk.END)
        noteInsert.insert(tk.END, f.read())
        title.delete(0, tk.END)
        if fs.split(".")[0] != "": title.insert(0, fs.split(".")[0])

def clear():
    noteInsert.delete("1.0", tk.END)

def close():
    save()
    root.destroy()

def new():
    noteInsert.delete("1.0", tk.END)
    title.delete(0, tk.END)

title = ctk.CTkEntry(root, width=400)
title.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

noteInsert = ctk.CTkTextbox(root, width=400, height=300)
noteInsert.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

fg_color = "#A9A9A9"
hover_color = "#808080"
text_color = "white"

newButton = ctk.CTkButton(root, text="New", command=new, fg_color=fg_color, text_color=text_color, hover_color=hover_color, height=50)
saveButton = ctk.CTkButton(root, text="Save", command=save, fg_color=fg_color, text_color=text_color, hover_color=hover_color)
openButton = ctk.CTkButton(root, text="Open", command=load, fg_color=fg_color, text_color=text_color, hover_color=hover_color)
clearButton = ctk.CTkButton(root, text="Clear", command=clear, fg_color=fg_color, text_color=text_color, hover_color=hover_color)
closeButton = ctk.CTkButton(root, text="Close", command=close, fg_color=fg_color, text_color=text_color, hover_color=hover_color)

newButton.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
saveButton.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
openButton.grid(row=3, column=1, padx=20, pady=5, sticky="ew")
clearButton.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
closeButton.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
