import pandas
from tkinter import *
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
LANG_LEARN = "Spanish"
LANG_TRANS = "English"
LANG_FONT = ("Ariel", 25, "italic")
WORD_FONT = ("Ariel", 35, "bold")

try:
    raw_db = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    raw_db = pandas.read_csv("Spanish_1000_Freq.csv")
finally:
    db = raw_db.to_dict(orient="records")

timer_id = None
word = None


# ------------------ Save Process --------------------- #
def save_process():
    pandas.DataFrame.from_records(db).to_csv("words_to_learn.csv", index=False)


# --------------- Remove Card from DB ----------------- #
def remove_card_from_pack():
    if word is not None:
        db.remove(word)
        save_process()
    show_new_word()


# ---------------- Single Word Timer ------------------ #
def show_translation():
    card_canvas.itemconfig(card_word_text, text=word[LANG_TRANS], fill="white")
    card_canvas.itemconfig(card_lang_text, text=LANG_TRANS, fill="white")
    card_canvas.itemconfig(card_image_id, image=back_pic)


def show_new_word():
    global word, timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
    word = choice(db)
    timer_id = window.after(3000, show_translation)
    card_canvas.itemconfig(card_word_text, text=word[LANG_LEARN], fill="black")
    card_canvas.itemconfig(card_lang_text, text="Español", fill="black")
    card_canvas.itemconfig(card_image_id, image=front_pic)


# ------------------------ UI ------------------------- #

window = Tk()
window.minsize(800, 500)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=20)

# Pictures
front_pic = PhotoImage(file="images/card_front.png")
back_pic = PhotoImage(file="images/card_back.png")
wrong_logo_pic = PhotoImage(file="images/wrong.png")
right_logo_pic = PhotoImage(file="images/right.png")

# Canvases
card_canvas = Canvas(width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)
card_image_id = card_canvas.create_image(500, 300, image=back_pic)
card_word_text = card_canvas.create_text(500, 300, text="Floopy", font=WORD_FONT)
card_lang_text = card_canvas.create_text(500, 200, text="Lang", font=LANG_FONT)

# Buttons
wrong_button = Button(image=wrong_logo_pic, highlightthickness=0, command=show_new_word)
right_button = Button(image=right_logo_pic, highlightthickness=0, command=remove_card_from_pack)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()
