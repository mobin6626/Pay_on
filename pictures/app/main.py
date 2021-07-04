from tkinter import *
from time import strftime
from datetime import date, time, timezone
from app.user.user_sign_in import *
from app.manager.manager_sign_in import *
from app.manager.sign import *
import tkinter.messagebox



def main_screen():

    global root
    global main_screen

    root = Tk()
    root.title("pay on")
    root.geometry("1100x500")
    root.resizable(False, False)
    color = "#f5a442"
    color_1 = "#b3f542"
    root.configure(bg=color_1)


    # ============= functions =============
    def errorMsg(ms):
        if ms == 'error':
            tkinter.messagebox.showerror('دوباره امتحان کنید', 'مشکلی پیش آمده لطفا دوباره امتحان کنید')


    def user_sign():
        root.quit()
        user_screen()



    def manager_sign():
        root.quit()
        mngr_screen()

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
                    background=color, foreground=color_1,
                    highlightbackground=color, command=user_sign)
    b_user.place(x=467, y=200)

    b_manager = Button(root, text="ورود مدیر", font=("b koodak", 12), width=16
                       , height=2, background=color, foreground=color_1, highlightbackground=color,
                       command=manager_sign)
    b_manager.place(x=467, y=300)

    b_quit = Button(root, text="خروج", font=("b koodak", 12), width=16
                    , height=2, background=color, foreground=color_1, highlightbackground=color,
                    command=root.destroy)
    b_quit.place(x=467, y=400)

    # ============= Labels =============
    welcome = Label(root, text="به منوی اپ خوش آمدید", font=("b koodak", 16),
                    bg=color_1, foreground=color)
    welcome.place(x=467, y=10)

    created = Frame(root, width=6, height=2, bg='black')
    created.place(x=0,y=475)

    developer = Label(created, text="Created by Mobin Bagheri ", font=("b koodak", 9),
                    bg=color_1, foreground=color)
    developer.pack(side=TOP)




    root.mainloop()

main_screen()