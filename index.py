from tkinter import *
from PIL import Image, ImageTk
import random

listImages = [Image.open("face1.png"), 
              Image.open("face2.png"),
              Image.open("face3.jpg"),
              Image.open("face4.png"),
              Image.open("face5.png"),
              Image.open("face6.png")]

fenetre = Tk()
fenetre.geometry("600x670+400+40")
fenetre.title("Jeu de simulation de dé")
fenetre.config(bg="black")

choixImage = random.choice(listImages)
imageInitial = ImageTk.PhotoImage(choixImage.resize((350, 350)))

titre = Label(fenetre, text="Choisi un nombre pour jouer", 
              font=("Arial", 12, "bold"), fg="white", 
              width=30, bg="black")
titre.place(relx=0.5, y=50, anchor="center", height=40)

champ = Entry(fenetre)
champ.place(relx=0.5, y=120, anchor="center", height=30, width=50)

label0 = Label(fenetre, bg="black")
label0.place(relx=0.5, y=573, anchor="center", height=50, width=400)

def verifie_valeur(x):
    if x.isdigit():
        x = int(x)
        if 1 <= x <= 6:
            return x
        else:
            label0.config(text="Veuillez choisir un nombre entre 1 et 6")
    else:
        label0.config(text="Saisie invalide, entrez un nombre entre 1 et 6")
    return None

# Cette fonction met à jour l'image du label
def lancer():
    nombre = verifie_valeur(champ.get())
    de_lance = random.choice(listImages)
    indexImage = listImages.index(de_lance)
    imageAffiche = ImageTk.PhotoImage(de_lance.resize((350, 350)))
    
    # Mettre à jour l'image du label
    label.config(image=imageAffiche)
    
    # Conserver la référence de l'image dans la fenêtre pour éviter que l'image soit effacée
    label.image = imageAffiche

    if (nombre - 1) == indexImage:
        label0.config(text="Bravo, vous avez gagné !")
    else:
        label0.config(text="Dommage vous avez perdu ! Résessayer", fg="white")

# Créer le label avec l'image initiale
label = Label(fenetre, image=imageInitial)
label.place(relx=0.5, y=330, anchor="center", width=350, height=350)

bouttonLancer = Button(fenetre, text="Lancer", command=lancer)
bouttonLancer.place(relx=0.3, y=650, anchor="center", width=100)

bouttonQuit = Button(fenetre, text="Quitter", command=fenetre.quit)
bouttonQuit.place(relx=0.7, y=650, anchor="center", width=100)

fenetre.mainloop()
