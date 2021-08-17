import tkinter as tk
from typing import Text

## behavior
def onClick():
    global text_field
    print(text_field.get())

window = tk.Tk()

btn = tk.Button(window, text= "Click me!", command= onClick)
btn.pack()

## create text field
text_field = tk.Entry(window, text = "...")
text_field.pack()


window.mainloop()