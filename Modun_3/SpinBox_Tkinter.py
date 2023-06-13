from tkinter import *
window = Tk()
window.title("Welcome to Python PCAP app")
window.geometry('350x200')
#Tạo spinbox có chiều rộng 5, giá trị từ 0 đến 
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=0)
window.mainloop()
