# Nathan John
# Importing data from tkinter


from tkinter import *

# Creating and designing the interface


temp_converter = Tk()
temp_converter.title("Temperature converter")
temp_converter.config(bg="#202020")
temp_converter.geometry("800x500")
temp_converter.resizable(False, False)

# Continuous design of the interface


# Frame 1


frame = Frame(temp_converter, width=300, height=200, highlightbackground="black", highlightthickness=1, bg="grey")
frame.place(x=50, y=51)
celsius_header = Label(frame, text="Celsius to Fahrenheit", bg="blue")
celsius_header.place(x=60, y=0)
celsius_entry = Entry(frame, state="readonly")
celsius_entry.place(x=60, y=150)

# Frame 2


frame_2 = Frame(temp_converter, width=300, height=200, highlightbackground="black", highlightthickness=1, bg="grey")
frame_2.place(x=380, y=51)
fahrenheit_header = Label(frame_2, text="Fahrenheit to Celsius", bg="blue")
fahrenheit_header.place(x=60, y=0)
fahrenheit_entry = Entry(frame_2, state="readonly")
fahrenheit_entry.place(x=60, y=150)


# Activation of Degrees Celsius


def activate_celsius():
    celsius_entry.config(state="normal")
    fahrenheit_entry.config(state="readonly")
    frame.config(bg="white")
    frame_2.config(bg="grey")
    return


# Degrees Celsius button


Celsius_button = Button(temp_converter, text="Activate - Celsius to Fahrenheit", command=activate_celsius)
Celsius_button.place(x=80, y=280)


# Activation of Degrees Fahrenheit


def activate_fahrenheit():
    fahrenheit_entry.config(state="normal")
    celsius_entry.config(state="readonly")
    frame.config(bg="grey")
    frame_2.config(bg="white")

    return


# Degrees Fahrenheit button


Fahrenheit_button = Button(temp_converter, text="Activate - Fahrenheit to Celsius", command=activate_fahrenheit)
Fahrenheit_button.place(x=420, y=280)


# Using if statements to convert between the Degrees


def convert():
    if fahrenheit_entry.get() == "":
        celsius = float(celsius_entry.get())
        celsius_convert = (celsius * (9 / 5) + 32)
        Conversion_answer.config(text=round(celsius_convert))
    elif celsius_entry.get() == "":
        fahrenheit = float(fahrenheit_entry.get())
        fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9
        Conversion_answer.config(text=round(fahrenheit_to_celsius))


# The Conversion button


Conversion = Button(temp_converter, text="Calculate conversion", command=convert)
Conversion.place(x=90, y=400)
Conversion_answer = Label(temp_converter, width=20, height=2, bg="white")
Conversion_answer.place(x=300, y=400)

# Defining the delete functions


def delete():
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    Conversion_answer.config(text="")

# Defining the kill function


def kill():
    temp_converter.destroy()


# Exit button as well as the clear button


clear = Button(temp_converter, text="Clear", width=15, command=delete)
clear.place(x=500, y=400)
Exit = Button(temp_converter, text="exit", width=15, command=kill)
Exit.place(x=500, y=440)

# Now run the program


temp_converter.mainloop()
