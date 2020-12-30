import time as t
print()
print("Calc! - Calculadora Online para todas as coisa.")
print()

print("Matemática")
print("    [1.1] Equação do 1º Grau")
print("    [1.2] Equação do 2º Grau")
print("    [1.3] Área do Quadrado")
print("Física")
print("    [2.1] Velocidade Média")
print("    [2.2] Movimento Uniforme")
print("    [2.3] Equação de Torricelli")

print()

escolha = input("Escolha a equação desejada: ")
print()

if escolha == "1.1":
    print("Exemplo: ax + b = 0")

    a = input("Digite o a: ")
    b = input("Digite o b: ")
    x = input("Digite o x: ")

    print()

    print("Pro")
    t.sleep(1)
    print("ce")
    t.sleep(1)
    print("ssan")
    t.sleep(1)
    print("do !!!!!")
    t.sleep(1)
    print()

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