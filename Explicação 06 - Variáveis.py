# Tipos primitivos de dados em Python
# int      | Inteiro
# float    | Real / Ponto Flutuante
# bool     | Booleano (True, False)
# complex  | Tipo complexo
# string   | Alfanuméricos

# Variáveis de texto
texto = 'Curso de Python Fundamentos'  # Atribuição x Comparação
print(texto)
print('Tipo:', type(texto), '\n')

# Atribuir valores
var_a = 99
var_b = 4.5763
var_c = False  # falso
var_d = 2+9j
var_e = 'Python'

print(var_a, var_b, var_c, var_d, var_e)
print(type(var_a), type(var_b), type(var_c), type(var_d), type(var_e), sep='\n')

# Conversão de tipos
var_f = float(var_a)
print('A conversão de int para float:', type(var_f), var_f, '\n')

var_g = int(var_b)
print('Conversão de float para int:', type(var_g), var_g, '\n')

# Variáveis boolenas
var_h = False
var_i = True

print(var_h, var_i)
print(not(var_h), not(var_i))
