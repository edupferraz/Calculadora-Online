
def trativa_erros(a, b, c):

    e_vazio = (a == '' and (b == '' or c == '')) and (b == '' and c == '') and (a == '' and b == '' and c == '' )

    if e_vazio:
        print()
        print("Deixe apenas uma variável")
        exit()

    return e_vazio