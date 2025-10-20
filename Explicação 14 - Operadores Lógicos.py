# Operadores Lógicos
# and, or, not

var_1 = 3
var_2 = 6
var_3 = 9

print('Variável 1:', var_1, 'Variável 2:', var_2, 'Variável 3:', var_3)
print()

print('var_1 é maior do que var_2 E var_2 é maior que var_3',
      var_1 > var_2 and var_2 > var_3)
print()

print('var_3 é maior do que var_2 E var_2 é maior que var_1',
      var_3 > var_2 and var_2 > var_1)
print()

# OR
print('var_2 é maior do que var_1 OU var_2 é maior que var_3',
      var_2 > var_1 or var_2 > var_3)
print()

# not
print(not(False), '\n')
print(not(True), '\n')
print(not(1 == 2))
