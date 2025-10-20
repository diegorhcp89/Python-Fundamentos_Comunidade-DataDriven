minha_lista = ['Comunidade', 'Data', 'Driven', 'Python', 'Fundamentos']

# Verificar elementos da lista
print('Python' in minha_lista)
print('Python' not in minha_lista)
print('PYTHON' in minha_lista)
print()

# Operadores com listas
lista_numeros = [5, 11, 16, 19, 77, 55, 77, 43]
print('Mínimo:', min(lista_numeros))
print('Máximo:', max(lista_numeros))
print('Soma:', sum(lista_numeros))
print('Média:', sum(lista_numeros) / len(lista_numeros))

# Métodos para listas
# append
minha_lista.append('Fundamentos')
print(minha_lista)

# insert
minha_lista.insert(0, 'Treinamento')
print(minha_lista)

# pop - Apaga elementos da lista
minha_lista.pop()
print(minha_lista)

minha_lista.pop(1)
print(minha_lista)

# remove
minha_lista.remove('Treinamento')
print(minha_lista)

# sort - ordena em ordem crescente
# reverse - ordem inversa
minha_lista_2 = minha_lista.copy()
minha_lista_2.append('Treinamento')
print(minha_lista_2)

minha_lista_2.sort()
print(minha_lista_2)

minha_lista_2.reverse()
print(minha_lista_2)

print(minha_lista_2.count('Python'))

print()