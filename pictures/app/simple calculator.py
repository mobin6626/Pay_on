from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Simple Calculator")
root.resizable(False, False)
root.geometry("500x400")
color = "#b315ad"
root.configure(bg=color)


# ======== frames ========
input_frame = Frame(root, bg="#b315ad",width=150, height=150)
input_frame.pack(side='right', ipady=100,padx=40)

frame_buttons = Frame(root, width=500, height=80, bg=color)
frame_buttons.place(x=0, y=200)

frame_res = Frame(root, width=130, height=100)
frame_res.place(x=185,y=320)

# ======== Functions ========
res_one = IntVar()
res_two = IntVar()
res_result = IntVar()


# ======== Functions ========
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division error', "can't divide by 0" )


def plus():
    try:
        value = float(res_one.get()) + float(res_two.get())
        res_result.set(value)
    except:
        errorMsg('error')

def minus():
    try:
        value = float(res_one.get()) - float(res_two.get())
        res_result.set(value)
    except:
        errorMsg('error')


def multyply():
    try:
        value = float(res_one.get()) * float(res_two.get())
        res_result.set(value)
    except:
        errorMsg('error')


def divide():
    try:
        value = float(res_one.get()) / float(res_two.get())
        res_result.set(value)
    except:
        errorMsg('division zero error')
# ======== Button ========
b_plus = Button(frame_buttons, text = 'plus', font=('arial', 11), width=8, height=2, command=plus)
b_plus.pack(side='left' , padx=20)

b_minus = Button(frame_buttons, text = 'minus', font=('arial', 11), width=8, height=2, command=minus)
b_minus.pack(side='left',padx=20)

b_multyply = Button(frame_buttons, text = 'multyply', font=('arial', 11), width=8, height=2, command=multyply)
b_multyply.pack(side='left',padx=20)

b_divide = Button(frame_buttons, text = 'divide', font=('arial', 11), width=8, height=2, command=divide)
b_divide.pack(side='left', padx=20)


# ======== Entry ========
first_in = Entry(input_frame, textvariable=res_one)
first_in.pack(side = TOP, ipady = 2)

second_in = Entry(input_frame, textvariable=res_two)
second_in.pack(side = TOP, ipady=2, pady=10)

res_entry = Entry(frame_res, textvariable=res_result)
res_entry.pack(anchor = 'center')


# ======== labels ========
first_in_label = Label(root, bg=color , foreground='black', text='First Input:', font=("arial", 11))
first_in_label.place(x=240, y=67)

second_in_label = Label(root, bg=color , foreground='black', text='Second Input:', font=("arial", 11))
second_in_label.place(x=240, y=99)

result_in_label = Label(root, bg=color , foreground='black', text='Second Input:', font=("arial", 11))
result_in_label.place(x=89, y=318)

mainloop()