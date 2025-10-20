# Operadores Relacionais
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != diferente
# == igual
print('\033c')

valor_a = 20
valor_b = 200
valor_c = 30

print('Valor A:', valor_a, 'Valor B:', valor_b,'Valor C:', valor_c)
print()

print('b é maior que a?', valor_b > valor_a, '\n')
print('b é maior que c?', valor_b > valor_c, '\n')
print('c é igual a 20:', valor_c == 10, '\n')
print('c é maior ou igual a b?', valor_c >= valor_b, '\n')
print('a é diferente de 20?', valor_a != 20, '\n')

# Estrutura de decisão
# if (se)
if valor_a > valor_c:
    print('A é maior que C') # True
else:
    print('C é maior que A') # False

print()
