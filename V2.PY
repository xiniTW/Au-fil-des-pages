import random

NB_ESSAIS_MAX = 7
secret = random.randint(1, 100)
essais = 0

print("J'ai choisi un nombre entre 1 et 100. Vous avez 7 essais !")

while essais < NB_ESSAIS_MAX:
    saisie = input(f"Essai {essais + 1}/{NB_ESSAIS_MAX} : ")

    try:
        nombre = int(saisie)
    except ValueError:
        print("Ce n'est pas un nombre")
        continue

    if nombre < 1 or nombre > 100:
        print("le nombre doit être entre compris entre 1 et 100(essai non compté)")
        continue

    essais += 1

    if nombre == secret:
        print(f"Bravo ! Vous avez trouvé le nombre en {essais} essais.")
        break
    elif nombre < secret:
        print("Le nombre est trop petit.")
    else:
        print("Le nombre est trop grand.")

if essais == NB_ESSAIS_MAX and nombre != secret:
    print(f"Perdu ! Le nombre était {secret}.")