from tkinter import *
from html import unescape
from quiz_brain import QuizBrain

BACKGROUND_COLOR = "#04293A"
NORMAL_COLOR = "white"
RIGHT_COLOR = "#379237"
WRONG_COLOR = "#950101"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=BACKGROUND_COLOR)
        self.after_id = None

        # Label
        self.score_lbl = Label(text="Score: 0", bg=BACKGROUND_COLOR, fg=NORMAL_COLOR, font=("Courier", 12, "bold"))
        self.score_lbl.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=300, highlightthickness=0, background=NORMAL_COLOR)
        self.text_id = self.canvas.create_text(150, 150, width=250, text=unescape(quiz.next_question()),
                                               font=("Ariel", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # Images
        check_img = PhotoImage(file="Images/check.png")
        ex_img = PhotoImage(file="Images/x.png")

        # Buttons
        self.right = Button(
            image=check_img,
            bg=BACKGROUND_COLOR,
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0,
            command=self.click_right,

        )
        self.right.grid(row=2, column=0)
        self.wrong = Button(
            image=ex_img,
            bg=BACKGROUND_COLOR,
            activebackground=BACKGROUND_COLOR,
            highlightthickness=0,
            command=self.click_wrong
        )
        self.wrong.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.config(background=NORMAL_COLOR)
            self.canvas.itemconfig(self.text_id, text=unescape(next_question))
            self.after_id = None
        else:
            self.window.quit()

    def click_right(self):
        self.give_feedback("True")

    def click_wrong(self):
        self.give_feedback("False")

    def give_feedback(self, answer):
        if self.after_id is None:
            if self.quiz.check_answer(answer):
                background = RIGHT_COLOR
            else:
                background = WRONG_COLOR
            self.canvas.config(background=background)
            self.score_lbl.config(text=self.quiz.score_string())
            self.after_id = self.window.after(1000, self.get_next_question)
