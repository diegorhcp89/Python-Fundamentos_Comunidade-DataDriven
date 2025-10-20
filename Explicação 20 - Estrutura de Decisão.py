# Estrutura de decisão
# if
print('\033c')

# Exemplo 1
qtd_estoque = 29

if qtd_estoque >= 150:
    # True
    print('Estoque está normal.', '\n')
else:
    # False
    print('Estoque está baixo', '\n')

# Exemplo 2
numero = float(input('Digite um número qualquer: '))

if numero < 0:
    print('O número digitado é negativo!')
elif numero == 0:
    print('O número digitado é zero!')
else:
    print('O número digitado é positivo')

print()

# Exemplo 3
numero = input('Digite um número qualquer: ')

if numero.lstrip('-').isdigit():  # aceita números negativos
    numero = int(numero)  # converte para inteiro

    if numero < 0:
        print('O número digitado é negativo!')
    elif numero == 0:
        print('O número digitado é zero!')
    else:
        print('O número digitado é positivo')
        
else:
    print('O número digitado é inválido!')

print()