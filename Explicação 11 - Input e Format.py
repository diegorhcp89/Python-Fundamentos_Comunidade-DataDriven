# Input - Obter
print('\033c')

# math
import math

var_nome = input('Digite o seu nome: ')
print('Olá, ', var_nome, '\n')

print('Área de uma circunferência\n')

var_raio = input("Informe o raio da circunferência: ")
var_resultado = math.pi * float(var_raio) ** 2

print('Área: ', var_resultado)
print('Comprimento:', 2 * math.pi * float(var_raio))
print()

# Format

var_texto = '{0}, seja bem-vindo(a)'
print(var_texto.format(var_nome), '\n')

var_idade = 39
var_profissao = 'Analista de sistemas'
var_mensagem = '{0}, seja bem-vindo(a)! \nIdade1/ {1} \nProfissão: {2}'
print(var_mensagem.format(var_nome, var_idade, var_profissao))

# Formatação do resultado
print('Área: ', round(var_resultado))
print('Comprimento:', round(2 * math.pi * float(var_raio)))
print()

mensagem = '\nÁrea: {0:.1f}'
print(mensagem.format(var_resultado))