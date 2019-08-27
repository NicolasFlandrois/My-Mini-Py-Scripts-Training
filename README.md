# My-Mini-Py-Scripts
Mini python Scripts

In this repository I'll stack tiny scripts, command lines automation, small programs, practices, and exercices that are not part of a bigger projects,  or not big enough to have it's own project repository.

----------------------------
## TOOLS:

- **ask_integer.py**:

    create a fonction to verify if input number is integer and within range.

    *status*: Finished

--------------------------
## TINY PROJECTS:

+ **autogitcommitandpush.py**:

    This tiny project aim to automatically run bash scripts, from a python program, to commit in git every 20 min (1200sec), and after a loop of 4 cycles, push to remote GitHub repository.

    *status*: Finished

+ **Guess-the-number.py**:

    Small exercice/game, create a small guessing game: guess the randomly generated number within range [1;100], within 7 or 8 guess.

    *status*: Finished

+ **xmascountdown.py**:

    Create a Christmas count down, in Python.

    *status*: Finished

+ **drink_dispenser** [Folder]:

    Creating the script for a dispenser machine, asking for money according to price, and giving back change, taking into account a few perks.

    *status*: **[Work in progress]**

+ **fibonacci.py**:

    Generator and intention/comprehension list to create a fibonacci sequence, for n iterations.

    *status*: Finished

+ **tribonacci.py**:

    Generator and intention/comprehension list to create a tribonacci sequence, for n iterations.

    *status*: Finished

+ **Deck of cards** ('class'/OOP exercice):

    Generate a deck of cards, and deal hands to players.
    Using Object Oriented Programming, with python Classes system

    *status*: Finished

+ **Passphrase generator** [pw.py]:

    From a given text (or collection of books and dictionnaries, the more the merryer), the script will create a list of words choosen entirely randomly.

    *status*: **[Work in progress]**

+ **Pychain** (simple blockchain in python):

    Create in python a simple blockchain (as an exercise). -details and what will it be used for, to be determined-

    *status*: **[Ice box - Waiting to work on it]**

+ **rename.py**:

    Create in python an automating renaming multiple files script in a given directory.

    **Evolutions for v2.0**: I'd like to factorize this function, as a Class, OOP, or a simple function, so I can call this function in any project, and simplify the use, just by passing arguments.

    Arguments should be:

    - The Path in: os.chdir('/home/User/Pictures')

    - The New Name, in: new_name, or define f_title as the original if no specific arguments, otherwise if enter a string as an argument, this string becomes the title.

    *status*: v1.0 Finished

+ **Random Walk**:

    Monte Carlo simulation practice, applied to a random walk. cf description in the file.

    *status*: Finished

+ **GIF Converter**:

    This script (gifconvert.py) is a simple video converter, initially intended to convert videos into GIF files.

    *status*: Finished

+ **myrange.py**:

    Practice exercise using Iterators, Class and Generators. This script will simulate (recreate) Python's range method.

    *status*: Finished

+ **tips_and_tricks.py**:

    Practice exercise using Itertools, Sorted, f-strings.

    *status*: Finished

+ **sort_and_itertools.py**:

    Practice exercise to sort & iterate non ewploitable raw data, using: Itertools, collections, and/or sorted.

    *status*: Finished

+ **imc.py**:

    This short script (French user) tend to compute a person's "IMC" (Indice de Masse Corporel), the health weight/heigh² ratio.

    *to Do in v2*:

    - Incorporate the New IMC compute formula
    (Formule d’IMC classique : poids / taille^2
    Nouvelle formule d’IMC :1,3 x poids / taille^2,5)

    - Script Optimisation

    - Factoring

    - Create a menu (And/Or a GUI)

    *status*: v1.0 Finished

-----------------------------
## EXERCICES/PRACTICES:

- **SAN ANTONIO** (Open Classroom exercise):

    Suivi d'exercices de cours Démarrez votre projet en Python. Mini programme donnant des citations de San Antonio

    *status*: Finished

- **Matplotlib practice**:

    Follows [Youtube tutorial from Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) on Matplotlib

    *status*: Finished

- **Semaphore**: Static Method, intro from Mentor.
- **Singleton**: Static Method, intro from Mentor.
- **Factory Method**: Intro to Factory design pattern, from Mentor..

----------------------------
## Mini projects that moved to become a project of its own.

Those projects moved to their own repositories:

+ **Stardate Project**:

    - Generate (star trek) Stardate according to current time. Changing reference date.
    - Convert a date for input gregorian date (ISO-8601), to a stardate.
    - Translate a stardate input to a Gregorian date (ISO-8601).
    - This project has now an [independant GitHub Repository](https://github.com/NicolasFlandrois/stardate.git), and is no longer followed in this My-Mini-Python-Script Repo.

    *status*: Finished - v2

+ **Mayan Calendar Project** :

    - Generate of Mayan Long Count Calendar according to current time. Changing reference date.
    - Convert an input date (from gregorian ISO-8601 calendar) to Long Count.
    - Translate a Long Count Input, into a Gregorian date (ISO-8601 calendar).
    - Same 2 generator, convertor, translator, for Tzolkin and Ha'ab Mayan Calendar. Which is more difficult, as they are cycles, and don't refer to a year.
    - This project has now an [independant GitHub Repository](https://github.com/NicolasFlandrois/maya_date.git), and is no longer followed in this My-Mini-Python-Script Repo.

    *status*: Finished - v1

+ **Name Data Base Generator** (python + SQL):

    - The python generator will create random name association from lists of male names, female names and Family names, to generate a sql data base. Further more this kind of data base generator, can generate massive amount of data (names pairs). Such data base can be use to test software and scripts needing data. Such generator can be used for other objects than names.

    - Each entry containing:
        + ID SQL Key (autogenerated by SQL)
        + Family name (randomly paired with first name)
        + First name (randomly paired with family name)
        + Gender (M/F depending on first name randomly assigned)
        + Birth date (Random)
        + Socialsecurity number (According to gender + Year of birth + Month of birth + Randomly assigned department number in range or within a list + 8 random numbers) cf: [wiki page](https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France#ancrage_C)

    *status*: **[Ice box - Waiting to work on it]**
