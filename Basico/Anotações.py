
#Cartilha - Primeiros Códigos em Python.ipynb

### Operações Básicas com String

#1. Concatenar -> +
#2. Verificar se um texto está contido dentro do outro -> in


#Concatenar
print('O faturamento da loja foi ' + '1000')

#Verificar se um texto está dentro do outro
print('@' in 'lira@gmail.com') #retorna true or false

#para cadastrar um cliente

cpf = input('Digite seu cpf (apenas números, sem pontos e traços)') #input aceita texto
#cpf = int(input('Digite seu cpf (apenas números, sem pontos e traços)'))  -> pra definir o tipo

print(type(cpf))

print('O cpf do cliente é ' + cpf)

#Format 

codigo = 123

print("O codigo é {} teste".format(codigo)) 

#F-string

print(f"O codigo é {codigo} teste") 

"""Gabarito - Módulo if - Aula 04.ipynb

# Comparadores Python

in    texto existe dentro de outro texto 
not   verifica o contrário da comparação

Obs: Se em alguma condição você não quiser fazer nada, você pode simplesmente escrever:
pass

Exemplo:
    email_usuario = input('Insira seu e-mail:')
    if not '@' in email_usuario:
        print('Email Inválido')
    else:
        pass
"""

