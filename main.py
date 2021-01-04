import time as t

from tratativa_erros import trativa_erros

from funcao_1_grau import funcao_1_grau

from velocidade_media import velocidade_media

from conversao_base import conversao_base

print('''Calc! - Calculadora Online para todas as coisa.''')

print('''
Matemática
    [1] Equação do 1º Grau
    [2] Equação do 2º Grau

Física
    [3] Velocidade Média

Conversão
    [4] Conversão de Base (Binário, decimal e hexacimal)
    [5] Conversão de Temperatura (C, F, K)
    ''')

escolha = input('Escolha a equação desejada: ')

# Função com papel de loading
def carregando():
    print()
    print('Carregando...')
    print()

if escolha == '1':
    print('''
    Exemplo: ax + b = 0
    Obs: Apenas um valor em branco
        ''')
    a = input('Digite o a: ')
    b = input('Digite o b: ')
    x = input('Digite o x: ')

    validacao = trativa_erros(a, b, x)

    if not validacao:
        carregando()
        funcao_1_grau(a, b, x)
    else:
        print("Digite um caractere válido!")

elif escolha == '3':
    print('''
    Exemplo: v = s / t
    Obs: Apenas um valor em bran4co
            ''')

    v = input('Digite o v: ')
    s = input('Digite o s: ')
    t = input('Digite o t: ')

    validacao = trativa_erros(v, s, t)

    if not validacao:
        carregando()
        velocidade_media(v, s, t)
elif escolha == '4':
    n = int(input('Digite um numero qualquer: '))

    validacao = n == ''

    if not validacao:
        carregando()
        conversao_base(n)
else:
    print('Por favor, escolha uma opção válida!')


