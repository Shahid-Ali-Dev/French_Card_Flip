import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
learn = data.to_dict(orient="records")
dictionary = {}
def french():
     global timer,dictionary
     canvas.after_cancel(timer)
     dictionary = random.choice(learn)
     canvas.itemconfig(t, text="French",fill= "black")
     canvas.itemconfig(w, text=dictionary["French"],fill= "black")
     canvas.itemconfig(im, image= background_white)
     timer = canvas.after(3000,func=english)

def english():
    if dictionary != {}:
        eng = dictionary["English"]
        canvas.itemconfig(t, text="English",fill= "white")
        canvas.itemconfig(w, text=eng,fill= "white")
        canvas.itemconfig(im, image= bg_green)

def is_known():
    learn.remove(dictionary)
    new = pandas.DataFrame(learn)
    new.to_csv("./data/words_to_learn.csv",index=False)
    french()

tk = Tk()
tk.title("Flashy")
tk.config(bg=BACKGROUND_COLOR, pady=30,padx=30)
background_white = PhotoImage(file=r"C:\Users\HP\Desktop\python\Day 31\images\card_front.png")
bg_green = PhotoImage(file= "./images/card_back.png")
r = PhotoImage(file="./images/right.png")
wr = PhotoImage(file="./images/wrong.png")
canvas = Canvas(bg=BACKGROUND_COLOR,width=800,height=526,highlightthickness=0)
timer = canvas.after(3000, func=english)
im = canvas.create_image(405,270,image= background_white)
t = canvas.create_text(400,150,text= "",font=("Ariel",25,"italic"))
w = canvas.create_text(400,250,text= "",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=3,pady=15)

right = Button(image=r,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
right.grid(row=1,column=2)

wrong = Button(image=wr,highlightthickness=0,bg=BACKGROUND_COLOR,command=french)
wrong.grid(row=1,column=0)

french()
tk.mainloop()