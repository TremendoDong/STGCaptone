# TremendoDong_u3249826_ST1Assignment2_Week7[a]GUI

import tkinter as tk
from tkinter import simpledialog, messagebox


def save_words():
    num_words = simpledialog.askinteger("Input", "How many words would you like to write to the file?")
    words = []
    for i in range(num_words):
        word = simpledialog.askstring("Input", f"Enter word {i + 1}:")
        words.append(word)

    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
    messagebox.showinfo("Success", "Words saved successfully!")


root = tk.Tk()
root.title('Word Writer')

btn_save = tk.Button(root, text="Enter Words", command=save_words)
btn_save.pack(pady=20)

root.mainloop()
