import random
from time import sleep
import math
import os

# this a casino simulation game

totalMoney = 10000
continuer = True

while continuer :
    print("\nVous débutez la partie avec", totalMoney, 'Dh. \n')
    numeroMise = -1

    # choisir la case sur la quelle on mise
    while numeroMise < 0 or numeroMise > 50:
        try:
            print("Choisissez le numéro de la mise [0,50]")
            numeroMise = int(input("Quel est votre choix? ..."))
        except ValueError:
            print("vous n'avez rien introduit.")
            numeroMise = -1
        if numeroMise < 0:
            print("vous devez choisir un nombre supérieur à 0.")
        elif numeroMise > 50:
            print("vous devez choisir un nombre inférieur à 50.")

    print("Vous avez choisi", numeroMise)

    # choisir le mantant à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > totalMoney:
        mise = input("\nQuelle votre mise?")
        try:
            mise = int(mise)
        except ValueError:
            print("vous n'avez pas choisi votre mise.")
        if mise <= 0:
            print("La mise est négative ou nulle.")
        if mise > totalMoney:
            print("Vous n'avez pas assez d'agent. Vous avez", totalMoney)

    # lancer la roulette
    print("\nLe croupier lance la roulette ...")
    numeroGagnant = random.randrange(0, 50)
    sleep(2)
    print("la roulette s'arrete sur", numeroGagnant)

    # processing
    if numeroGagnant == numeroMise:
        print("\nVous avez miser sur le bon numero, vous gagner", mise *3, 'DH')
        totalMoney += mise * 3
    elif numeroGagnant % 2 == numeroMise % 2:
        print("\nVous avez miser sur la bonne couleur, vous gagnez", math.ceil(mise * 0.5), 'DH')
        totalMoney += math.ceil(mise * 0.5)
    else:
        print("\nDésolé, vous avez perdu", mise, 'DH')
        totalMoney -= mise

    # Game over
    if totalMoney <= 0:
        print("\nVous êtes ruiner, c'est la fin de la partie")
        continuer = False
    else:
        print("\nvous avez maintenant", totalMoney, 'DH')
        quitter = input("\nVoulez vous quitter la partie (o/n)?")
        if quitter == 'o' or quitter == 'O':
            print("\nVous quitter le casino avec", totalMoney, 'DH')
            continuer = False

os.system("pause")


