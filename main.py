import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import os
import subprocess
import sys


# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.title("Inscription")
        self.state("zoomed")

        # Centrer les widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Créer un frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Créer les widgets
        self.create_widgets()

        # Lancer la musique
        pygame.mixer.init()
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(-1)

    def create_widgets(self):
        # Labels et champs d'entrée avec style moderne
        labels = ["Genre :", "Nom :", "Prénom :", "Âge :", "Niveau :", "Mail :"]
        self.entries = {}
        
        for i, label in enumerate(labels):
            ctk.CTkLabel(self.main_frame, text=label, font=("Arial", 24)).grid(row=i, column=0, pady=10, padx=20, sticky="e")

        # Combobox pour le genre
        self.entries["genre"] = ctk.CTkComboBox(self.main_frame, values=["Homme", "Femme", "Autres"],
                                               font=("Arial", 16), width=200)
        self.entries["genre"].grid(row=0, column=1, pady=10, padx=20, sticky="w")

        # Entrées texte
        for i, field in enumerate(["nom", "prenom", "age"]):
            self.entries[field] = ctk.CTkEntry(self.main_frame, font=("Arial", 16), width=200)
            self.entries[field].grid(row=i+1, column=1, pady=10, padx=20, sticky="w")

        # Combobox pour le niveau
        self.entries["niveau"] = ctk.CTkComboBox(self.main_frame, values=["Facile", "Intermédiaire", "Difficile"],
                                                font=("Arial", 16), width=200)
        self.entries["niveau"].grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # Entrée pour le mail
        self.entries["mail"] = ctk.CTkEntry(self.main_frame, font=("Arial", 16), width=200)
        self.entries["mail"].grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Bouton d'envoi
        self.submit_button = ctk.CTkButton(self.main_frame, text="Envoyer", font=("Arial", 16),
                                         command=self.enregistrer_et_lancer)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=20)

    def envoyer_email_confirmation(self, email, nom, prenom, niveau):
        # Configuration de l'email
        sender_email = "brachetfabien91@gmail.com"  # À remplacer par votre email
        sender_password = "virr cusn zdox ropn"  # À remplacer par votre mot de passe d'application

        # Création du message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Confirmation d'inscription au Quiz"

        # Corps du message
        body = f"""
        Bonjour {prenom} {nom},

        Nous vous confirmons votre inscription au Quiz de niveau {niveau}.
        Vous pouvez maintenant commencer à jouer !

        Bonne chance !

        L'équipe Quiz
        """
        message.attach(MIMEText(body, "plain"))

        try:
            # Connexion au serveur SMTP de Gmail
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Envoi de l'email
            text = message.as_string()
            server.sendmail(sender_email, email, text)
            server.quit()
            return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'envoi de l'email: {str(e)}")
            return False

    def enregistrer_et_lancer(self):
        # Récupérer les valeurs
        genre_dict = {"Homme": 1, "Femme": 2, "Autres": 0}
        genre = genre_dict.get(self.entries["genre"].get(), "Inconnu")
        nom = self.entries["nom"].get()
        prenom = self.entries["prenom"].get()
        age = self.entries["age"].get()
        niveau = self.entries["niveau"].get()
        mail = self.entries["mail"].get()

        # Vérifier que tous les champs sont remplis
        if not (nom and prenom and age and mail and genre != "Inconnu" and niveau):
            messagebox.showwarning(title="Erreur", message="Veuillez remplir tous les champs")
            return

        # Enregistrer dans le CSV
        with open("inscriptions.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([genre, nom, prenom, age, niveau, mail, 0, 0, 0])  # Ajout des scores initialisés à 0

        # Envoyer l'email de confirmation
        if self.envoyer_email_confirmation(mail, nom, prenom, niveau):
            messagebox.showinfo(title="Succès", message="Inscription enregistrée et email de confirmation envoyé !")
        else:
            messagebox.showinfo(title="Succès partiel", message="Inscription enregistrée mais l'email de confirmation n'a pas pu être envoyé.")
        
        # Lancer le jeu
        self.ouvrir_jeu()

    def ouvrir_jeu(self):
        # Sélectionner le fichier à exécuter en fonction du niveau
        niveau = self.entries["niveau"].get()
        if niveau == "Facile":
            fichier_jeu = "quizz_facile.py"
        elif niveau == "Intermédiaire":
            fichier_jeu = "quizz_intèrmédiaire.py"
        elif niveau == "Difficile":
            fichier_jeu = "quizz_difficile.py"

        # Obtenir le chemin complet du fichier
        chemin_jeu = os.path.join(os.path.dirname(__file__), fichier_jeu)
        
        # Vérifier si le fichier existe
        if not os.path.exists(chemin_jeu):
            messagebox.showerror("Erreur", f"Le fichier {fichier_jeu} n'existe pas!")
            return
        
        try:
            # Lancer le jeu dans un nouveau processus avec le bon interpréteur Python
            process = subprocess.Popen([sys.executable, chemin_jeu])
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du lancement du jeu: {str(e)}")
            return

if __name__ == "__main__":
    app = App()
    app.mainloop()