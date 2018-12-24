#! usr/bin/python3
# Tue 25 Dec 2018 12:19:39 AM CET 
# Author: Nicolas Flandrois

def ask_integer(message:str, range, error_message:str = ""):
    """
    Le but de cette fonction
    est de demander un entier à l'utilisateur
    avec un message personnalisé
    Répéter l'opération si l'entrée n'est pas un entier
    avec un message d'erreur personnalisé
    L'entier sera vérifié par la fonction passée en paramètres
    """
    nb = None
    while True:
        try:
            nb = int(input(message))
            if nb in range:
                return nb
                raise
                
        except KeyboardInterrupt:
            break
            
        except:
            print(error_message)


#to do inclued a value to exit the loop, optional, make it as default -1 (cannot be a string or float, as exception will be raised)

print ("test lines")

ask_integer("Please choose a number (range test):", range(1, 100), "Error")
ask_integer("Please choose a number (list test):", (101, 110, 120, 130, 140, 150, 160), "Error")
ask_integer("Please choose a number (Tuples test):", [200, 300, 400, 500, 600], "Error")
