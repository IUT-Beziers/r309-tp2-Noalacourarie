from tkinter import *

root = Tk()
root.title('TP2')

def switch():
    label.config(image = photo) 

def routeur():
    label1.config(image = photo1)
   
dessin = Canvas(root, width=1600, height=920, bg='ivory')
dessin.pack(side=TOP, padx=5, pady=5)
button = Button(root, text='switch', command=switch)
'''button.place(x='', y='100')'''
button.pack(side=RIGHT, padx=5, pady=5)
button1 = Button(root, text='routeur', command=routeur)
'''button1.place(x='0', y='100')'''
button1.pack(side=LEFT,padx=5, pady=5)

photo= PhotoImage(file='switch.png')
label = Label(image = '')
label.pack()



photo1= PhotoImage(file='routeur.png')
label1 = Label(image = '')
label1.pack()



root.mainloop ()