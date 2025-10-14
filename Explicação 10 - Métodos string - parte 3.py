# Extração de texto
print('\033c')

texto = 'Curso de Python Fundamentos'

print(texto[0:5])
print(len(texto[0:5]))
print()

print(texto[9:])
print(texto[:5])

# Eliminar espaçpes desnecessários
var_texto_sujo = '          Curso de Python      '
print('Tamanho (antes):', len(var_texto_sujo))
print(var_texto_sujo.strip())
print('Tamanho (antes):', len(var_texto_sujo.strip()), '\n')

# join (junção)
var_texto_join = 'Python'
print('-'.join(var_texto_join))
print()
