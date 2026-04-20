# ANALISADOR DE TRIANGULO: RECEBA TRÊS LADOS (A, B, e C) DE UM POSSÍVEL TRIÂNGULO, DETERMINE SE 
#REGRA DE EXISTENCIA: UM TRIANGULO SO EXISTE SE A SOMA DE DOIS LADOS FOR SEMPRE MAIOR QUE O TERC
#SE (E SOMENTE SE) O TRIANGULO EXISTIR, CLASSIFICAR O TIPO COM BASE NA IGUALDADE DOS LADOS.
#EQUILATERO: TODOS OS TRES LADOS SAO IGUAIS
#ISOSCELES: APENAS 2 LADOS SAO IGUAIS.
#ESCALENO: TODOS OS 3 LADOS SAO DIFERENTES.

#OBS. LADOS DE UM TRIANGULO JAMAIS PODEM SER 0 OU NUMERO NEGATIVO!!!

print("-" * 30)
print(f"{'ANALISADOR DE TRIÂNGULOS':^30}")
print("-" * 30)

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

#UM LADO DE TRIANGULO NAO PODE SER 0 OU NEGATIVO, LOGO: if a > 0 and b > 0 and c > 0
 #PARENTESES NAS SOMAS PRIMEIRO POIS PRECISA RESOLVER
        #A SOMA PRIMEIRO ANTES DE PARTIR PARA O and
#PRINT() => \\ O FIM DE todo PRINT() É UM "\n". O end+"" tinha essa quebra de linha

if a > 0 and b > 0 and c > 0:
    
    if (a + b > c) and (a + c > b) and (b + c > a): 
        print("Esse triângulo é válido! Classificação: ", end="")

        if a == b == c:
            print("Seu triângulo é EQUILÁTERO")

        elif a == b or a ==c or b == c:
         print("Seu triângulo é ISÓCELES")

        else:
          print("Seu triângulo é ESCALENO!")  

    
    else:
     print("Os lados informados não podem gerar um triângulo!!")
     print("MOTIVO: Um dos lados informados é maior que a soma dos outros dois lados! \n\n")
        
    

else:
    print("ERRO: Não existem triangulos com lados nulos ou negativos!! \n ")
