from tkinter import * 
from tkinter import messagebox

quizz = Tk()
quizz.title("Jeux Niveau : Difficile ")
quizz.state("zoomed")

# Définir une police plus grande
large_font = ('Arial', 16)

# Liste des questions et des réponses correctes
questions = [
    ("Quel est le nombre premier le plus grand connu ?", "A"),
    ("Quelle est la constante de Planck ?", "B"),
    ("Quel est le théorème de Gödel ?", "C"),
    ("Quelle est la formule de la relativité restreinte ?", "D"),
    ("Quel est le plus grand nombre de Fermat connu ?", "A"),
    ("Quelle est la conjecture de Goldbach ?", "B"),
    ("Quel est le plus grand nombre parfait connu ?", "C"),
    ("Quelle est la conjecture de Poincaré ?", "D"),
    ("Quel est le plus grand nombre de Mersenne connu ?", "A"),
    ("Quelle est la conjecture de Riemann ?", "B")
]

# Réponses possibles
reponses_possibles = [
    ("A) 2^77,232,917-1", "B) 2^31,112,609-1", "C) 2^25,964,951-1", "D) 2^20,996,011-1"),
    ("A) 6.62607015×10^-34 J·s", "B) 6.62607015×10^-34 m^2 kg/s", "C) 6.62607015×10^-34 kg·m^2/s", "D) 6.62607015×10^-34 N·m"),
    ("A) Incomplétude", "B) Complétude", "C) Indécidabilité", "D) Consistance"),
    ("A) E=mc", "B) E=mc^3", "C) E=mc^4", "D) E=mc^2"),
    ("A) 2^32+1", "B) 2^16+1", "C) 2^8+1", "D) 2^4+1"),
    ("A) Tout nombre pair est la somme de deux nombres premiers", "B) Tout nombre pair supérieur à 2 est la somme de deux nombres premiers", "C) Tout nombre impair est la somme de deux nombres premiers", "D) Tout nombre impair supérieur à 2 est la somme de deux nombres premiers"),
    ("A) 2^30,402,457-1", "B) 2^25,964,951-1", "C) 2^8,589,869-1", "D) 2^6,972,593-1"),
    ("A) Toute variété de dimension trois est homéomorphe à la sphère", "B) Toute variété de dimension deux est homéomorphe à la sphère", "C) Toute variété de dimension quatre est homéomorphe à la sphère", "D) Toute variété de dimension trois simplement connexe est homéomorphe à la sphère"),
    ("A) 2^77,232,917-1", "B) 2^31,112,609-1", "C) 2^25,964,951-1", "D) 2^20,996,011-1"),
    ("A) Tous les zéros non triviaux de la fonction zêta de Riemann ont une partie réelle de 1/2", "B) Tous les zéros non triviaux de la fonction zêta de Riemann ont une partie réelle de 1", "C) Tous les zéros non triviaux de la fonction zêta de Riemann ont une partie réelle de 0", "D) Tous les zéros non triviaux de la fonction zêta de Riemann ont une partie réelle de 2")
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