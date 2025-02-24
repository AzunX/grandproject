import customtkinter as ctk
import tkinter as tk

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Quiz Interface")
root.geometry("600x400")

# Ajouter un logo au milieu
logo = ctk.CTkLabel(root, text="LOGO", font=("Arial", 24))
logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Ajouter le bouton Entrer en bas à gauche
enter_button = ctk.CTkButton(root, text="Entrer", fg_color="blue")
enter_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)

# Ajouter le bouton Sortir en bas à droite
exit_button = ctk.CTkButton(root, text="Sortir", fg_color="blue")
exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

# Lancer l'application
root.mainloop()
