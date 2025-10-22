# Exercice : créer un chatbot

import random # toujours en début de fichier !

print("=== Assitant Moral - Premier programme ===")

name = input("Quel est ton prénom ? ")
print("\nEnchanté(e)", name, "!\nJe suis ravie de te connaître.")

mood = input("\nComment te sens-tu aujourd'hui? (bien / moyen / mal) ")

def repondre(mood, name):
 if mood == "bien":
      print(random.choice([
            "Super ! Je suis contente pour toi.",
            "Génial ! Profite de cette bonne énergie.",
            "Top ! Continue sur cette lancée."
            ]))
      
 elif mood == "moyen":
      print(random.choice([
            f"Courage, {name}. Un pas à la fois.",
            "De belles choses t'attendent.",
            "Prend un morceau de chocolat. (^_-)"
            ]))

 elif mood == "mal":
      print(random.choice([
            f"Je suis là, {name}. Tu n'es pas seul(e).",
            "Une chose à la fois. Tu vas t'en sortir.",
            "As-tu quelque chose pour te réconforter?"
            ]))
 else:
      print("Je n'ai pas bien compris ton humeur, peux-tu recommencer?")

repondre(mood, name)
      
print("\nPasse une belle journée, ", name, "!")
