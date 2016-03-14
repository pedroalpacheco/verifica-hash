#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Marco 14 14:00:23 2016
LCI
@author: papacheco
"""

#import md5
import hashlib
#import os


arquivo = open(
    '/home/papacheco/Desktop/API-s-python/verifica-hash/teste1.txt', 'r').read()

arquivo2 = open(
    '/home/papacheco/Desktop/API-s-python/verifica-hash/teste2.txt', 'r').read()

lk = hashlib.md5(arquivo)
lk2 = hashlib.md5(arquivo2)

print(lk)
print(lk2)

if lk == lk:
    print("Arquivos iguais!")
else:
    print("Arquivos diferentes!")
