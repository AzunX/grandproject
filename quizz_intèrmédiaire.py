from tkinter import * 
from tkinter import messagebox

quizz = Tk()
quizz.title("Jeux Niveau : Intermédiaire ")
quizz.state("zoomed")

# Définir une police plus grande
large_font = ('Arial', 16)

# Liste des questions et des réponses correctes
questions = [
    ("Quelle est la capitale de l'Italie ?", "A"),
    ("Quel est le plus grand océan du monde ?", "B"),
    ("Quelle est la formule chimique de l'eau ?", "C"),
    ("Qui a peint la Joconde ?", "D"),
    ("Quel est le plus grand désert du monde ?", "A"),
    ("Quelle est la planète la plus proche du soleil ?", "B"),
    ("Quel est le symbole chimique de l'or ?", "C"),
    ("Combien de continents y a-t-il sur Terre ?", "D"),
    ("Quel est le plus long fleuve du monde ?", "A"),
    ("Quelle est la langue la plus parlée au monde ?", "B")
]

# Réponses possibles
reponses_possibles = [
    ("A) Rome", "B) Paris", "C) Madrid", "D) Berlin"),
    ("A) Atlantique", "B) Pacifique", "C) Indien", "D) Arctique"),
    ("A) CO2", "B) H2", "C) H2O", "D) O2"),
    ("A) Van Gogh", "B) Picasso", "C) Rembrandt", "D) Léonard de Vinci"),
    ("A) Sahara", "B) Gobi", "C) Kalahari", "D) Atacama"),
    ("A) Vénus", "B) Mercure", "C) Mars", "D) Terre"),
    ("A) Ag", "B) Fe", "C) Au", "D) Pb"),
    ("A) 5", "B) 6", "C) 7", "D) 8"),
    ("A) Nil", "B) Amazone", "C) Yangtsé", "D) Mississippi"),
    ("A) Anglais", "B) Mandarin", "C) Espagnol", "D) Hindi")
]

# Index du quiz actuel
current_quiz = 0

# Variable pour stocker la réponse sélectionnée
reponse = StringVar()

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
    global current_quiz
    _, bonne_reponse = questions[current_quiz]
    if reponse.get() == bonne_reponse:
        messagebox.showinfo("Résultat", "Bravo! C'est la bonne réponse!")
        current_quiz += 1
        if current_quiz < len(questions):
            afficher_question()
        else:
            messagebox.showinfo("Félicitations", "Vous avez terminé tous les quiz!")
            quizz.quit()
    else:
        messagebox.showinfo("Résultat", "Désolé, ce n'est pas la bonne réponse.")

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

