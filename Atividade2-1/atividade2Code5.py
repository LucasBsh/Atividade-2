# !/usr/bin/env python
# -*- coding :latin1 -*-

def verifica_primo(frase):
    print frase[::-1]

def main():

    frase = raw_input('Digite uma frase : ')
    verifica_primo(frase)

if __name__ == '__main__':
    main()