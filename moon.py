#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 04 June 2020 15:28:28
# Last Modified time: Thu 04 June 2020 23:32:47 

# Description: Short project to determine the moon phase from a date.
# Dependency library/requirement: pip install astral
# Official Website: https://astral.readthedocs.io/en/latest/index.html

from astral import moon
from datetime import datetime
import decimal


def float_range(start, stop, step):
    '''Float Range Function. start and stop can be integers or floats.
    Steps is a float, and indicate the decimal float.'''
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)


def moon_phase_name(date, lang='en'):
    '''
    Given a date, this function will return the moon's phase name.
    English by Default
    lang argument:
        'en' = English
        'fr' = French
        'it' = Italian
        'es' = Spanish
        'de' = German
        'no' = Norwegian
        'ru' = Russian
        'cn' = Chinese (Simplified)

        NB: Translations were wupplied by 'Google Translation'.
    '''
    phase_name = {
        'en': ("New Moon", "First Quarter", "Full Moon", "Last Quarter"),
        'fr': ("Nouvelle Lune", "Lune Croissante",
               "Pleine Lune", "Lune Décroissante"),
        'it': ("Nuova Luna", "Luna Crescente", "Luna Piena", "Luna calante"),
        'es': ("Luna nueva", "Luna Creciente", "Luna Llena", "Luna Menguante"),
        'de': ("Neumond", "Halbmond", "Vollmond", "Abnehmender Mond"),
        'no': ("Nymåne", "Halvmåne", "Fullmåne", "Avtagende måne"),
        'ru': ("Новолуние", "полумесяц", "полнолуние", "Убывающая Луна"),
        'cn': ("新月", "新月", "满月", "残月")
    }

    moon_phase = round(moon.phase(date), 2)

    if moon_phase in float_range(0, 7, 0.01):
        return phase_name[lang][0]
    elif moon_phase in float_range(7, 14, 0.01):
        return phase_name[lang][1]
    elif moon_phase in float_range(14, 21, 0.01):
        return phase_name[lang][2]
    elif moon_phase in float_range(21, 28, 0.01):
        return phase_name[lang][3]
    else:
        return None


now = datetime.now()
print(now)
print(now.strftime("%A, %B %d, %Y"))
print(moon_phase_name(datetime.now()))
print(moon_phase_name(datetime.now(), 'fr'))
print(moon_phase_name(datetime.now(), 'it'))
print(moon_phase_name(datetime.now(), 'es'))
print(moon_phase_name(datetime.now(), 'de'))
print(moon_phase_name(datetime.now(), 'en'))
print(moon_phase_name(datetime.now(), 'no'))
print(moon_phase_name(datetime.now(), 'ru'))
print(moon_phase_name(datetime.now(), 'cn'))

print()
birth = datetime(1984, 7, 1, 1, 30, 0, 0)
print(birth.strftime("%A, %B %d, %Y"))
print(moon_phase_name(birth))
