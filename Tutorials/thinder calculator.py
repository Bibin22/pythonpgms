from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.config(bg="#C370F3")
def hello():
    print("hello world")
button1 = Button(window, text="1", )
button2 = Button(window, text="2",)
button3 = Button(window, text="3",)

button4 = Button(window, text="4", )
button5 = Button(window, text="5",)
button6= Button(window, text="6",)

button7 = Button(window, text="7", )
button8 = Button(window, text="8",)
button9= Button(window, text="9",)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)




window.mainloop()