from tkinter import *
from PIL import Image
import random

listImages = [Image.open("face1.png"), 
                  Image.open("face2.png"),
                  Image.open("face3.jpg"),
                  Image.open("face4.png"),
                  Image.open("face5.png"),
                  Image.open("face6.png")]

fenetre = Tk()
fenetre.geometry("600x600+400+100")
fenetre.title("Jeu de simulation de dé")

titre = Label(fenetre, text="Choisi un nombre pour jouer", 
              font=("Arial", 12, "bold"), fg="white", 
              width=30, bg="black")
titre.place(relx=0.5, y=50, anchor="center", height=40)

champ = int(Entry(fenetre))
champ.place(relx=0.5, y =120, anchor="center", height=30, width=200)

def choix():
    image = random.choice(listImages)
    image.save("imageChoisi.png")
    return image
    
boutton = Button(text="Quitter", command=quit)
boutton.place(relx=0.5, anchor="center", y = 550, width=100)

fenetre.mainloop()
