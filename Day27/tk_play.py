import tkinter


def button_clicked():
    entered = input_.get()
    label.config(text=entered)
    input_.delete(0, len(entered))


window = tkinter.Tk()
window.title("Miles to KM Calculator")
window.minsize(width=350, height=250)
window.config(padx=50, pady=50)

# Labels
label = tkinter.Label(text="LABEL", font=("Ariel", 18, "bold"))
# label.pack()
# label.place(100, 100)
label.grid(column=0, row=0)
label.config(padx=10, pady=10)
# label["text"] = "New Text"
label.config(text="New Text")

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input_ = tkinter.Entry(width=10)
input_.grid(column=3, row=2)
# input_.pack()

window.mainloop()
