import csv 

import smtplib 

from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from tkinter import * 

from tkinter import messagebox 

from tkinter import ttk 

import tkinter as tk 

from PIL import Image, ImageTk 

import pygame  # Import de pygame pour la musique 

import os  # Import du module os pour utiliser os.path.dirname(__file__)

 

# Fenêtre principale 

f = tk.Tk() 

f.state("zoomed")   

f.title("Inscription") 

 

 

# Lancement de la musique 

pygame.mixer.init() 

pygame.mixer.music.load("boom.mp3")  # Remplace "musique.mp3" par ton fichier 

pygame.mixer.music.play(-1)  # -1 pour répéter en boucle 

 

 

 

# Charger l'image de fond 

image = Image.open("bg.png")  # Remplace par le chemin de ton image 

image = image.resize((f.winfo_screenwidth(), f.winfo_screenheight()))  # Adapter à la fenêtre 

bg_image = ImageTk.PhotoImage(image) 

 

 

 

# Afficher l'image dans un Label en arrière-plan 

bg_label = tk.Label(f, image=bg_image) 

bg_label.place(relwidth=1, relheight=1)  # Couvre toute la fenêtre 

 

 

 

 

# Configuration des colonnes pour le centrage 

f.columnconfigure(0, weight=1) 

f.columnconfigure(1, weight=1) 

 

# Labels et champs d'entrée 

l1 = tk.Label(f, text="Genre : ", font=("Arial", 30)) 

l1.grid(row=0, column=0, columnspan=2, sticky="n") 

 

l2 = tk.Label(f, text="Nom : ", font=("Arial", 30)) 

l2.grid(row=1, column=0, columnspan=2, sticky="n") 

 

l3 = tk.Label(f, text="Prénom : ", font=("Arial", 30)) 

l3.grid(row=2, column=0, columnspan=2, sticky="n") 

 

l4 = tk.Label(f, text="Âge : ", font=("Arial", 30)) 

l4.grid(row=3, column=0, columnspan=2, sticky="n") 

 

l5 = tk.Label(f, text="Niveau : ", font=("Arial", 30)) 

l5.grid(row=4, column=0, columnspan=2, sticky="n") 

 

l6 = tk.Label(f, text="Mail : ", font=("Arial", 30)) 

l6.grid(row=5, column=0, columnspan=2, sticky="n") 

 

# Champs d'entrée 

e1 = ttk.Combobox(f, values=["Homme", "Femme", "Autres"], font=("Arial", 14), width=20) 

e1.grid(row=0, column=1, pady=5) 

 

e2 = tk.Entry(f, font=("Arial", 14), width=22)  # Nom 

e2.grid(row=1, column=1, pady=5) 

 

e3 = tk.Entry(f, font=("Arial", 14), width=22)  # Prénom 

e3.grid(row=2, column=1, pady=5) 

 

e4 = tk.Entry(f, font=("Arial", 14), width=22)  # Âge 

e4.grid(row=3, column=1, pady=5) 

 

e5 = ttk.Combobox(f, values=["Facile", "Intermédiaire", "Difficile"], font=("Arial", 14), width=20) 

e5.grid(row=4, column=1) 

 

e6 = tk.Entry(f, font=("Arial", 14), width=22)  # Mail 

e6.grid(row=5, column=1, pady=5) 

 

# Fonction pour enregistrer les données dans un fichier CSV et lancer le jeu 

def enregistrer_et_lancer(): 

    genre_dict = {"Homme": 1, "Femme": 2, "Autres": 0}   

    genre = genre_dict.get(e1.get(), "Inconnu")   

    nom = e2.get() 

    prenom = e3.get() 

    age = e4.get() 

    niveau = e5.get() 

    mail = e6.get() 

 

    if not (nom and prenom and age and niveau and mail and genre != "Inconnu"): 

        messagebox.showerror("Erreur", "Veuillez remplir tous les champs") 

        return 

 

    # Enregistrer les données dans un fichier CSV 

    with open("inscriptions.csv", "a", newline="") as file: 

        writer = csv.writer(file) 

        writer.writerow([genre, nom, prenom, age, niveau, mail]) 

 

    messagebox.showinfo("Succès", "Inscription enregistrée !") 

 

    # Ouvrir la fenêtre du jeu (placeholder pour ton code) 

    ouvrir_jeu() 

 

# Fonction pour ouvrir la fenêtre du jeu (tu mettras ton code de jeu ici) 

def ouvrir_jeu():
    
    # Sélectionner le fichier à exécuter en fonction du niveau
    niveau = e5.get()
    if niveau == "Facile":
        fichier_jeu = "quizz_facile.py"
    elif niveau == "Intermédiaire":
        fichier_jeu = "quizz_intèrmédiaire.py"
    elif niveau == "Difficile":
        fichier_jeu = "quizz_difficile.py"
    
    # Exécuter le fichier du jeu correspondant au niveau
    import subprocess
    subprocess.Popen(['python', fichier_jeu], cwd=os.path.dirname(__file__))
 

# Bouton "Envoyer" 

b1 = tk.Button(f, text="Envoyer", font=("Arial", 14), width=20, height=2, command=enregistrer_et_lancer) 

b1.grid(row=6, column=0, columnspan=2, pady=20) 

 

f.mainloop() 