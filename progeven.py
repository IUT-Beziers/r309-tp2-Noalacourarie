from tkinter import *

root = Tk()
root.title('TP2')

def switch():
    label.config(image = photo) 

def routeur():
    label1.config(image = photo1) 
   

button = Button(root, text='switch', command=switch)
button.place(x='', y='100')
button.grid(row=0,column=1)
button1 = Button(root, text='routeur', command=routeur)
button1.place(x='0', y='100')
button1.grid(row=0,column=0)

photo= PhotoImage(file='switch.png')
label = Label(image = '')
label.grid(row=5,column=5)



photo1= PhotoImage(file='routeur.png')
label1 = Label(image = '')
label1.grid(row=5,column=5)


root.mainloop ()