import pyttsx3
from tkinter import *
from tkinter.ttk import *
from time import strftime
friend = pyttsx3.init()


root = Tk()
root.title('Clock')
root.configure(bg='black')
def time():
    tl = strftime('%I:%M:%S %p')
    label.config(text=tl)
    label.after(1000,time)

label = Label(root,font=('ds-digital',80),background='black', foreground='#2DFC57')

label.pack(anchor='c')

time()


mainloop()
tm = strftime('%I:%M:%S %p')
current_time = f'The current time is {tm}'
friend.say(current_time)
friend.runAndWait()
