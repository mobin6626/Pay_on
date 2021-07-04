from tkinter import *
from manager_sign_in import *


test = Tk()
test.title("pay on(fucking test)")
test.geometry("1100x500")
test.resizable(False,False)
color = "black"
color_1 = "#006eff"
test.configure(bg=color_1)

def fuckingFuck():
    test.quit()
    return manager_information


bTest = Button(manager_information,  text="برگشت", font=("b koodak", 12), width=13, height=2,
                background=color, foreground="white", highlightbackground=color, command=back_to_main)