from tkinter import *

FONT = ("Ariel", 12, "normal")


def miles_to_km():
    miles = miles_input.get()
    miles_input.delete(0, len(miles))
    miles = float(miles)
    converted_km = 1.609344 * miles
    km_label.config(text=f"{converted_km:.2f}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=100)
window.config(padx=45, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_suffix_label = Label(text="Miles", font=FONT , padx=2)
miles_suffix_label.grid(row=0, column=2)

pre_km_label = Label(text="is equal to", font=FONT, padx=2)
pre_km_label.grid(row=1, column=0)

km_label = Label(text="0", font=FONT)
km_label.grid(row=1, column=1)

km_suffix_label = Label(text="Km", font=FONT, padx=2)
km_suffix_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", font=FONT, command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()
