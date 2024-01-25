# -*- coding: utf-8 -*-
"""List Python - Cartilha de Métodos.ipynb

# Métodos Específicos de Lista em Python

- list.append(valor)<br>
Adiciona um valor ao final de uma lista

Uso:
    vendas = [150, 320]
    vendas.append(110)
Resultado:
    vendas = [150, 320, 110]

- list.extend(lista2)<br>
Adiciona todos os valores da lista2 na lista original

Uso:
    vendas = [150, 320, 110, 450, 390, 370]
    vendas_2semestre = [440, 470, 900, 1000, 1100, 1050]
    vendas.extend(vendas_2semestre)
Resultado:
    vendas = [150, 320, 110, 450, 390, 370, 440, 470, 900, 1000, 1100, 1050]

- list.insert(posicao, valor)<br>
Adiciona um valor em uma posição específica em uma lista. Não é recomendado usar a não ser que seja realmente necessário inserir em uma posição específica, porque o método append é mais eficiente.

Uso:
    vendas = [150, 320]
    vendas.insert(1, 110)
Resultado:
    vendas = [150, 110, 320]
Obs:
    Compare com o caso do list.append para ver a diferença

- list.remove(valor)<br>
Remove o valor da lista (apenas a 1ª ocorrência, então caso haja 2 vezes o valor na lista, apenas a 1ª será removida). Além disso, dá um erro caso valor não exista dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.remove('Maria')
Resultado:
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.pop(posicao)<br>
Remove o item que está na posicao (índice) passado. Além disso, esse item é dado como resultado do pop, portanto pode ser armazenado em uma variável ou usado para outra coisa na mesma linha de código.

Uso:<br>
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']<br>
    vendedores.pop(2)<br>
Resultado:<br>
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.clear()<br>
Remove todos os itens de uma lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.clear()
Resultado:
    vendedores = []

- list.index(valor)<br>
Retorna a posição do valor dentro da lista (em qual índice está o valor). Dá erro caso não haja o valor dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    posicao_Joao = vendedores.index('João')
Resultado:
    posicao_Joao = 0

- list.count(valor)<br>
Retorna a quantidade de vezes que o valor aparece na lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus', 'João']
    qtde_Joao = vendedores.count('João')
Resultado:
    qtde_Joao = 2

- list.sort(reverse=False)<br>
Ordena os valores da lista em ordem crescente, ou alfabética, (reverse=False) ou decrescente (reverse=True).

Uso:
    vendas = [150, 300, 190, 480]
    vendas.sort(reverse=True)
Resultado:
    vendas = [480, 300, 190, 150]

- list.reverse()<br>
Inverte a ordem dos elementos de uma lista.

Uso:
    vendas = [150, 300, 190, 480]
    vendas.reverse()
Resultado:
    vendas = [480, 190, 300, 150]

- list.copy()<br>
Cria uma cópia da lista original. Outra opção é fazer lista2 = lista1[:]

Uso:
    vendas = [150, 300, 190, 480]
    vendas2 = vendas.copy()
Resultado:
    vendas2 = [150, 300, 190, 480]
"""