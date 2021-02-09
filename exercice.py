#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number*-1

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []
    for i in range(len(prefixes)):
        nom = prefixes[i] + suffixe
        noms.append(nom)

    return noms


def prime_integer_summation() -> int:
    nombre = 6
    nombres_premier = [2, 3, 5]

    while len(nombres_premier) < 100:
        premier = True
        for i in range(2, int(nombre**0.5)+1):
            if nombre % i == 0:
                premier = False
                break
        if premier:
            nombres_premier.append(nombre)
        nombre += 1

    return sum(nombres_premier)


def factorial(number: int) -> int:
    i = 0
    facto = 1
    for i in range(number):
        facto *= number-i

    return facto


def use_continue() -> None:
    for i in range(10):
        if i == 5:
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            acceptance.append(False)
            continue
        if 25 in group:
            acceptance.append(True)
            continue

        if 50 in group:
            is_50 = True
        else:
            is_50 = False

        is_accepted = True
        for age in group:
            if (age < 18) or (is_50 and age > 70):
                is_accepted = False
                break

        acceptance.append(is_accepted)
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
