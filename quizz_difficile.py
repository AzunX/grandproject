import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
import os

class JeuDifferences(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Jeu des différences - Niveau Difficile")
        self.geometry("2200x1200")
        
        # Initialisation des variables
        self.vies = 3
        self.total_differences = 7  # Nombre réel de différences
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Frame pour les images
        self.images_frame = ctk.CTkFrame(self.main_frame)
        self.images_frame.pack(pady=20)
        
        try:
            # Charger les images
            image1 = Image.open("image1.png")
            image2 = Image.open("image2.png")
            
            # Redimensionner les images si nécessaire
            max_size = (2000, 2000)
            image1.thumbnail(max_size)
            image2.thumbnail(max_size)
            
            # Convertir les images pour tkinter
            self.photo1 = ImageTk.PhotoImage(image1)
            self.photo2 = ImageTk.PhotoImage(image2)
            
            # Créer les labels pour les titres des images
            titre1 = ctk.CTkLabel(self.images_frame, text="Image 1", font=("Arial", 20, "bold"))
            titre1.grid(row=0, column=0, padx=20, pady=(0, 10))
            
            titre2 = ctk.CTkLabel(self.images_frame, text="Image 2", font=("Arial", 20, "bold"))
            titre2.grid(row=0, column=1, padx=20, pady=(0, 10))
            
            # Créer les labels pour afficher les images
            self.label1 = ctk.CTkLabel(self.images_frame, image=self.photo1, text="")
            self.label1.grid(row=1, column=0, padx=30)
            
            self.label2 = ctk.CTkLabel(self.images_frame, image=self.photo2, text="")
            self.label2.grid(row=1, column=1, padx=30)
            
        except FileNotFoundError:
            message = ctk.CTkLabel(
                self.images_frame,
                text="Images non trouvées!\n\nPour jouer :\n1. Placez 'image1.png' et 'image2.png' dans le même dossier que ce script\n2. Les images doivent contenir des différences\n3. Redémarrez le jeu",
                font=("Arial", 16)
            )
            message.pack(pady=50)
        
        # Frame pour l'entrée et les informations
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(pady=20)
        
        # Label pour les vies
        self.vies_label = ctk.CTkLabel(
            self.input_frame,
            text=f"Vies restantes : {self.vies}",
            font=("Arial", 16)
        )
        self.vies_label.pack(pady=10)
        
        # Label pour la question
        self.question_label = ctk.CTkLabel(
            self.input_frame,
            text="Combien de différences voyez-vous entre ces deux images ?",
            font=("Arial", 16)
        )
        self.question_label.pack(pady=10)
        
        # Entry pour la réponse
        self.reponse_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.reponse_entry.pack(pady=10)
        self.reponse_entry.bind('<Return>', lambda e: self.verifier_reponse())
        
        # Bouton pour valider
        self.submit_button = ctk.CTkButton(
            self.input_frame,
            text="Valider",
            command=self.verifier_reponse
        )
        self.submit_button.pack(pady=10)
        
    def verifier_reponse(self):
        try:
            reponse = int(self.reponse_entry.get())
            self.reponse_entry.delete(0, 'end')
            
            if reponse == self.total_differences:
                self.fin_jeu(True)
            else:
                self.vies -= 1
                self.vies_label.configure(text=f"Vies restantes : {self.vies}")
                
                if self.vies <= 0:
                    self.fin_jeu(False)
                else:
                    messagebox.showwarning("Incorrect", 
                        f"Ce n'est pas le bon nombre de différences! Il vous reste {self.vies} vies.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide!")
    
    def fin_jeu(self, victoire):
        if victoire:
            message = "Félicitations! Vous avez trouvé le bon nombre de différences!"
            score = self.total_differences  # Score maximum si victoire
        else:
            message = f"Game Over! Il y avait {self.total_differences} différences."
            score = 0  # Pas de points si perdu
        
        # Créer une nouvelle fenêtre pour les résultats
        resultats_window = ctk.CTkToplevel(self)
        resultats_window.title("Fin du jeu")
        resultats_window.geometry("400x300")
        
        # Afficher le message de fin
        score_label = ctk.CTkLabel(
            resultats_window,
            text=message,
            font=("Arial", 16)
        )
        score_label.pack(pady=20)
        
        def fermer_et_retourner():
            # Mettre à jour le CSV avec le score
            try:
                # Lire le fichier CSV avec encodage UTF-8
                df = pd.read_csv(
                    "inscriptions.csv",
                    names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"],
                    encoding='utf-8'
                )
                
                # Mettre à jour le score difficile pour la dernière ligne
                df.loc[df.index[-1], "Score_Diff"] = score
                
                # Sauvegarder le fichier CSV avec encodage UTF-8
                df.to_csv("inscriptions.csv", index=False, header=False, encoding='utf-8')
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la mise à jour du score : {str(e)}")
            
            resultats_window.destroy()
            self.destroy()
            from main import Menu
            menu = Menu()
            menu.mainloop()
        
        # Bouton pour retourner au menu
        retour_button = ctk.CTkButton(
            resultats_window,
            text="Retour au menu",
            command=fermer_et_retourner
        )
        retour_button.pack(pady=20)

if __name__ == "__main__":
    jeu = JeuDifferences()
    jeu.mainloop()