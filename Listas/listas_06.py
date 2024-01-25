# -*- coding: utf-8 -*-
"""Listas 06.ipynb
# Juntar Listas, Ordenar e Cuidados Especiais

### 2 formas:

- lista1.extend(lista2)
- lista_nova = lista1 + lista2

Obs: o Método .append não junta listas, mas adiciona um valor no final da lista(com .append ele adiciona a lista inteira e não apenas os valores)
"""

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']

produtos.extend(novos_produtos)

print(produtos)

#ou 

totalProdutos = produtos + novos_produtos

print(totalProdutos) #A diferença é que aqui eu não altero nenhuma das duas listas iniciais

"""### Cuidado:

- [1] + [2] não é a mesma coisa que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações.
"""

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

totalVendasIphone = vendas_iphone11 + vendas_iphonex
print(totalVendasIphone)

# !=

totalVendasIphone = vendas_iphone11[0] + vendas_iphonex[0]
print(totalVendasIphone)

"""### Ordenar listas

lista.sort()
"""

produtos.sort()
print(produtos)

vendas.sort(reverse=True)
print(vendas)
