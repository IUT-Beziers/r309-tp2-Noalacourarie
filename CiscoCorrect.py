from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('TP2')

c = Canvas(root, bg='white', width=600, height=500)
c.pack()

# Fonction pour importer les images dans le canvas

def aff_routeur():
    c.create_image(30,30, image=image1)
    

def aff_switch():
    c.create_image(30,60, image=image2)

def aff_serveur():
    c.create_image(30,30, image=image3)

# Création des boutons pour les images

button = Button(root, text = "Routeur", height= 1, width= 8, padx=2, pady=2,command=aff_routeur)
button.pack(side = LEFT)

button1 = Button(root, text = "Switch",height= 1, width= 8, padx=2, pady=2, command=aff_switch)
button1.pack(side = LEFT)

button2 = Button(root, text = "Serveur",height= 1, width= 8, padx=2, pady=2, command=aff_serveur)
button2.pack(side = LEFT)

# Création des images qui vont être utiliser

imageFile = "routeur.png"
image1 = ImageTk.PhotoImage(Image.open(imageFile))

imageFile = "switch.png"
image2 = ImageTk.PhotoImage(Image.open(imageFile))

imageFile = "serveur.png"
image3 = ImageTk.PhotoImage(Image.open(imageFile))

# Création du bouton quitter

Bouton_Quitter=Button(root, text ='Quitter',height= 1, width= 8, padx=2, pady=2, command=root.destroy)
Bouton_Quitter.pack(side=LEFT,padx=5)

# Appuyer echap pour quitter

root.bind("<Escape>", exit)

# Drag and drop les images

my_label = Label(root, text="to display",bg='yellow', font=30)
my_label.pack(pady=20)

def move(event):
    global image1
    image1 = ImageTk.PhotoImage(Image.open("routeur.png"))
    c.create_image(event.x,event.y, image=image1)
    my_label.config(text="Position x :" + str(event.x) + ', y: ' + str(event.y))

root.bind('<B1-Motion>', move)

root.mainloop()