for x in range (5):
        print(x)
    
    #x começa valendo 0 e para quando chegar a 5
    
    #lopping de x de 0 a 4
    
#======================================

#PARA UM LOOPPING QUE RODASSE 300 VEZES SERIA:

notas = []

for x in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    print("Quantidade de notas", len(notas)) #len = lenght tamanho
    
    for n in notas:#ira repetir a quantidade de vezes que notas possuir de possuir de posições
        codigo_aluno = n[0] #neste caso n esta pegando o valor da posição 0 da lista notas
        nota = n[1]
        print("O RM", codigo_aluno, "tirou a nota:", nota)