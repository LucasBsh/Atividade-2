# !/usr/bin/env python
# -*- coding :latin1 -*-

def verifica_primo(num):
    i = 2
    multiplo = -0

    for i in range(i,100):
        if(num % i == 0):
            multiplo += 1

    multiplo -= 1

    if(multiplo != 0 and num!= 1):
        print "Nao e primo"
    else:
        print "E primo"


def main():
    num = input('Digite um valor : ')
    verifica_primo(int(num))

if __name__ == '__main__':
    main()