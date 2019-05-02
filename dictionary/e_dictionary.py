import os
import json
import random
import time
import tkinter as tk
from tkinter import ttk
from pygame import mixer
from gtts import gTTS


def main():
    def speech():
        mixer.init()
        try:
            tts=gTTS(text=word, lang='en')
            tts.save('1.mp3')
            mixer.music.load('1.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.03)
            mixer.music.stop()
            
        except Exception:
            pass



    words = json.load(open(filename))
    word, description = random.choice(list(words.items()))
    description = '\n\n- '.join(description)
    print(word, description)

    root = tk.Tk()
    root.title("Dictionary")

    root.geometry('{}x{}+{}+{}'.format(400, 200, position_y, position_x))
    ttk.Style().configure("TLabel", padding=12, relief="flat",
                          wraplength=450)
    text1 = ttk.Label(root, font=('Arial 20 bold'), text= word)
    text2 = ttk.Label(root, font=('Arial 12'), text= description)

    text1.pack(expand=1, anchor='center')
    text2.pack(expand=1, anchor='center')

    root.after(1000, lambda: speech())
    root.after(8000, lambda: root.destroy())

    root.mainloop()


sleep_sec = random.randint(20, 500)
position_x = random.randint(50, 700)
position_y = random.randint(50, 1200)



if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    # filename = os.path.join(dirname, "dictionary.json")
    filename = os.path.join(dirname, "en_ru_dict.json")
    for i in range(1):
        # time.sleep(sleep_sec)
        main()
