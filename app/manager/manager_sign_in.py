from tkinter import *
from app.main import *
import tkinter.messagebox
import os
import app.data

def manager_screen():

    global manager
    global manager_screen

    manager = Tk()
    manager.title("pay on(manager)")
    manager.geometry("1100x500")
    manager.resizable(False, False)
    color = "black"
    color_1 = "#b3f542"
    color_2 = "#f5a442"
    manager.configure(bg=color_1)



    # ============ variables ============
    username = StringVar()
    password = StringVar()




    # ============ Functions ============

    def errorMsg(ms):
        if ms == 'error':
            tkinter.messagebox.showerror('دوباره امتحان کنید','مشکلی پیش آمده لطفا دوباره امتحان کنید')

    def back_to_main_manager():
        manager.quit()
        main_screen()

    def clear_waiter_list():
        waiter_list.delete(0, END)

    def fill_waiter_list(waiter):
        for waiter_ in waiter:
            waiter_list.insert(END, waiter_)

    def waiter_list_view():
        clear_waiter_list()
        waiter = app.data.view()
        fill_waiter_list(waiter)

    # ============ Label ============
    waiter_name_label = Label(manager, text="پیشخدمت", font=("MRT_AridiNaskh Black", 12), bg=color_1)
    waiter_name_label.grid(row = 0, column = 2)

    waiter_age_label = Label(manager, text="سن", font=("MRT_AridiNaskh Black", 12), bg=color_1)
    waiter_age_label.grid(row = 1, column = 2)

    waiter_income_label = Label(manager, text="درآمد", font=("MRT_AridiNaskh Black", 12), bg=color_1)
    waiter_income_label.grid(row = 2, column = 2)

    item_name_label = Label(manager, text="نام کالا", font=("MRT_AridiNaskh Black", 12), bg=color_1)
    item_name_label.grid(row = 0, column = 3)

    item_price_label = Label(manager, text="قیمت کالا", font=("MRT_AridiNaskh Black", 12), bg=color_1)
    item_price_label.grid(row = 1, column = 3)

    # ============ Entry ============
    waiter_name = Entry(manager, font=("MRT_AridiNaskh Black", 12), bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    waiter_name.grid(row = 0, column=1)

    waiter_age = Entry(manager, font=("MRT_AridiNaskh Black", 12), bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    waiter_age.grid(row = 1, column = 1)

    waiter_income = Entry(manager, font=("MRT_AridiNaskh Black", 12), bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    waiter_income.grid(row = 2, column = 1)

    # --------


    item_name = Entry(manager, font=("MRT_AridiNaskh Black", 12), bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    item_name.grid(row = 0, column=4)

    item_price = Entry(manager, font=("MRT_AridiNaskh Black", 12), bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    item_price.grid(row = 1, column=4)

    # ============ List Box ============
    # show waiters
    waiter_list = Listbox(manager, font=('MRT_AridiNaskh Black', 14), width=40,
                          height=12, bg=color_2, foreground=color_1, highlightbackground=color_2)
    waiter_list.grid(row = 0, column = 0, rowspan = 8)

    waiter_scroll = Scrollbar(manager, orient='horizontal')
    waiter_scroll.grid(row=8, column=0)

    def get_selected_row(event):
        global selected_book
        index = waiter_list.curselection()[0]
        selected_book = waiter_list.get(index)
        waiter_name.delete(0, END)
        waiter_name.insert(END, selected_book[0])
        waiter_age.delete(0, END)
        waiter_age.insert(END, selected_book[1])
        waiter_income.delete(0, END)
        waiter_income.insert(END, selected_book[2])


    waiter_list.bind("<<ListboxSelect>>", get_selected_row)


    # show list of items
    item_list_manager = Listbox(manager, font=('MRT_AridiNaskh Black', 14),
                                width=44, height=12, bg=color_2, foreground=color_1,
                      highlightbackground=color_2)
    item_list_manager.grid(row = 0, column = 5, rowspan = 8)

    item_scroll = Scrollbar(manager, orient="horizontal")
    item_scroll.grid(row = 8, column=5)

    item_list_manager.configure(yscrollcommand = item_scroll.set)
    item_scroll.configure(command = item_list_manager.yview)
    # ============ Button ============

    # add waiter in lists
    def add_to_waiter_list():
        clear_waiter_list()
        waiter = app.data.insert(waiter_name.get(), waiter_age.get(), waiter_income.get())
        fill_waiter_list(waiter)

    add_waiter_list = Button(manager,  text="اضافه کردن", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1,
                             highlightbackground=color, command=add_to_waiter_list)
    add_waiter_list.grid(row= 3, column = 1)

    # update waiter in lists
    def update_to_waiter_list():
        clear_waiter_list()
        waiter = app.data.update()


    update_waiters_list = Button(manager,  text="آپدیت", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1, highlightbackground=color)
    update_waiters_list.grid(row= 4, column = 1)

    def delete_to_waiter_list():
        app.data.delete()
        waiter_list_view()

    delete_waiters_list = Button(manager,  text="حذف", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1,
                                 highlightbackground=color, command=delete_to_waiter_list)
    delete_waiters_list.grid(row= 5, column = 1)

    pay_waiters_list = Button(manager,  text="پرداخت درآمد", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1, highlightbackground=color)
    pay_waiters_list.grid(row= 6, column = 1)






    add_item_list = Button(manager,  text="اضافه کردن کالا", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1, highlightbackground=color)
    add_item_list.grid(row= 2, column = 4)

    update_item_list = Button(manager,  text="آپدیت کالا", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1, highlightbackground=color)
    update_item_list.grid(row= 3, column = 4)

    delete_item_list = Button(manager,  text="حذف کالا", font=("MRT_AridiNaskh Black", 12), width=11,
                    background=color_2, foreground=color_1, highlightbackground=color)
    delete_item_list.grid(row= 4, column = 4)

    b_back = Button(manager,  text="بازگشت", font=("MRT_AridiNaskh Black", 14), width=11, height=1,
                    background=color_2, foreground=color_1,
                    highlightbackground=color, command=back_to_main_manager)
    b_back.place(x=0, y=442)

    # =============================

    waiter_list_view()
    manager.mainloop()

manager_screen()