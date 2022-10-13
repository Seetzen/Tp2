"""Projet fait par  Michael Seetzen
Groupe 403
code pour le jeux de devinette, TP2"""

from random import randint
nb_essaie = 0

devinette = True
def main():
    global devinette, nb_essaie
    while devinette:
        random_number = randint(0, 100)

        not_found = True
        while not_found:

            user_guess = int(input("Quelle numéro devinez-vous?\n"))
            nb_essaie += 1
            if user_guess < random_number:
                print("Vôtre numéro est trop petit")

            elif user_guess > random_number:
                print("Vôtre numéro est trop grand.")

            elif user_guess == random_number:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essaie} essaies.")
                rejouer = input("Voulez-vous rejouer? (y/n)")
                not_found = False

                if rejouer == "y":
                    jouer = True

                elif rejouer == "n":
                    print("Au revoir")
                    jouer = False
main()

