#!/usr/bin/env python
# -*- coding :latin1 -*-

idadeDias = input('Digite sua idade em dias: ')

anos  = idadeDias / 365
meses = (idadeDias - (365*anos)) /30
idadeDias = idadeDias - 365*anos
idadeDias = idadeDias - 30*meses

print 'Sua idade e',anos, 'anos', meses, 'meses e',idadeDias , 'dias.'

