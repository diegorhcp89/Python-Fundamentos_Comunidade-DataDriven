# Método é um procedimento que pode manipular atributos de objetos para qual
# o método foi chamado.
print('\033c')

texto_exemplo = 'Python Fundamentos'
print(type(texto_exemplo), '\n')
print(texto_exemplo.capitalize(), '\n')

# Concatenar (juntar) textos
texto_1 = 'Curso'
texto_2 = 'Python'
texto_3 = 'Fundamentos'

resultado = texto_1 + ' ' + texto_2 + ' ' + texto_3
print(resultado)
print('Conversão para Maiúscula:', resultado.upper(), '\n')

var_a, var_b = 100, 200
print('Resultado:' + str(var_a + var_b))

# Preenchimento de caracteres

# Tamanho de uma string
print('Tamanho do texto:', len(resultado), '\n')

qtd = 75

# 50 caracteres
print(resultado.ljust(qtd, '.'))
print(resultado.ljust(qtd, '-'))
print(resultado.ljust(qtd, ' '))
print()

print(resultado.rjust(qtd, '.'))
print(resultado.rjust(qtd, '-'))
print(resultado.rjust(qtd, ' '))
print()

print(resultado.center(qtd, '.'))
print(resultado.center(qtd, '-'))
print(resultado.center(qtd, ' '))
print()