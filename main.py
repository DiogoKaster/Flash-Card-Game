from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as r

# ----------------- CONSTANTS ---------------------
BACKGROUND_COLOR = "#B1DDC6"
score = 0

# -------------- READING CSV FILE -----------------

data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")


# ----------------- FUNCTIONS ---------------------


def right_ans():
    global score
    score += 1
    create_cards()


def wrong_ans():
    global score
    if score == 0:
        pass
    else:
        score -= 1
    create_cards()


def flip_card():
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(canvas_txt, text="French", fill=BACKGROUND_COLOR)
    canvas.itemconfig(canvas_ask, text=guessing['French'], fill=BACKGROUND_COLOR)


def create_cards():
    global guessing
    guessing = r.choice(data_dict)
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(canvas_txt, text="English", fill="white")
    canvas.itemconfig(canvas_ask, text=guessing['English'], fill="white")
    window.after(3000, func=flip_card)


# --------------- CREATING THE UI -----------------
# HIGH SCORE MESSAGE BOX
with open("score.txt", "r") as file:
    content = file.read()
    messagebox.showinfo(title="High Score", message=f"Your higher score was {content}")
# MAIN WINDOW

window = Tk()
window.title("Flash Card")
window.config(pady=100, padx=50, bg=BACKGROUND_COLOR)

# CANVAS & IMAGE

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")

guessing = r.choice(data_dict)

canvas_img = canvas.create_image(400, 263, image=card_back)
canvas_txt = canvas.create_text(400, 200, text="English", fill="white", font=("Courier", 30, "bold"))
canvas_ask = canvas.create_text(400, 300, text=guessing['English'], fill="white", font=("Courier", 30))
canvas.grid(column=1, row=0)

window.after(3000, func=flip_card)

# BUTTONS

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_ans)
right_button.grid(column=2, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_ans)
wrong_button.grid(column=0, row=1)

window.mainloop()

with open("score.txt", "w") as file:
    file.write(f"{score}")
