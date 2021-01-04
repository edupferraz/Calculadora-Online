
def conversao_base(n):
    print('''    [1] Conveter para binário
    [2] Converter para octal
    [3] Converter para hexadecimal
    ''')
    opcao = int(input('Escolha umas das opções de conversão '))
    print()
    
    if opcao == 1:
        print('O número {} corresponte a {} em binário'.format(n,bin(n)[2:]))
    elif opcao == 2:
        print('O número {} corresponde a {} em octal'.format(n,oct(n)[2:]))
    elif opcao == 3:
        print('O número {} corresponde a {} em hexadecimal'.format(n,hex[2:](n)))
    else:
        print('Opção invalida tente novamente')