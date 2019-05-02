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
    root.geometry('{}x{}+{}+{}'.format(610, 400, position_y, position_x))
    ttk.Style().configure("TLabel", padding=12, relief="flat",
                          wraplength=600)
    text1 = ttk.Label(root, font=('Arial 20 bold'), text= word)
    text2 = ttk.Label(root, font=('Arial 12'), text= description)
    text1.pack()
    text2.pack()
    root.after(8000, lambda: root.destroy())
    root.mainloop()

sleep_sec = random.randint(20, 25)
position_x = random.randint(50, 700)
position_y = random.randint(50, 1200)



if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "dictionary.json")
    for i in range(1):
        # time.sleep(sleep_sec)
        main()
