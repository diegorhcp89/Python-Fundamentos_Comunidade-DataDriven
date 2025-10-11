# Instrução print
# Saída dos scripts no terminal

# Saída de texto
print()
print("Olá, mundo!")
print('Olá, mundo!\n')

# Operações matemáticas
print(2 + 100 + 8 + 900)
print('Resultado:\t' + str(2 + 100 + 8 + 900))
print('Resultado:\t', 2 + 100 + 8 + 900)
print('A', 'B')

# f-string
valor_1 = 100
valor_2 = 200
resultado = valor_1 + valor_2
print(f'Resultado: {resultado}')

# raw-string
print(r'c:\temp')

# substituição com o símbolo de %
print('Resultado da substituição:\n%d' % (resultado))

# Parâmetros (finalização de linha = end)
texto = 'Olá, mundo!'
print(texto, end='|')
print(texto, end='\n')
print(texto, end='')
print()

# Parâmetros (separador = sep)
print('Resultado:', valor_1 + valor_2, '\n', sep='|')
print('NOMES: Karine e Letícia', 'COMUNIDADE:DataDriven', 
      'CURSO: Python Fundamentos\n', sep='\n')

# Tabulador
print('Curso\tde\tPython', '\n', 
      'Mat.\t06\t- Tabuladores', '\n',
      'Mat.\t07\t- Comentários', sep='')
