from tkinter import *
from time import strftime
from datetime import date, time, timezone
import user_sign_in
import manager_sign_in
import tkinter.messagebox
import os

root = Tk()
root.title("pay on")
root.geometry("1100x500")
root.resizable(False, False)
color = "black"
color_1 = "#006eff"
root.configure(bg=color_1)

# manager = manager_sign_in
# user = user_sign_in
# ============= functions =============
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('دوباره امتحان کنید', 'مشکلی پیش آمده لطفا دوباره امتحان کنید')


def user_sign():
    root.destroy()
    open(user_sign_in.user)


def manager_sign():
    root.destroy()
    open(manager_sign_in.manager_information)


# ============= time ============
d = date.today()

day_label = Label(root, text=d, font=("b koodak", 14), background=color_1, foreground=color,
                  width=18, height=2)
day_label.pack(side=TOP, pady=100)

# day_label = Label(root, font=("arial", 10), background="black", foreground="white",
#                    width=18, height=2)
# day_label.place(x=200, y=120)

# ============= Button =============
b_user = Button(root, text="ورود کاربر", font=("b koodak", 12), width=16, height=2,
                background=color, foreground="white",
                highlightbackground=color, command=user_sign)
b_user.place(x=467, y=200)

b_manager = Button(root, text="ورود مدیر", font=("b koodak", 12), width=16
                   , height=2, background="black", foreground="white", highlightbackground=color,
                   command=manager_sign)
b_manager.place(x=467, y=300)

b_quit = Button(root, text="خارج", font=("b koodak", 12), width=16
                , height=2, background="black", foreground="white", highlightbackground=color,
                command=root.destroy)
b_quit.place(x=467, y=400)

# ============= Labels =============
welcome = Label(root, text="به منوی اپ خوش آمدید", font=("b koodak", 16),
                bg=color_1, foreground=color)
welcome.place(x=467, y=10)

root.mainloop()
