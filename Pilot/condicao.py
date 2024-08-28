# idade = int (input("informe sua idade: "))

# if idade >= 18:
#     print("Maior de idade! Permitido")
# else:
#     print("Menor de idade! Bloqueado")

salario = float(input("Informe o salario: "))

if salario <= 3000:
    print("Programador junior")
elif salario > 3000 and salario <=6000:
    print("Programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador senior")
else: 
    print("gerente de projetos")
    
    # elif é igual ao else if{}
    #em python nao se usa ponto e virgula, em alguma funcoes como if else se usa : 
    #para executar o bloco de codigo e não precisa de chaves, apenas os parenteses#
    #necessarios para o codigo
    
    
    