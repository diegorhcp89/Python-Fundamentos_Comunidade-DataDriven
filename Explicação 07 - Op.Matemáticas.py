# Operações matemáticas
import os
os.system('cls')

valor_a = 37
valor_b = 32

print('Variaveris - A:', valor_b, 'B:', valor_b)
print('Somar:', valor_a + valor_b)
print('Subtrair', valor_a - valor_b)
print('Multiplicar:', valor_a * valor_b)
print('Elevar a uma potência:', valor_a ** valor_b)
print('Dividir:', valor_a / valor_b)
print('Divir truncando:', valor_a // valor_b)
print('Resto de uma divisão (MOD):', valor_a % valor_b )

# Prioridade das operações
print('Resultado 1:', -7 * (6 + 2) ** 2)
print('Resultado 2:', (-7 * 6+ 9 ** 2))

valor_a = 5
valor_b = 4
valor_c = 3
valor_d = 2

print('Média', (valor_a + valor_b + valor_c + valor_d) / 4)

# Operadores Incrementais
valor_inicial = valor_a

# Somar n valores ao valor principal da variáveis
# +=
valor_inicial = valor_inicial + 1
print(valor_inicial)

valor_inicial += 100
print(valor_inicial, '\n')

valor_inicial -= 10
print(valor_inicial, '\n')

valor_inicial *= 10
print(valor_inicial, '\n')

valor_inicial /= 2
print(valor_inicial, '\n')

print()