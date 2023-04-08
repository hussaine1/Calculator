import tkinter as tk

master=tk.Tk()
master.title("Calculator")
master.geometry("350x275")

label1=tk.Label(master, text="screen goes here")
label1.grid(row=1,column=0, columnspan=5)

number1=tk.Button(master, text="1")
number1.grid(row=2,column=0)

number2=tk.Button(master, text="2")
number2.grid(row=2,column=1)

number3=tk.Button(master, text="3")
number3.grid(row=2,column=2)

number4=tk.Button(master, text="4")
number4.grid(row=3,column=0)

number5=tk.Button(master, text="5")
number5.grid(row=3,column=1)

number6=tk.Button(master, text="6")
number6.grid(row=3,column=2)

number7=tk.Button(master, text="7")
number7.grid(row=4,column=0)

number8=tk.Button(master, text="8")
number8.grid(row=4,column=1)

number9=tk.Button(master, text="9")
number9.grid(row=4,column=2)

number0=tk.Button(master, text="0")
number0.grid(row=5,column=0, columnspan=2)



master.mainloop()