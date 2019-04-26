import os
import json
import random
import time
import tkinter as tk
from tkinter import ttk
import sys


def main():

    words = json.load(open(filename))
    word, description = random.choice(list(words.items()))
    description = '\n- '+'\n- '.join(description)
    print(word, description)
    root = tk.Tk()
    root.geometry('{}x{}+{}+{}'.format(610, 400, 1200,150))
    ttk.Style().configure("TLabel", padding=12, relief="flat",
                          font=('Arial 12 bold'), wraplength=600)
    text1 = ttk.Label(root, text= word)
    text2 = ttk.Label(root, text= description)
    text1.pack()
    text2.pack()
    root.after(7000, lambda: root.destroy())
    root.mainloop()





if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "dictionary.json")

    main()
