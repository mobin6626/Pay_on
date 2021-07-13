import tkinter.messagebox
from tkinter import *
from app.main import *
import app.user.data_user
import app.user.data_1_user



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

    # ========= items =========
    def clear_item_list():
        items.delete(0, END)

    def fill_item_list(items):
        for item_ in items:
            items.insert(END, item_)

    def item_list_view():
        clear_item_list()
        items = app.user.data_1_user.view()
        fill_item_list(items)

    # ======== Label ========
    item_label = Label(user, text='نام کالا', font=('b koodak', 14), bg=color_1)
    item_label.grid(row=0, column=2)

    tip_label = Label(user, text='تیپ', font=('b koodak', 14), bg=color_1)
    tip_label.grid(row=1, column=2)

    waiter_label= Label(user, text='پیشخدمت', font=('b koodak', 14), bg=color_1)
    waiter_label.grid(row=2, column=2)


    price_label = Label(user, text='قیمت کالا', font=('b koodak', 14), bg=color_1)
    price_label.grid(row=3, column=2)

    numbers_label = Label(user, text='تعداد', font=('b koodak', 14), bg=color_1)
    numbers_label.grid(row=4, column=2)

    tip_all_label = Label(user, text='تیپ کل', font=('b koodak', 14), bg=color_1)
    tip_all_label.grid(row=3, column=4)

    price_all_label = Label(user, text='قیمت کل', font=('b koodak', 14), bg=color_1)
    price_all_label.grid(row=4, column=4)



    # ======== Entry ========
    name_var = StringVar()
    item_name = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                      highlightbackground=color_2, textvariable=name_var)
    item_name.grid(row=0, column=0)

    tip = Scale(user, orient='horizontal', width=20, bg=color_2, foreground=color_1,
                highlightbackground=color_2)
    tip.grid(row=1, column=0)

    waiter_var = StringVar()
    waiter = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                   highlightbackground=color_2, textvariable=waiter_var)
    waiter.grid(row=2, column=0)

    price_var = IntVar()
    item_price = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                       highlightbackground=color_2, textvariable=price_var)
    item_price.grid(row=3, column=0)


    numbers_var = IntVar()
    numbers = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                    highlightbackground=color_2, textvariable=numbers_var)
    numbers.grid(row=4, column=0)

    # ------------

    tip_var = IntVar()
    tip_all = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                    highlightbackground=color_2, textvariable=tip_var)
    tip_all.grid(row=3, column=3)

    price_all_var = IntVar()
    price_all = Entry(user, width=20, font=('b koodak', 14), bg=color_2, foreground=color_1,
                      highlightbackground=color_2, textvariable=price_all_var)
    price_all.grid(row=4, column=3)




    # ======== List Box ========
    item_list_user = Listbox(user, font=('b koodak', 14), width=35, height=5, bg=color_2, foreground=color_1,
                    highlightbackground=color_2)
    item_list_user.grid(row=0, column=3, rowspan=3, columnspan=2)


    # show all items

    items = Listbox(user, font=('b koodak', 14), width=30, height=15, bg=color_2, foreground=color_1,
                        highlightbackground=color_2)
    items.grid(row=0, column=6, rowspan=25, columnspan=6)

    scrolbar_list = Scrollbar(user, bg=color_2)
    scrolbar_list.place(x=778, y=275)

    items.configure(yscrollcommand=scrolbar_list.set)
    scrolbar_list.configure(command=items.yview)

    def get_selected_row_all_items(event):
        global selected_items
        index = items.curselection()[0]
        selected_items = items.get(index)
        item_name.delete(0, END)
        item_name.insert(END, selected_items[1])
        item_price.delete(0, END)
        item_price.insert(END, selected_items[2])

    items.bind("<<ListboxSelect>>", get_selected_row_all_items)

    # ======== Button ========
    b_back = Button(user, text="بازگشت", font=("b koodak", 14), width=11, height=1, bg=color_2, foreground=color_1,
                    highlightbackground=color_2, command=back_to_main_user)
    b_back.place(x=0, y=442)

    choose = Button(user, text="انتخاب", font=("b koodak", 14), width=13, height=1, bg=color_2, foreground=color_1,
                    highlightbackground=color_2)
    choose.grid(row=6, column=0)

    delete_in_list = Button(user, text="حذف", font=("b koodak", 14), width=13, height=1, bg=color_2, foreground=color_1,
                            highlightbackground=color_2)
    delete_in_list.grid(row=0, column=5)

    def refresh():
        item_list_view()

    refresh = Button(user, text="تازه سازی", font=("b koodak", 14), width=13, height=1, bg=color_2, foreground=color_1,
                            highlightbackground=color_2, command=refresh)
    refresh.grid(row=1, column=5)

    purchase = Button(user, text="پرداخت", font=("b koodak", 14), width=14, height=2, bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    purchase.grid(row=6, column=3)


    item_list_view()
    user.mainloop()


user_screen()