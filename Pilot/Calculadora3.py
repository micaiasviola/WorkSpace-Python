from os import system


try:
    system('cls')
    print("Soma de n1 + n2")

    n1 = int(input("Digite n1: "))  # Captura o valor de n1
    n2 = int(input("Digite n2: "))  # Captura o valor de n2
    soma = n1 + n2


print(f"O valor é {soma}")  # Exibe a soma


except ValueError:
    print("Apenas numeros!")
