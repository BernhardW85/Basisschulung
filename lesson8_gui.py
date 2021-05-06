import tkinter
import random
from tkinter import messagebox

secret = random.randint(1,20)
window = tkinter.Tk()

hello_label = tkinter.Label(window, text="Guess the number?!")
hello_label.pack()
guess = tkinter.Entry(window)
guess.pack()

def button_click():
    if int(guess.get()) == secret:
        result_text = "You WON"
    elif int(guess.get()) > secret:
        result_text = "Wrong - the number is too high."
    else:
        result_text = "Wrong - the number is too low"
    messagebox.showinfo("Result", result_text)

submit = tkinter.Button(window, text="Submit", command=button_click)
submit.pack()

window.mainloop()
