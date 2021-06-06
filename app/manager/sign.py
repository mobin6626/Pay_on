from tkinter import *
import tkinter.messagebox

mngr = Tk()
mngr.title("pay on(manager)")
mngr.geometry("1100x500")
mngr.resizable(False, False)
color = "black"
color_1 = "#b3f542"
color_2 = "#f5a442"
mngr.configure(bg=color_1)

# =========== Function ===========
def errorMsg(ms):
    if ms == 'username':
        tkinter.messagebox.showerror('نام کاربری نامعتبر','نام کاربری وارد شده نامعتبر است لطفا دوباره تلاش کنید')
    elif ms == 'password':
        tkinter.messagebox.showerror('رمز نامعتبر','رمز وارد شده نادرست است لطفا دوباره امتحان کنید')
    elif ms == 'invalid':
        tkinter.messagebox.showerror('اظلاعات غلط','اطلاعات وارد شده غلط میباشد لطفا دوباره تلاش کنید')


username1 = 'mobin'
password1 = 1234

def login():
    # if username.get() == username1:
    #     try:
    #         password.get() == password1
    #         print('you got damn right')
    #     except:
    #         errorMsg('password')
    # elif password.get() == password1:
    #     try:
    #         username.get() == username1
    #         print('you got damn right')
    #     except:
    #         errorMsg('username')
    # else:
    #     errorMsg('invalid')
    # -----------------------------
    if password.get() == password1 or username.get() == username1:
        print('you god damn right')
    else:
        errorMsg('invalid')


# =========== Labels ===========
sign_label = Label(mngr, text='ورود به منوی مدیریت', font=('b koodak', 16), bg=color_1, foreground=color_2)
sign_label.pack(side=TOP,pady=20)

user_label = Label(mngr, text='نام کاربری', font=('b koodak', 11), bg=color_1, foreground=color_2)
user_label.pack(side=TOP)


# =========== Variables ===========
username_var = StringVar()
password_var = IntVar()


# =========== Entry ===========
username = Entry(mngr,width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                  highlightbackground=color_2, textvariable=username_var)
username.pack(side=TOP, pady=20)

pass_label = Label(mngr, text='رمز عبور', font=('b koodak', 11), bg=color_1, foreground=color_2)
pass_label.pack(side=TOP)

password = Entry(mngr, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                  highlightbackground=color_2, textvariable=password_var)
password.pack(side=TOP, pady=20)



# =========== Button ===========
log_in = Button(mngr, text="ورود", font=("b koodak", 14), width=11, height=1, bg=color_2, foreground=color_1,
                  highlightbackground=color_2, command=login)
log_in.pack(side=TOP, pady=20)



mainloop()