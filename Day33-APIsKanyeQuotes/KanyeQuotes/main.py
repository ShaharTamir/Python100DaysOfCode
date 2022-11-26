from tkinter import *
import requests


def get_new_quote():
    # https://api.kanye.rest
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    res_quote = response.json()
    canvas.itemconfig(quote_id, text=f"{res_quote['quote']}")


# Window
window = Tk()
window.minsize(width=500, height=800)
window.title("Kanye Says...")
window.config(padx=50, pady=20, background="white")

# Images
quote_background = PhotoImage(file="images/background.png")
kanye_img = PhotoImage(file="images/kanye.png")

# Canvas
canvas = Canvas(width=400, height=600, bg="white", highlightthickness=0)
quote_background_id = canvas.create_image(200, 300, image=quote_background)
quote_id = canvas.create_text(200, 300, text="Kanye", width=200, font=("Courier", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Button
new_quote = Button(image=kanye_img, highlightthickness=0, bg="white", command=get_new_quote)
new_quote.grid(row=1, column=0)

window.mainloop()
