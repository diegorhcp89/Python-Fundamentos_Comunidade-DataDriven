# Listas são estruturas de dados que permitem armazenar
# múltiplos valores em um única variável.
# Também conhecida como array ou coleção
# Mutável
# criada com o uso [ ]

print('\033c')

lista_vazia = []
print(type(lista_vazia))
print()

minha_lista = ['Comunidade', 'Data', 'Driven', 'Python', 'Fundamentos', 1000]
print(minha_lista, '\n')
print('Tamanho', len(minha_lista), '\n')

# Unificar
minha_lista_2 = ['Valor_1', 'Valor_2']
minha_lista_unida = minha_lista + minha_lista_2
print(minha_lista_unida)

# Duplicar lista
minha_lista_3 = minha_lista_2 * 4
print(minha_lista_3)

# Acesso de elementos
print(minha_lista_unida[1])
print(minha_lista_unida[2:])
print(minha_lista_unida[1:3])
print(minha_lista_unida[:2])
print(minha_lista_unida[-1])