from tkinter import * 
from tkinter import messagebox
import os

quizz = Tk()
quizz.title("Jeux Niveau : Facile ")
quizz.state("zoomed")

# Définir une police plus grande
large_font = ('Arial', 16)

# Liste des questions et des réponses correctes
questions = [
    ("Combien font 1 + 1 ?", "A"),
    ("Quelle est la première lettre de l'alphabet ?", "B"),
    ("Combien de côtés a un triangle ?", "C"),
    ("Quel est le contraire de jour ?", "D"),
    ("Combien de doigts as-tu sur une main ?", "A"),
    ("Quelle est la couleur du ciel par temps clair ?", "B"),
    ("Combien de jours y a-t-il dans une semaine ?", "C"),
    ("Quel est le cinquième mois de l'année ?", "D"),
    ("Combien de pattes a un chat ?", "A"),
    ("Quelle est la capitale de la France ?", "B")
]

# Réponses possibles
reponses_possibles = [
    ("A) 2", "B) 5", "C) 3", "D) x"),
    ("A) Z", "B) A", "C) B", "D) C"),
    ("A) 4", "B) 5", "C) 3", "D) 6"),
    ("A) Soleil", "B) Matin", "C) Lumière", "D) Nuit"),
    ("A) 5", "B) 6", "C) 4", "D) 7"),
    ("A) Vert", "B) Bleu", "C) Rouge", "D) Jaune"),
    ("A) 5", "B) 6", "C) 7", "D) 8"),
    ("A) Mars", "B) Avril", "C) Juin", "D) Mai"),
    ("A) 4", "B) 2", "C) 6", "D) 8"),
    ("A) Londres", "B) Paris", "C) Berlin", "D) Madrid")
]

# Index du quiz actuel
current_quiz = 0

# Variable pour stocker la réponse sélectionnée
reponse = StringVar()

# Variable globale pour les vies
life = 1

def afficher_question():
    global current_quiz
    question, _ = questions[current_quiz]
    L1.config(text=question)
    R1.config(text=reponses_possibles[current_quiz][0])
    R2.config(text=reponses_possibles[current_quiz][1])
    R3.config(text=reponses_possibles[current_quiz][2])
    R4.config(text=reponses_possibles[current_quiz][3])
    reponse.set(None)  # Réinitialiser la sélection

def verifier():
    global life, current_quiz
    _, bonne_reponse = questions[current_quiz]
    if reponse.get() == bonne_reponse:
        current_quiz += 1
        if current_quiz < len(questions):
            afficher_question()
        else:
            messagebox.showinfo("Félicitations", "Vous avez terminé tous les quiz!")
            quizz.quit()
    else:
        life = life - 1
        print(life)
        messagebox.showinfo("Résultat", f"Désolé, ce n'est pas la bonne réponse. Il te reste {life} chances.")
        if life == 0:
            messagebox.showinfo("Désolé", "Tu as perdu toutes tes chances !")
            afficher_reponses()


def fermer_et_retourner():
    fenetre_reponses.destroy()
    quizz.destroy()
    os.system('python main.py')


def afficher_reponses():
    fenetre_reponses = Toplevel(quizz)
    fenetre_reponses.title("Réponses correctes")
    fenetre_reponses.geometry("400x400")

    Label(fenetre_reponses, text="Réponses correctes", font=('Arial', 18, 'bold')).pack(pady=10)

    for i, (question, reponse) in enumerate(questions):
        texte = f"Q{i+1}: {question}\nRéponse: {reponses_possibles[i][ord(reponse) - 65]}"
        Label(fenetre_reponses, text=texte, font=('Arial', 12), justify=LEFT, wraplength=380).pack(pady=5)

    Button(fenetre_reponses, text="Fermer", command=fenetre_reponses.destroy, font=large_font).pack(pady=10)
    quizz.after(30000, fermer_et_retourner)



# Configurer les widgets
L1 = Label(quizz, text="", font=large_font)
L1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Ajouter des espaces réservés pour uniformiser la largeur
quizz.grid_columnconfigure(0, minsize=100)
quizz.grid_columnconfigure(1, minsize=100)
quizz.grid_columnconfigure(2, minsize=100)
quizz.grid_columnconfigure(3, minsize=100)

R1 = Radiobutton(quizz, text="", variable=reponse, value="A", font=large_font)
R1.grid(row=3, column=0, padx=10, pady=10)

R2 = Radiobutton(quizz, text="", variable=reponse, value="B", font=large_font) 
R2.grid(row=3, column=1, padx=10, pady=10)

R3 = Radiobutton(quizz, text="", variable=reponse, value="C", font=large_font)
R3.grid(row=3, column=2, padx=10, pady=10)

R4 = Radiobutton(quizz, text="", variable=reponse, value="D", font=large_font)
R4.grid(row=3, column=3, padx=10, pady=10)

bouton_verifier = Button(quizz, text="Vérifier", command=verifier, font=large_font)
bouton_verifier.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Afficher la première question
afficher_question()

quizz.mainloop()

fermer_et_retourner()
def fermer_et_retourner():
    fenetre_reponses.destroy()
    quizz.destroy()
    os.system('python main.py')

