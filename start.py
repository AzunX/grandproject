import customtkinter as ctk
import tkinter as tk
import subprocess
import sys
import os

def execute_main():
    # Lancer main.py dans un nouveau processus
    chemin_main = os.path.join(os.path.dirname(__file__), 'main.py')
    subprocess.Popen(['python', chemin_main])

def execute_admin():
    # Lancer main.py dans un nouveau processus
    chemin_main = os.path.join(os.path.dirname(__file__), 'admin.py')
    subprocess.Popen(['python', chemin_main])

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Quiz Interface")
root.geometry("800x600")

# Ajouter un logo au milieu
from PIL import Image
logo_image = ctk.CTkImage(Image.open("logo.jpg"), size=(300, 300))
logo = ctk.CTkLabel(root, image=logo_image, text="")
logo.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

text_label = ctk.CTkLabel(root, text="Bienvenue au QuizGame !", font=("Arial", 20))
text_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Ajouter le bouton Entrer en bas à gauche
enter_button = ctk.CTkButton(root, text="Admin Menu", fg_color="blue", command=execute_admin)
enter_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)

# Ajouter le bouton Sortir en bas à droite
exit_button = ctk.CTkButton(root, text="Quizz Game", fg_color="blue", command=execute_main)
exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

# Lancer l'application
root.mainloop()
