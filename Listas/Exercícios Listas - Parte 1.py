# -*- coding: utf-8 -*-
"""07.07.02 Exercícios Listas.ipynb
# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem
print(vendas_ano)

maisVendas = max(vendas_ano)
menosVendas = min(vendas_ano)

i = vendas_ano.index(maisVendas)
melhorMes = meses[i]

j = vendas_ano.index(menosVendas)
piorMes = meses[j]

print(melhorMes)
print(piorMes)

"""## 2. Continuação
Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""
print(f'O melhor mes do ano foi{melhorMes} com {maisVendas} vendas')
print(f'O pior mes do ano foi{piorMes} com {menosVendas} vendas')

faturamento = sum(vendas_ano)
print(f'Faturamento total: R${faturamento}')

percentual = maisVendas/faturamento

print('O maior valor representou {:.2%} das vendas do ano'.format(percentual))#pra formatar como porcentagem: {:%}

"""## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""

top3 = []

top3.append(maisVendas)
vendas_ano.remove(maisVendas)

maisVendas = max(vendas_ano)

top3.append(maisVendas)
vendas_ano.remove(maisVendas)

maisVendas = max(vendas_ano)

top3.append(maisVendas)
vendas_ano.remove(maisVendas)

print(top3)
