
def funcao_1_grau(a, b, x):
    # Se a for a variável
    if a == '' and b != '' and x != '':
        print(f'x.{x} + {b} = 0')
        print(f'x.{x} =  -({b})')
        print(f'x = {int(b) / int(x)}')

    # Se b for a variável
    elif a != '' and b == '' and x != '':
        print(f'{a}.{x} + b = 0')
        print(f'{a}.{x} = - (b)')
        print(f'{a}.{x} = {- (int(a) * int(x))}')

    # Se x for a variável
    elif a != '' and b != '' and x == '':
        print(f'{a}.x + {b} = 0')
        print(f'{a}.x =  - ({b})')
        print(f'x = {int(b) / int(a)}')

    # Se todos os campos forem preenchidos
    elif a != '' and b != '' and x != '':
        print(f'{a}.{x} + {b} ')
        print(f'{int(a) * int(x)} + {b}')
        print(f'{int(a) * int(x) + int(b)}')
