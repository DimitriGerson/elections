#!/usr/bin/python3
# -*- coding: utf-8 -*-

def testerFonction(fonction):
    def faireUnPrintAvec1Param(param):
        print('Appel de la fonction : ' + fonction.__name__ + " avec le parmaetre : " + str(param))
        return fonction(param)
    return faireUnPrintAvec1Param


def maFonctionSimple1(nombre):
    """
    Example:
    >>> maFonctionSimple1(4)
    16
    """
    return nombre*nombre

@testerFonction
def maFonctionSimple(nombre):
    """
    les testmod() ne fonctionnent pas avec les fonctions decoratées !!!
    Example:
    >>> print(maFonctionSimple(4))
    1000
    """
    return nombre*nombre


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    print("Les tests de la documentation ont été effectués")
    print(maFonctionSimple(4))
    
        
