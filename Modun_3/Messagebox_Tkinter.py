from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to Python PCAP app")
window.geometry('350x200')

def clicked():
    messagebox.showinfo('Message title', 'Message content')
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
#Hộp thoại cảnh báo
messagebox.showwarning('Message title', 'Message content')
#Hộp thoại báo lỗi
messagebox.showerror('Message title', 'Message content')
from tkinter import messagebox
res = messagebox.askquestion('Message title','Message content')
res2 = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')
window.mainloop()