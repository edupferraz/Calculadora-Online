
def velocidade_media(v, s, t):
    # (s and t) != '' -> Outra forma possível

    # Se a for a variável
    if v == '' and s and t != ''  and t != '':
        print(f'v = {s} / {t}')
        print(f'v = {int(s) / int(t) }')

    # Se b for a variável
    elif v != '' and s == '' and t != '':
        print(f'{v} = s / {t}')
        print(f'{v} . {t} = s')
        print(f'{int(v) * int(t)} = s')

    # Se x for a variável
    elif v != '' and s != '' and t == '':
        print(f'{v} = {s} / t')
        print(f'{v} . {s} = t')
        print(f'{int(v) * int(s)} = t')

    # Se todos os campos forem preenchidos
    elif v != '' and s != '' and t != '':
        print(f'{v} = {s} / {t}')
        print(f'{v} = {int(s) / int(t) }')
