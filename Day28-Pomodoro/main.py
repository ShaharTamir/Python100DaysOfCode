from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
SEC_IN_MIN = 60
CHECK = "✓"
timer_id = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def restart_timer():
    global reps
    reps = 0
    canvas.itemconfig(text_id, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check.config(text="")
    if timer_id is not None:
        window.after_cancel(timer_id)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def add_check():
    new_check_string = ""
    for _ in range(math.floor(reps / 2)):
        new_check_string += CHECK
    check.config(text=new_check_string)


def start_timer():
    global reps
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN)
        label.config(fg=RED, text="Break")
    elif reps < 8 and reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(fg=PINK, text="Break")
    elif reps < 8 and reps % 2 == 1:
        count_down(WORK_MIN)
        label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time_left):
    global timer_id

    if time_left < 0:
        start_timer()
        add_check()
        return
    else:
        timer_id = window.after(1000, count_down, time_left - 1)
        time_string = f"{time_left // SEC_IN_MIN:02}:{time_left % SEC_IN_MIN:02}"
        canvas.itemconfig(text_id, text=time_string)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 45, "normal"))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_b = Button(text="Start", highlightthickness=0, background="white",
                 font=("ariel", 12, "normal"), command=start_timer)
start_b.grid(row=2, column=0)

reset_b = Button(text="Reset", highlightthickness=0, background="white",
                 font=("ariel", 12, "normal"), command=restart_timer)
reset_b.grid(row=2, column=2)

check = Label(text="", bg=YELLOW, fg=GREEN, font=("", 20, "bold"))
check.grid(row=3, column=1)

window.mainloop()
