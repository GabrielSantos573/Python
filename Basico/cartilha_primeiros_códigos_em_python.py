
#Cartilha - Primeiros Códigos em Python.ipynb

### Operações Básicas com String

#1. Concatenar -> +
#2. Verificar se um texto está contido dentro do outro -> in


#Concatenar
print('O faturamento da loja foi ' + '1000')

#Verificar se um texto está dentro do outro
print('@' in 'lira@gmail.com') #retorna true or false


### Pegar informações do Usuário

#para cadastrar um cliente
cpf = input('Digite seu cpf (apenas números, sem pontos e traços)') #input aceita texto
print('O cpf do cliente é ' + cpf)