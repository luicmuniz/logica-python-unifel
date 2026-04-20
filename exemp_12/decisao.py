
#CASO. 1 - SIMULAR SISTEMA QUE CONTROLA O ACESSO A UM EVENTO DA UNIFEL

# convidados = ["luic", "jorge", "genaldo", "denis"]
# usuario = input(" Digite seu nome: ").lower()

# if usuario in convidados:
#     print("LIBERADO! Seja bem-vindo ao evento!")

#     #Aninhamento => um if dentro do outro
#     idade = int(input("Qual a sua idade: "))
#     if idade >= 18: 
#         print("Você recebeu uma pulseira VIP \n")
#     else:
#         print("Você recebeu uma pulseira da área KIDS (infantil)! \n")
# else:
#     print("ACESSO NEGADO. Seu nome não consta na lista. Procure a recepção! ")
# print("-" * 30)


#CASO. 2 CLASSIFICAR DO CLIMA DO EVENTO
# print("\n" * 2)
# temp = float(input("Digite a temperatura da sala: "))
# status = None
# if temp > 35:
#     status = "Calor extremo no salão \n"
# elif 25 <= temp <= 35: #ENCADEAMENTO LOGICO -> TEMP >= 25 AND TEMP <= 35
#     status = "Suportável"
# elif 17 <= temp<= 24:
#     status = "Agradável"
# else:
#     status = "Muito frio" #16 pra baixo
#     print(f"A temperatura está: {temp} (16 ou abaixo)!! \n")
# print(f"O clima está: {status} ({temp}°)!! \n")
 
# CASO 3 MENU DE COMANDOS DA GESTÃO DO EVENTO
opcao = input("Escolha uma opção: A (Relatório) | B (Saldo) | C (Sair): ").upper()
# math é parecido com if

match opcao:
    case "A":
        print("GERANDO RELATÓRIO DETALHADO DO EVENTO... \n")
    case "B":
        print("Calculando a receita consolidada atual do evento... \n")
 
    case "C":
        print("Saindo do sistema... Até logo! \n")


