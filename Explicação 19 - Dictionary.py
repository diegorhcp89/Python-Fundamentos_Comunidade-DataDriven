# Dicionário ou Dictionary
import os
os.system('cls')

dicionario_a = {
    1: 'Data',
    2: 'Driven'
}
print(type(dicionario_a))

# Qtd elementos
print('Tamanho', len(dicionario_a))

# Adicionar elementos
dicionario_a[3] = "Comunidade"
dicionario_a[4] = 'Python'
print(dicionario_a)

# Update
dicionario_a.update({1:'Fundamentos'})
print(dicionario_a, '\n')

# Apagar intens
del(dicionario_a[1])
print(dicionario_a, '\n')

# Elementos
print('Keys (chaves):', dicionario_a.keys())
print('Keys (itens):', dicionario_a.items())
print('Values (valores):', dicionario_a.values())
print()