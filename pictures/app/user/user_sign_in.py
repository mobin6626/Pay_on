import tkinter.messagebox
from tkinter import *
from app.main import *


def user_screen():

    global user
    global user_screen

    user = Tk()
    user.title("pay on(user)")
    user.geometry("1100x500")
    user.resizable(False, False)
    color = "black"
    color_1 = "#b3f542"
    color_2 = "#f5a442"
    user.configure(bg=color_1)


    # ======== Functions ========
    def errorMsg(ms):
        if ms == 'error':
            tkinter.messagebox.showerror('دوباره امتحان کنید', 'مشکلی پیش آمده لطفا دوباره امتحان کنید')


    def back_to_main_user():
        user.quit()
        main_screen()


    # ======== Label ========
    item_label = Label(user, text='نام کالا', font=('b koodak', 14), bg=color_1)
    item_label.grid(row=0, column=3)

    tip_label = Label(user, text='تیپ', font=('b koodak', 14), bg=color_1)
    tip_label.grid(row=1, column=3)

    waiter_label= Label(user, text='پیشخدمت', font=('b koodak', 14), bg=color_1)
    waiter_label.grid(row=3, column=3)

    price_label = Label(user, text='قیمت کالا', font=('b koodak', 14), bg=color_1)
    price_label.grid(row=4, column=3, rowspan=5)

    numbers_label = Label(user, text='تعداد', font=('b koodak', 14), bg=color_1)
    numbers_label.grid(row=7, column=3, rowspan=5)

    tip_all_label = Label(user, text='تیپ کل', font=('b koodak', 14), bg=color_1)
    tip_all_label.grid(row=3, column=6, rowspan=2)

    price_all_label = Label(user, text='قیمت کل', font=('b koodak', 14), bg=color_1)
    price_all_label.grid(row=4, column=6, rowspan=3)



    # ======== Entry ========
    name_var = StringVar()
    name_item = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                      highlightbackground=color_2, textvariable=name_var)
    name_item.grid(row=0, column=0, columnspan=3)

    tip = Scale(user, orient='horizontal', width=20, bg=color_2, foreground=color_1,
                highlightbackground=color_2)
    tip.grid(row=1, column=0, columnspan=3, rowspan=1)

    waiter_var = StringVar()
    waiter = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                   highlightbackground=color_2, textvariable=waiter_var)
    waiter.grid(row=3, column=0, columnspan=3, rowspan=2)

    price_var = IntVar()
    item_price = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                       highlightbackground=color_2, textvariable=price_var)
    item_price.grid(row=6, column=0, columnspan=3, rowspan=2)


    numbers_var = IntVar()
    numbers = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                    highlightbackground=color_2, textvariable=numbers_var)
    numbers.grid(row=9, column=2, rowspan=2)

    # ------------

    tip_var = IntVar()
    tip_all = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                    highlightbackground=color_2, textvariable=tip_var)
    tip_all.grid(row=3, column=5, rowspan=2)

    price_all_var = IntVar()
    price_all = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                      highlightbackground=color_2, textvariable=price_all_var)
    price_all.grid(row=5, column=5, rowspan=3)




    # ======== List Box ========
    items = Listbox(user, font=('b koodak', 14), width=35, height=3, bg=color_2, foreground=color_1,
                    highlightbackground=color_2)
    items.grid(row=0, column=4, columnspan=3, rowspan=2)

    item_list_user = Listbox(user, font=('b koodak', 14), width=36, height=10, bg=color_2, foreground=color_1,
                        highlightbackground=color_2)
    item_list_user.grid(row=13, column=14)

    scrolbar_list = Scrollbar(user, bg=color_2)
    scrolbar_list.grid(row=12 ,column=10, rowspan=2)

    item_list_user.configure(yscrollcommand=scrolbar_list.set)
    scrolbar_list.configure(command=item_list_user.yview)



    # ======== Button ========
    b_back = Button(user, text="بازگشت", font=("b koodak", 14), width=11, height=1, bg=color_2, foreground=color_1,
                    highlightbackground=color_2, command=back_to_main_user)
    b_back.place(x=0, y=442)

    choose = Button(user, text="انتخاب", font=("b koodak", 14), width=14, height=1, bg=color_2, foreground=color_1,
                    highlightbackground=color_2)
    choose.grid(row=12, column=2, rowspan=1)

    delete_in_list = Button(user, text="حذف", font=("b koodak", 14), width=8, height=1, bg=color_2, foreground=color_1,
                            highlightbackground=color_2)
    delete_in_list.grid(row=0, column=9)

    purchase = Button(user, text="پرداخت", font=("b koodak", 14), width=14, height=2, bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    purchase.grid(row=12, column=5)



    user.mainloop()


user_screen()