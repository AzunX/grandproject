import customtkinter as ctk
from tkinter import messagebox
import os
import pandas as pd

# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Quiz(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("Quiz - Niveau Facile")
        self.geometry("800x600")
        
        # Initialisation des variables
        self.current_quiz = 0
        self.vies = 3
        self.bonnes_reponses = 0  # Compteur de bonnes réponses
        
        # Questions, réponses et choix
        self.questions = [
            {
                "question": "Quelle est la capitale de la France ?",
                "reponses": ["Paris", "Lyon", "Marseille", "Bordeaux"],
                "correct": "Paris"
            },
            {
                "question": "Combien font 2+2 ?",
                "reponses": ["3", "4", "5", "6"],
                "correct": "4"
            },
            {
                "question": "De quelle couleur est le ciel ?",
                "reponses": ["Rouge", "Vert", "Bleu", "Jaune"],
                "correct": "Bleu"
            },
            {
                "question": "Quel est le plus grand océan du monde ?",
                "reponses": ["Atlantique", "Indien", "Arctique", "Pacifique"],
                "correct": "Pacifique"
            },
            {
                "question": "Combien y a-t-il de continents ?",
                "reponses": ["5", "6", "7", "8"],
                "correct": "7"
            }
        ]
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Créer les widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Label pour la question
        self.question_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        # Frame pour les boutons
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.pack(pady=20)

        # Boutons de réponse
        self.answer_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(self.buttons_frame, text="", 
                              command=lambda x=i: self.select_answer(x),
                              font=("Arial", 16))
            btn.pack(pady=10)
            self.answer_buttons.append(btn)

        # Label pour les vies restantes
        self.vie_label = ctk.CTkLabel(self.main_frame, text=f"Vies restantes : {self.vies}", font=("Arial", 16))
        self.vie_label.pack(pady=10)

        # Afficher la première question
        self.afficher_question()

    def select_answer(self, index):
        if self.current_quiz >= len(self.questions):
            self.fin_quiz()
            return
            
        question_data = self.questions[self.current_quiz]
        selected_answer = question_data["reponses"][index]
        
        if selected_answer == question_data["correct"]:
            self.bonnes_reponses += 1
            self.current_quiz += 1
            if self.current_quiz < len(self.questions):
                self.afficher_question()
            else:
                self.fin_quiz()
        else:
            self.vies -= 1
            if self.vies > 0:
                self.vie_label.configure(text=f"Vies restantes : {self.vies}")
                messagebox.showwarning("Incorrect", f"Mauvaise réponse ! Il vous reste {self.vies} vies.")
            else:
                self.fin_quiz()

    def afficher_question(self):
        if self.current_quiz >= len(self.questions):
            self.fin_quiz()
            return
            
        question_data = self.questions[self.current_quiz]
        self.question_label.configure(text=question_data["question"])
        
        # Mettre à jour les textes des boutons
        for i, reponse in enumerate(question_data["reponses"]):
            self.answer_buttons[i].configure(text=reponse)

    def fin_quiz(self):
        # Créer une nouvelle fenêtre pour les résultats
        reponses_window = ctk.CTkToplevel(self)
        reponses_window.title("Résultats")
        reponses_window.geometry("400x300")
        
        # Afficher le score
        score_label = ctk.CTkLabel(reponses_window, 
                                 text=f"Quiz terminé !\nNombre de bonnes réponses : {self.bonnes_reponses}/{len(self.questions)}", 
                                 font=("Arial", 16))
        score_label.pack(pady=20)
        
        def fermer_et_retourner():
            # Mettre à jour le CSV avec le nombre de bonnes réponses
            self.update_csv_score()
            reponses_window.destroy()
            self.quit()

        ctk.CTkButton(reponses_window, text="Fermer",
                     command=fermer_et_retourner,
                     font=("Arial", 16)).pack(pady=20)

    def update_csv_score(self):
        try:
            # Lire le fichier CSV
            df = pd.read_csv("inscriptions.csv", names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Trouver la dernière ligne (l'utilisateur actuel) et mettre à jour son score
            df.loc[df.index[-1], "Score_Facile"] = self.bonnes_reponses
            
            # Sauvegarder le fichier CSV
            df.to_csv("inscriptions.csv", index=False, header=False)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la mise à jour du score : {str(e)}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.mainloop()