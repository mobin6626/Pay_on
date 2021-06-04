from tkinter import *
import main
import tkinter.messagebox
import os



manager_information = Tk()
manager_information.title("pay on(manager)")
manager_information.geometry("1100x500")
manager_information.resizable(False, False)
color = "black"
color_1 = "#006eff"
manager_information.configure(bg=color_1)



# ============ variables ============
username = StringVar()
password = StringVar()




# ============ Functions ============

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('دوباره امتحان کنید','مشکلی پیش آمده لطفا دوباره امتحان کنید')

def back_to_main():
    manager_information.destroy()
    open(main.root)

def submit():
    if username == 'user':
        print('yes')
    elif password == 'user':
        print('yes')


# ============ Entry ============
b_username = Entry(manager_information,  text="نام کاربری", font=("b koodak", 12),
                    foreground="red")
b_username.place(x=50, y=50)

b_password = Entry(manager_information,  text="رمز ورود", font=("b koodak", 12),
                    foreground="red")
b_password.place(x=170, y=50)


# ============ Button ============
b_submit = Button(manager_information,  text="تائید", font=("b koodak", 12), width=13, height=2,
                background=color, foreground="white", highlightbackground=color, command=submit)
b_submit.place(x=300, y=50)


b_back = Button(manager_information,  text="برگشت", font=("b koodak", 12), width=13, height=2,
                background=color, foreground="white", highlightbackground=color, command=back_to_main)
b_back.place(x=0, y=423)