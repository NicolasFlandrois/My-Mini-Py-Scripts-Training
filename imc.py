#!/usr/bin/python3.7
# UTF8
# Date: Tue 27 Aug 2019 14:27:23 CEST
# Author: Nicolas Flandrois

# Calcul de son IMC
# (Indice de Masse Corporelle)

# Calcul de l'IMC :
# IMC = weight(kg) / height²(m)

# Avec ce résultat, on peut se situer par rapport aux catégories ci-dessous :

# Catégorie de l'IMC (kg/m2)  Classification  Risque de développer des problèmes de santé
# IMC inférieur à 16  Maigreur extrême    Risque de maladie accrue
# IMC compris entre 16 et 19  Maigreur    Risque de maladie élevé
# IMC compris entre 20 et 25  Corpulence normale  Risque de maladie faible
# IMC compris entre 25 et 30  Embonpoint  Risque de maladie accrue
# IMC compris entre 30 et 35  Obésité de classe I Risque de maladie élevé
# IMC compris entre 35 et 40  Obésité de classe II    Risque de maladie très élevé
# IMC supérieur à 40  Obésité de classe III   Risque de maladie extrêmement élevé
# Définition de l'IMC :
# L’IMC (Indice de Masse Corporelle) est notamment utilisé par les diététiciens pour situer le poids d’une personne par rapport à la norme des personnes de sa taille et de son poids.

from math import pow

print("""L’IMC (Indice de Masse Corporelle) est notamment utilisé par les
diététiciens pour situer le poids d’une personne par rapport à la norme
des personnes de sa taille et de son poids.""")

weight = float(input('Poids (kg)? \t'))
height = float(input('Taille (m)? \t'))

imc = round((weight / pow(height, 2)), 2)

def target_weight(imc:int, height:float):
    return round((imc * pow(height, 2)), 2)


print('Votre IMC est de: \t', imc)
if int(imc) in range(0, 16):
    print('Maigreur extrême \t Risque de maladie accrue')
elif int(imc) in range(16, 20):
    print('Maigreur \t Risque de maladie élevé')
elif int(imc) in range(20, 25):
    print('Corpulence normale \t Risque de maladie faible')
elif int(imc) in range(25, 30):
    print('Embonpoint \t Risque de maladie accrue')
elif int(imc) in range(30, 35):
    print('Obésité de classe I \t Risque de maladie élevé')
elif int(imc) in range(35, 40):
    print('Obésité de classe II \t Risque de maladie très élevé')
else:
    print('Obésité de classe III \t Risque de maladie extrêmement élevé')

if int(imc) in range(0, 20):
    print('\n Pour être dans la catégorie cible suivante :\n \
    >>>>  Corpulence normale \t Risque de maladie faible')

    print("Poids Cible moyen :\t", target_weight(22, height),
          "kg. (Soit ", round((target_weight(22, height)) - weight, 2), "kg à gagner.)")
    print("Poids Cible max/au plus mince :\t", target_weight(20, height),
          "kg. (Soit ", round((target_weight(20, height)) - weight, 2), "kg à gagner.)")
    print("Poids Cible min/au plus gros :\t", target_weight(25, height),
          "kg. (Soit ", round((target_weight(25, height)) - weight, 2), "kg à gagner.)")
elif int(imc) in range(20, 25):
    print('Votre Objectif est de maintenir votre forme. Vous êtes dans l\'IMC cible.')
else:
    print('\n Pour être dans la catégorie cible suivante :\n \
    >>>>  Corpulence normale \t Risque de maladie faible')

    print("Poids Cible moyen :\t", target_weight(22, height),
          "kg. (Soit ", round((weight - target_weight(22, height)), 2), "kg à perdre.)")
    print("Poids Cible max/au plus mince :\t", target_weight(20, height),
          "kg. (Soit ", round((weight - target_weight(20, height)), 2), "kg à perdre.)")
    print("Poids Cible min/au plus gros :\t", target_weight(25, height),
          "kg. (Soit ", round((weight - target_weight(25, height)), 2), "kg à perdre.)")

print('\n\n\tCeci est une estimation grossière, et ne remplace pas l\'avis \n\
d\'un spécialiste de santé (Votre médecin généraliste, ou d\'un nutrisioniste)')
