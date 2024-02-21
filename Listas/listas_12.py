# -*- coding: utf-8 -*-
"""Listas 10.ipynb
# Listas de Listas

### Estrutura:

Cada item de uma lista pode ser qualquer tipo de variável. Inclusive, uma lista.

Quando dentro de uma lista temos cada item como sendo uma outra lista, temos uma "nested list", ou seja, uma lista de listas.

Todas as regras de lista e tudo que vimos até agora funciona exatamente igual, mas vamos ver como isso funciona na prática
"""

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

"""- Quanto João vendeu de IPad?
- Quanto Diego vendeu de IPhone
- Qual o total de vendas de IPhone?
"""

joaoIpad = vendas[1][0]
print(joaoIpad)


diegoIphone = vendas[2][1]
print(diegoIphone)


"""- E se Lira na verdade fez apenas 50 vendas de IPhone, como eu modifico na minha lista o valor de vendas dele?"""

vendas[0][1] = 50

"""- E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?"""

produtos.append('mac')

vendasMac = [12, 15, 6, 17]

vendas[0].append(vendasMac[0])#só usar for

