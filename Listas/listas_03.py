"""Listas 03.ipynb

# Como descobrir o índice de um item de uma lista?

i = lista.index('item')

Exemplo:

Digamos que você puxou do Banco de Dados da sua empresa uma lista com todos os produtos que a empresa vende e a quantidade em estoque de todos eles.
"""

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

"""Nesse caso a lista é "pequena" para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.

E agora, como eu faço para descobrir a quantidade em estoque do produto geladeira?
"""



"""Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto"""

produto = input("Insira o nome do produto : ")

if produto in produtos:
    i = produtos.index(produto)
    qtdEstoque = estoque[i]
    print(f'Temos {qtdEstoque} de {produto} no estoque')
else:
    print(f'{produto} não encontrado na lista')


