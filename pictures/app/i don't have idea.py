import pyfiglet
from termcolor2 import colored
from tkinter import *

# print(pyfiglet.figlet_format("Fuck  you  All"))

def termcolor():

    global root

    root = Tk()
    root.resizable(False, False)
    root.geometry('400x400')
    root.title("What would you like print?!!")
    color_1 = "black"
    color_2 = "magenta"
    root.configure(bg=color_1)
# ========================
# entry

    message = Entry(root, width=20, text='what would you like print? :', font=('arial', 16))
    message.pack(side=TOP, pady=20, ipady=10)

    color = Entry(root, width=20, text='what color? :', font=('arial', 16))
    color.pack(side=TOP, pady=20, ipady=10)

    result = Entry(root, width=20, font=('arial', 16))
# ========================
# Button
    generate = Button(root, text="Generate", bg=color_2, width=10, height=2,
        command=lambda : print_clr(color,message))
    generate.pack(side=TOP)

    result.pack(side=TOP, pady=15, ipady=30)
# ========================
# Label

    message_var = Label(root, text='what would you like print? :', font=('arial', 8),
        bg=color_2, foreground=color_1)
    message_var.place(x=5, y=0)

    color_var = Label(root, text='what color? :', font=('arial', 8), bg=color_2, foreground=color_1)
    color_var.place(x=5, y=80)

# ========================
# Functions


    valid_color = ["red","green","blue","yellow","magenta","cyan"]

    # message = input("what would you like print? : ")
    # color = input("what color? :")


    def print_clr(color, message):
        if color.get() not in valid_color:
            color.get = "red"
        ascii_clr = pyfiglet.figlet_format(message.get())
        ascii_clr = colored(ascii_clr, color=color.get())
        # print(ascii_clr)
        result.set(ascii_clr)



    # print_clr(color, message)
    mainloop()

termcolor()