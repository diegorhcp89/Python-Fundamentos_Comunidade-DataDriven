# Operadores de Associação
# in e not in
# Função range
print('\033c')

# Função range: serve para gerar uma sequência de números
faixa_valor = range(1, 6)
print(type(faixa_valor))

for valor in faixa_valor:
    print(valor)

print('\n')

print('********** Operador In **********\n')
print('1 está na faixa_valores........:', 1 in faixa_valor, '\n')
print('99 esta na faixa_valores.......:', 99 in faixa_valor, '\n')
print('1 e 3 estão na faixa?..........:', 1 in faixa_valor and 3 in faixa_valor, '\n')
print()

print('********** Operador Not In **********\n')
print('1 não está na faixa_valores........:', 1 not in faixa_valor, '\n')
print('99 não esta na faixa_valores.......:', 99 not in faixa_valor, '\n')
print('1 e 3 não estão na faixa?..........:', 1 not in faixa_valor and 60 in faixa_valor, '\n')
print()
