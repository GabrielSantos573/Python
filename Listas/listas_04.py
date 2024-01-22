"""Listas 04.ipynb

# Adicionar e Remover itens de uma lista

Adicionar:
lista.append(item)

Remover:
item_removido = lista.pop(indice)
lista.remove(item)

Digamos que você está construindo o controle de produtos da Apple.
E a Apple lançou o IPhone 11 e irá tirar dos seus estoques o IPhone X
"""

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

"""## Existem 2 formas de tratar o erro:

1. Criar um if para evitar que ele aconteça

2. Esperar que ele possa acontecer e tratar caso o erro aconteça com:
"""
try:
    produtos.remove('iphone x')
    print(produtos)
except:
    pass #caso não tenha o que fazer caso o try n dê certo 




