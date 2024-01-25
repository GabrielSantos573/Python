# -*- coding: utf-8 -*-
"""Listas 05.ipynb

# Algumas Funções Básicas de Lista

## Tamanho da Lista

tamanho = len(lista)
"""

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

"""- Quantos produtos temos a venda?"""

tamanho = len(produtos)
print(f'Temos {tamanho} produtos')

"""## Maior e Menor Valor

maior = max(lista)

menor = min(lista)
"""

vendas = [1000, 1500, 15000, 270, 900, 100, 1200]

"""- Qual o item mais vendido?
- Qual o item menos vendido?
"""

maisVendido=max(vendas)
menosVendido=min(vendas)

print(f"O mais vendido teve {maisVendido} unidades vendidas")
print(f"O menos vendido {menosVendido} unidades vendidas")

i = vendas.index(maisVendido)
prodMaisVendido = produtos[i]

print(prodMaisVendido)

j = vendas.index(menosVendido)
prodMenosVendido = produtos[j]

print(prodMenosVendido)