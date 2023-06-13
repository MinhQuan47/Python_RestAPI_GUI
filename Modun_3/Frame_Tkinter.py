from tkinter import *
def say_hi():
    print("Hello!")
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
root.title("Tkinter frame")
label= Label(frame1,text="Python PCAP",justify=LEFT)
label.pack(side=LEFT)
hi_there = Button(frame2,text="BKACAD",command=say_hi)
hi_there.pack()
frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)
root.mainloop()