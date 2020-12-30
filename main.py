import time as t
print()
print("Calc! - Calculadora Online para todas as coisa.")
print()

print("Matemática")
print("    [1] Equação do 1º Grau")
print("    [2] Equação do 2º Grau")
print("    [3] Área do Quadrado")
print("Física")
print("    [4] Velocidade Média")
print("    [5] Movimento Uniforme")
print("    [6] Equação de Torricelli")

print()

escolha = input("Escolha a equação desejada: ")
print()

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

def funcao_1_grau():
    if a == "" and b != "" and x != "":
        print(f"x.{x} + {b} = 0")
        print(f"x.{x} =  -{b}")
        print(f"x = {int(b) / int(x)}")

    elif a != "" and b == "" and x != "":
        print(f"{a}.{x} + b = 0")
        print(f"{a}.{x} = - b")
        print(f"{a}.{x} = {- (int(a) * int(x))}")
    elif a != "" and b != "" and x == "":
        print(f"{a}.x + {b} = 0")
        print(f"{a}.x =  -{b}")
        print(f"x = {int(b) / int(a)}")

    elif a != "" and b != "" and x != "":
        print(f"{a}.{x} + {b} = 0")
        print(f"{int(a) * int(x)} + {b} = 0")
        print(f"{int(a) * int(x) + int(b)} = 0")
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


