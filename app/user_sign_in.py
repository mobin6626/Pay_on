from tkinter import *
import main
import tkinter.messagebox
import os



user = Tk()
user.title("pay on(user)")
user.geometry("1100x500")
user.resizable(False, False)
color = "black"
color_1 = "#006eff"
user.configure(bg=color_1)


# ======== Functions ========
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('دوباره امتحان کنید','مشکلی پیش آمده لطفا دوباره امتحان کنید')


def back_to_main():
    user.quit()
    open(main.root)



# ======== Button ========
b_back = Button(user,  text="برگشت", font=("b koodak", 12), width=13, height=2,
                background=color, foreground="white", highlightbackground=color, command=back_to_main)
b_back.place(x=0, y=423)

mainloop()