from tkinter import *
from PIL import Image, ImageTk
import random

fenetre = Tk()
fenetre.geometry("600x670+400+40")
fenetre.title("Jeu de simulation de dé")
fenetre.config(bg="black")

listImages = [
    Image.open("face1.png").resize((350, 350)), 
    Image.open("face2.png").resize((350, 350)),
    Image.open("face3.jpg").resize((350, 350)),
    Image.open("face4.png").resize((350, 350)),
    Image.open("face5.png").resize((350, 350)),
    Image.open("face6.png").resize((350, 350))
]

listImagesTk = [ImageTk.PhotoImage(img) for img in listImages]

choixImage = random.choice(listImagesTk)

titre = Label(fenetre, text="Choisissez un nombre pour jouer", 
              font=("Arial Black", 12, "bold"), bg="black", fg="white")
titre.place(relx=0.5, y=50, anchor="center", height=40, width=300)

champ = Entry(fenetre)
champ.place(relx=0.5, y=120, anchor="center", height=30, width=200)

label0 = Label(fenetre, bg="black")
label0.place(relx=0.5, y=573, anchor="center", height=50, width=500)

def verifie_valeur(x):
    if x.isdigit():
        x = int(x)
        if 1 <= x <= 6:
            return x
        else:
            label0.config(text="Veuillez choisir un nombre entre 1 et 6", fg="#ff0000", font=("Consolas", 14, "bold"))
    else:
        label0.config(text="Saisie invalide, entrez un nombre entre 1 et 6", fg="#ff0000", font=("Consolas", 14, "bold"))
    return None

def lancer():
    nombre = verifie_valeur(champ.get())
    de_lance = random.choice(listImagesTk)
    indexImage = listImagesTk.index(de_lance)
    
    label.config(image=de_lance)
    label.image = de_lance

    if nombre - 1 == indexImage:
        label0.config(text="Bravo, vous avez gagné !", fg="#0000e6", font=("Arial Black", 14, "bold"))
    else:
        label0.config(text="Dommage, vous avez perdu ! Réessayer", fg="#ff0000", font=("Consolas", 14, "bold"))

label = Label(fenetre, image=choixImage)
label.place(relx=0.5, y=330, anchor="center", width=350, height=350)

bouttonLancer = Button(fenetre, text="Lancer", command=lancer)
bouttonLancer.place(relx=0.3, y=650, anchor="center", width=100)

bouttonQuit = Button(fenetre, text="Quitter", command=fenetre.quit)
bouttonQuit.place(relx=0.7, y=650, anchor="center", width=100)

fenetre.mainloop()
