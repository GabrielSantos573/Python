# -*- coding: utf-8 -*-
"""Listas 07.ipynb
# Print de Listas

2 Opções:
- print "normal"
- método join -> delimitador.join(lista)
"""
produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']

print('\n'.join(produtos))

"""Lembrando do método split de strings:

lista = texto.split(separador)
"""

produtos = 'apple tv, mac, iphone x, iphone 11, IPad, apple watch, mac book, airpods'

listaProdutos = produtos.split(', ')#Transformando de texto -> lista, removendo a virgula e o espaço

print(listaProdutos)