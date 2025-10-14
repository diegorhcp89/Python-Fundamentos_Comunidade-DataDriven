# métodos para string
# parte 2
print('\033c')

# Alterar a caixa das palavras A/a
texto_exemplo = 'Curso Python Fundamentos'
texto_exemplo = texto_exemplo.upper().lower()
print(texto_exemplo)

# exit()

print('Resultado do método title:', texto_exemplo.title(), '\n')
print('Maiúsculas:', texto_exemplo.upper(), '\n')
print('Minúsculas:', texto_exemplo.lower(), '\n')
print('Inversão', texto_exemplo.swapcase(), '\n')

# Tamanho de uma string (len)
print('Tamanho', len(texto_exemplo), '\n')
print(len('Diego Amaral'))
