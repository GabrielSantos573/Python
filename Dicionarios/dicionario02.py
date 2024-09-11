mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# - Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves
# - 2 formas de pegar um valor:
#     - dicionario[chave] / retorna erro
#     - .get(chave) / get retorna none

# - Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
# - Quanto foi vendido de 'notebook asus' e de 'ipad'?

#com get
print(vendas_tecnologia.get('notebook asus'))
print('Vendemos {} ipads'.format(vendas_tecnologia.get('ipad')))

### Verificar se item está no dicionário:

# - if
# - .get(chave) = None

# Se tentarmos procurar as vendas de "copo" na lista de vendas tecnologia, o que acontece?

if 'copo' in vendas_tecnologia: #ele verifica as chaves e não os valores
    print(vendas_tecnologia['copos'])
else:
    print('Copos não esta no dicionario')
    
#ou

if vendas_tecnologia.get('copo') == None:
    print('Copos não esta no dicionario')
else:
    print(vendas_tecnologia.get('copo'))