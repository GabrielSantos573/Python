vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):  #O enumerate nos retorna uma tupla mesmo usando listas./ O i, venda é o mesmo unpacking que vemos em tuplas01.py
        print('{} vendeu {} unidades'.format(funcionarios[i], venda))