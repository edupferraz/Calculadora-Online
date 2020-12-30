import time as t

print('''Calc! - Calculadora Online para todas as coisa.''')

print('''
Matemática
    [1] Equação do 1º Grau
    [2] Equação do 2º Grau
    [3] Área do Quadrado
Física
    [4] Velocidade Média
    [5] Movimento Uniforme
    [6] Equação de Torricelli
    ''')

escolha = input("Escolha a equação desejada: ")
print()

# Função com papel de loading
def carregando():
    print("Pro")
    t.sleep(0.5)
    print("ce")
    t.sleep(0.5)
    print("ssan")
    t.sleep(0.5)
    print("do !!!!!")
    t.sleep(0.5)
    print()

# Função responsável pela resolução da função do 1º grau
def funcao_1_grau():

    # Se a for a variável
    if a == "" and b != "" and x != "":
        print(f"x.{x} + {b} = 0")
        print(f"x.{x} =  -{b}")
        print(f"x = {int(b) / int(x)}")

    # Se b for a variável
    elif a != "" and b == "" and x != "":
        print(f"{a}.{x} + b = 0")
        print(f"{a}.{x} = - b")
        print(f"{a}.{x} = {- (int(a) * int(x))}")

    # Se x for a variável
    elif a != "" and b != "" and x == "":
        print(f"{a}.x + {b} = 0")
        print(f"{a}.x =  -{b}")
        print(f"x = {int(b) / int(a)}")

    # Se todos os campos forem preenchidos
    elif a != "" and b != "" and x != "":
        print(f"{a}.{x} + {b} ")
        print(f"{int(a) * int(x)} + {b}")
        print(f"{int(a) * int(x) + int(b)}")
    else:
        print("Digite parâmetros válidos")

# Função responsável pela resolução da velocidade média
def velocidade_media():

    # Se a for a variável
    if v == "" and s != "" and t != "":
        print(f"v = {s} / {t}")
        print(f"v = {int(s) / int(t) }")

    # Se b for a variável
    elif v != "" and s == "" and t != "":
        print(f"{v} = s / {t}")
        print(f"{v} . {t} = s")
        print(f"{int(v) * int(t)} = s")

    # Se x for a variável
    elif v != "" and s != "" and t == "":
        print(f"{v} = {s} / t")
        print(f"{v} . {s} = t")
        print(f"{int(v) * int(s)} = t")

    # Se todos os campos forem preenchidos
    elif v != "" and s != "" and t != "":
        print(f"{v} = {s} / {t}")
        print(f"{v} = {int(s) / int(t) }")
    else:
        print("Digite parâmetros válidos")

if escolha == "1":
    print("Exemplo: ax + b = 0")

    a = input("Digite o a: ")
    b = input("Digite o b: ")
    x = input("Digite o x: ")

    print()
    carregando()

    funcao_1_grau()

elif escolha == "4":

    print("Exemplo: v = s / t")
    print("Obs: Apenas um valor em branco")
    print()

    v = input("Digite o v: ")
    s = input("Digite o s: ")
    t = input("Digite o t: ")

    print()
    # carregando()
    velocidade_media()



