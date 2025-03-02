import customtkinter as ctk
from tkinter import messagebox
import random
import pandas as pd

class Quiz(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Jeu de Devinettes - Niveau Intermédiaire")
        self.geometry("800x600")
        
        # Initialisation des variables
        self.vies = 6
        self.score = 0
        self.lettres_trouvees = set()
        
        # Mots et indices
        self.mots = [
            {"mot": "PYTHON", "indice": "Un langage de programmation populaire"},
            {"mot": "ORDINATEUR", "indice": "Machine électronique qui traite les données"},
            {"mot": "ALGORITHME", "indice": "Suite d'instructions pour résoudre un problème"},
            {"mot": "VARIABLE", "indice": "Espace de stockage nommé en programmation"},
            {"mot": "FONCTION", "indice": "Bloc de code réutilisable"},
            {"mot": "BOUCLE", "indice": "Structure qui répète des instructions"},
            {"mot": "INTERFACE", "indice": "Point de connexion entre deux systèmes"},
            {"mot": "MEMOIRE", "indice": "Stockage temporaire des données"},
            {"mot": "LOGICIEL", "indice": "Programme informatique"},
            {"mot": "INTERNET", "indice": "Réseau mondial d'ordinateurs"}
        ]
        
        self.mot_actuel = None
        self.indice_actuel = None
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Créer les widgets
        self.create_widgets()
        self.nouveau_mot()
        
    def create_widgets(self):
        # Label pour l'indice
        self.indice_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 18))
        self.indice_label.pack(pady=20)

        # Label pour le mot à deviner
        self.mot_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 24))
        self.mot_label.pack(pady=20)

        # Frame pour l'entrée de lettre
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(pady=20)

        # Entry pour la lettre
        self.lettre_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.lettre_entry.pack(side="left", padx=10)
        self.lettre_entry.bind('<Return>', lambda e: self.verifier_lettre())

        # Bouton pour valider
        self.submit_button = ctk.CTkButton(self.input_frame, text="Valider", 
                                         command=self.verifier_lettre)
        self.submit_button.pack(side="left", padx=10)

        # Label pour les vies restantes
        self.vie_label = ctk.CTkLabel(self.main_frame, text=f"Vies restantes : {self.vies}", 
                                    font=("Arial", 16))
        self.vie_label.pack(pady=10)

        # Label pour les lettres déjà essayées
        self.lettres_essayees_label = ctk.CTkLabel(self.main_frame, text="Lettres essayées : ", 
                                                  font=("Arial", 16))
        self.lettres_essayees_label.pack(pady=10)

    def nouveau_mot(self):
        if not self.mots:
            self.fin_jeu()
            return
            
        mot_dict = random.choice(self.mots)
        self.mots.remove(mot_dict)
        self.mot_actuel = mot_dict["mot"].upper()
        self.indice_actuel = mot_dict["indice"]
        self.lettres_trouvees = set()
        self.vies = 6
        self.afficher_mot()
        self.indice_label.configure(text=f"Indice : {self.indice_actuel}")
        self.vie_label.configure(text=f"Vies restantes : {self.vies}")
        self.lettres_essayees_label.configure(text="Lettres essayées : ")

    def afficher_mot(self):
        affichage = ""
        for lettre in self.mot_actuel:
            if lettre in self.lettres_trouvees:
                affichage += lettre + " "
            else:
                affichage += "_ "
        self.mot_label.configure(text=affichage)

    def verifier_lettre(self):
        lettre = self.lettre_entry.get().upper()
        self.lettre_entry.delete(0, 'end')
        
        if not lettre or len(lettre) != 1:
            messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre !")
            return
            
        if lettre in self.lettres_trouvees:
            messagebox.showinfo("Info", "Vous avez déjà essayé cette lettre !")
            return
            
        self.lettres_trouvees.add(lettre)
        self.lettres_essayees_label.configure(
            text=f"Lettres essayées : {' '.join(sorted(self.lettres_trouvees))}")
        
        if lettre in self.mot_actuel:
            self.afficher_mot()
            if all(l in self.lettres_trouvees for l in self.mot_actuel):
                self.score += 1
                messagebox.showinfo("Bravo!", "Vous avez trouvé le mot !")
                self.nouveau_mot()
        else:
            self.vies -= 1
            self.vie_label.configure(text=f"Vies restantes : {self.vies}")
            if self.vies <= 0:
                messagebox.showinfo("Game Over", f"Le mot était : {self.mot_actuel}")
                self.fin_jeu()
            else:
                messagebox.showwarning("Raté", "Cette lettre n'est pas dans le mot !")

    def fin_jeu(self):
        # Créer une nouvelle fenêtre pour les résultats
        resultats_window = ctk.CTkToplevel(self)
        resultats_window.title("Résultats")
        resultats_window.geometry("400x300")
        
        # Afficher le score
        score_final = self.score
        score_label = ctk.CTkLabel(resultats_window, 
                                 text=f"Jeu terminé !\nNombre de mots trouvés : {score_final}/{len(self.mots) + 1}", 
                                 font=("Arial", 16))
        score_label.pack(pady=20)
        
        def fermer_et_retourner():
            # Mettre à jour le CSV avec le score
            try:
                # Lire le fichier CSV avec encodage UTF-8
                df = pd.read_csv("inscriptions.csv", 
                               names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"],
                               encoding='utf-8')
                
                # Mettre à jour le score intermédiaire pour la dernière ligne
                df.loc[df.index[-1], "Score_Inter"] = score_final
                
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
        retour_button = ctk.CTkButton(resultats_window, text="Retour au menu", 
                                    command=fermer_et_retourner)
        retour_button.pack(pady=20)

if __name__ == "__main__":
    quiz = Quiz()
    quiz.mainloop()
