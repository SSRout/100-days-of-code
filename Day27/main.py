from tkinter import *


def miles_to_km():
    miles=float(miles_input.get())
    km=round(miles*1.609)
    km_result.config(text=f"{km}")

window=Tk()
window.title("Mile To Km")
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_lable=Label(text=" Miles")
miles_lable.grid(column=2,row=0)

is_equal_lable=Label(text=" is equal to")
is_equal_lable.grid(column=0,row=1)

km_result=Label(text="0")
km_result.grid(column=1,row=1)

km_lable=Label(text="Km")
km_lable.grid(column=2,row=1)

calculate=Button(text="Calculate",command=miles_to_km)
calculate.grid(column=1,row=2)

window.mainloop()