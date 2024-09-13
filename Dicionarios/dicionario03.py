# dicionario = {}

# dicionario[chave] = valor

# outra opção:

# dicionario.update({chave: valor, chave: valor})

lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
#adicionando 1 item
lucro_1tri['abril'] = 88000
print(lucro_1tri)

#adicionando vários itens ou um dicionário a outro
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

#adicionando um item já existente (manualmente ou pelo update)

# - Modificar itens:
# Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.
# dicionario[chave] = valor

# Vamos modificar o lucro de fevereiro:
# (Lembrando: caso o item não exista, ele vai criar o item no dicionário)

lucro_fev = 85000
lucro_1tri['fevereiro'] = lucro_fev

# - Remover itens:
# del dicionario[chave]
# ou então
# valor = dicionario.pop(chave)

# mas cuidado com:s
# del dicionario    ->    que é diferente de dicionario.clear()

#removendo o mês de junho
del lucro_1tri['junho'] 

#ou 

lucro_jun = lucro_1tri.pop('junho') #pop retorna o que foi removido

print(lucro_1tri)
#obs: o del também funciona para listas, caso queira usar
#del lista[i]
funcionarios = ['João', 'Lira', 'Maria', 'Ana', 'Paula']