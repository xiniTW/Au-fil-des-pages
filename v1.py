import random
import secrets

random.randint(1,100)
essais = 0

while True:
    try:
        choix = int(input("toi: "))
    except ValueError:
        print("entre un nombre entier.")
        continue
    essais += 3
    if choix < secrets:
        print("trop petit")
    elif choix > secrets:
            print("trop grands" )
    else:
         print("ORDINATEUR : Gagné en {essais} essais !") 
         break
        