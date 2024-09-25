from os import system


def switch_case(case):
    if case == 1:
        return "Você escolheu a opção 1."
    elif case == 2:
        return "Você escolheu a opção 2."
    elif case == 3:
        return "Você escolheu a opção 3."
    elif case == 4:
        return "Você escolheu a opção 4."
    else:
        return None


try:

    system('cls')

    print("1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão")

    escolha = int(input("Escolha uma opção: "))
    resultado_escolha = switch_case(escolha)
    if resultado_escolha is None:
        print("Opção invalida")
    else:
        n1 = float(input('Insira n1: '))

        n2 = float(input('insira n2: '))

        if escolha == 1:
            print("Soma", n1 + n2)
        elif escolha == 2:
            print("Subtração", n1 - n2)
        elif escolha == 3:
            print("Multiplicação", n1 * n2)
        elif escolha == 4:
            print("Divisão", n1 / n2)


except ValueError:
    print("Por favor, insira um número válido.")
