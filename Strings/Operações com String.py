# -*- coding: utf-8 -*-
"""
# Operações com String

str -> transforma número em string<br>
in -> verifica se um texto está contido dentro do outro<br>
operador + -> concatenar string<br>
format e {} -> substitui valores<br>

"""

faturamento = 1000
custo = 500
lucro = faturamento - custo

"""Uso do str() e do concatenar com +"""

print ('O faturamento da loja foi de: ' + str(faturamento))

"""Uso do Format"""

print(f'O faturamento foi de: {faturamento}')
#ou
print('O faturamento foi de: {} e o custo foi de: {}'.format(faturamento, lucro))



"""Uso do in (mais exercícios práticos nas próximas aulas)"""

print('@' in 'lira@gmail.com') #return true or false 
print('@' in 'lira.gmail.com') 
