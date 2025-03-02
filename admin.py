import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import os

class AdminApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.title("Admin Panel")
        self.geometry("400x300")

        # Configuration du thème
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Interface de connexion
        self.create_login_widgets()

    def create_login_widgets(self):
        # Titre
        title_label = ctk.CTkLabel(self.main_frame, text="Admin Login", font=("Arial", 24))
        title_label.pack(pady=20)

        # Champ de mot de passe
        self.password_entry = ctk.CTkEntry(self.main_frame, show="*", width=200)
        self.password_entry.pack(pady=20)

        # Bouton de connexion
        login_button = ctk.CTkButton(self.main_frame, text="Se connecter", command=self.verify_password)
        login_button.pack(pady=20)

    def verify_password(self):
        if self.password_entry.get() == "1234":
            self.show_stats_interface()
        else:
            messagebox.showerror("Erreur", "Mot de passe incorrect!")

    def show_stats_interface(self):
        # Nettoyer la frame principale
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Boutons pour les différentes statistiques
        ctk.CTkButton(self.main_frame, text="Distribution par genre", 
                     command=self.show_gender_stats).pack(pady=10)
        
        ctk.CTkButton(self.main_frame, text="Distribution par ages", 
                     command=self.show_age_stats).pack(pady=10)
        
        ctk.CTkButton(self.main_frame, text="Moyenne par niveau", 
                     command=self.show_score_by_level).pack(pady=10)
        
        ctk.CTkButton(self.main_frame, text="Score par tranche d'âge", 
                     command=self.show_score_by_age).pack(pady=10)
        
        ctk.CTkButton(self.main_frame, text="Retour", 
                     command=self.return_to_main).pack(pady=10)

    def show_gender_stats(self):
        try:
            # Lire le fichier CSV
            df = pd.read_csv("inscriptions.csv", names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Compter le nombre d'utilisateurs par genre
            gender_counts = df["Genre"].value_counts()
            
            # Créer une nouvelle fenêtre pour le graphique
            stats_window = ctk.CTkToplevel(self)
            stats_window.title("Statistiques par Genre")
            stats_window.geometry("600x500")
            
            # Créer une figure matplotlib
            fig = plt.Figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            
            # Créer le camembert
            colors = ['#FF9999', '#66B2FF']
            wedges, texts, autotexts = ax.pie(gender_counts.values, 
                                            labels=gender_counts.index,
                                            colors=colors,
                                            autopct='%1.1f%%',
                                            startangle=90)
            
            # Égaliser l'aspect du camembert
            ax.axis('equal')
            
            # Ajouter un titre
            ax.set_title("Répartition des Utilisateurs par Genre")
            
            # Créer le canvas
            canvas = FigureCanvasTkAgg(fig, master=stats_window)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=20)
            
            # Ajouter les statistiques textuelles
            stats_text = f"\nNombre total d'utilisateurs : {len(df)}\n"
            for genre, count in gender_counts.items():
                stats_text += f"\n{genre} : {count} utilisateurs"
            
            stats_label = ctk.CTkLabel(stats_window, text=stats_text, font=("Arial", 14))
            stats_label.pack(pady=20)
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'affichage des statistiques : {str(e)}")

    def show_level_performance(self):
        try:
            df = pd.read_csv("inscriptions.csv", 
                           names=["Genre", "Nom", "Prenom", "Age", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Calculer les moyennes des scores pour chaque niveau
            scores_moyens = {
                "Facile": df["Score_Facile"].mean(),
                "Intermédiaire": df["Score_Inter"].mean(),
                "Difficile": df["Score_Diff"].mean()
            }
            
            plt.figure(figsize=(8, 6))
            plt.bar(scores_moyens.keys(), scores_moyens.values())
            plt.title("Score moyen par niveau")
            plt.xlabel("Niveau")
            plt.ylabel("Score moyen")
            
            plt.savefig("level_stats.png")
            plt.close()
            
            self.show_stats_window("level_stats.png", "Performance par niveau")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture du fichier: {str(e)}")

    def show_age_stats(self):
        try:
            # Lire le fichier CSV
            df = pd.read_csv("inscriptions.csv", names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Convertir la colonne Age en numérique, en ignorant les erreurs
            df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
            
            # Créer une nouvelle fenêtre pour le graphique
            stats_window = ctk.CTkToplevel(self)
            stats_window.title("Distribution par Ages")
            stats_window.geometry("600x500")
            
            # Créer une figure matplotlib
            fig = plt.Figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            
            # Créer l'histogramme
            ax.hist(df['Age'].dropna(), bins=10, color='#66B2FF', edgecolor='black')
            ax.set_title("Distribution des Ages")
            ax.set_xlabel("Age")
            ax.set_ylabel("Nombre d'utilisateurs")
            
            # Créer le canvas
            canvas = FigureCanvasTkAgg(fig, master=stats_window)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=20)
            
            # Ajouter les statistiques textuelles
            stats_text = f"\nStatistiques des ages :\n"
            stats_text += f"\nMoyenne d'age : {df['Age'].mean():.1f} ans"
            stats_text += f"\nAge minimum : {df['Age'].min():.0f} ans"
            stats_text += f"\nAge maximum : {df['Age'].max():.0f} ans"
            
            stats_label = ctk.CTkLabel(stats_window, text=stats_text, font=("Arial", 14))
            stats_label.pack(pady=20)
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'affichage des statistiques : {str(e)}")

    def show_stats_window(self, image_path, title):
        # Créer une nouvelle fenêtre pour les statistiques
        stats_window = ctk.CTkToplevel(self)
        stats_window.title(title)
        stats_window.geometry("600x500")

        # Charger et afficher l'image
        img = Image.open(image_path)
        photo = ctk.CTkImage(img, size=(500, 400))
        img_label = ctk.CTkLabel(stats_window, image=photo, text="")
        img_label.pack(pady=20)

        # Bouton pour fermer
        close_button = ctk.CTkButton(stats_window, text="Fermer", command=stats_window.destroy)
        close_button.pack(pady=10)

    def show_score_by_level(self):
        try:
            # Lire le fichier CSV
            df = pd.read_csv("inscriptions.csv", names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Calculer les moyennes
            score_facile = df['Score_Facile'].mean()
            score_inter = df['Score_Inter'].mean()
            score_diff = df['Score_Diff'].mean()
            
            # Afficher dans une fenêtre
            messagebox.showinfo("Scores par niveau", 
                              f"Moyennes des scores :\n\n"
                              f"Niveau Facile : {score_facile:.1f}\n"
                              f"Niveau Intermédiaire : {score_inter:.1f}\n"
                              f"Niveau Difficile : {score_diff:.1f}")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {str(e)}")

    def show_score_by_age(self):
        try:
            # Lire le fichier CSV
            df = pd.read_csv("inscriptions.csv", names=["Genre", "Nom", "Prenom", "Age", "Niveau", "Mail", "Score_Facile", "Score_Inter", "Score_Diff"])
            
            # Convertir l'âge en numérique
            df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
            
            # Créer des groupes d'âge
            df['Age_Group'] = pd.cut(df['Age'], bins=[0, 20, 30, 100], labels=['0-20 ans', '21-30 ans', '30+ ans'])
            
            # Calculer le score total moyen par groupe d'âge
            df['Score_Total'] = df['Score_Facile'] + df['Score_Inter'] + df['Score_Diff']
            scores_by_age = df.groupby('Age_Group')['Score_Total'].mean()
            
            # Préparer le message
            message = "Score total moyen par âge :\n\n"
            for age_group, score in scores_by_age.items():
                message += f"{age_group} : {score:.1f}\n"
            
            # Afficher dans une fenêtre
            messagebox.showinfo("Scores par âge", message)
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {str(e)}")

    def return_to_main(self):
        self.destroy()

if __name__ == "__main__":
    app = AdminApp()
    app.mainloop()