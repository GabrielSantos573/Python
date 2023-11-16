# -*- coding: utf-8 -*-
"""Indice e Tamanho de String.ipynb

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
Pegar um item de uma string: texto[índice]
Pegar o tamanho de um texto: len(texto)
"""

email = 'lira@gmail.com'
nome = 'João Lira'

print(len(email)) 

print(nome[-1]) # Indice negativo onde -1 é o ulitmo caracter ... -3 -2 -1 

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + email[0])
print('Último Caractere ' + email[-1])
print('Servidor do email ' + email[5:10])

