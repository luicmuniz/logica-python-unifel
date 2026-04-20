#Exemp. sinal de transito
# sinal = "vermelho"

# if sinal == "verde": 
#     print("SIGA")

# elif sinal == "amarelo"
#     print("SIGA")

# else:
#     print("PARE!")

    # Validação de faixa de idade
# idade = int(input("Digite a sua idade: "))
# if idade < 18:
#         print("Você é menor de idade! ")
# elif 18 <= idade <= 20:
#         print("Você é maior de idade (Jovem, acabou de sair da adolescência)")
# elif 21 <= idade <= 29:
#         print("Você é um jovem adulto")
# elif 30 <= idade <= 45:
#         print("Parabéns! Você está maduro")
# elif 46 <= idade <= 64:
#         print("Comemore! Você é uma pessoa na terceira dade")
# else:
#         print("Você é um idoso! \n Coroa, já anda de graça no buzu!! =)")   

#IF TERMINARIO - MAS SÓ SERVE PARA CONDIÇÃO SIMPLES, NESSE CASO SO PEDE MAIOR DE 18

# if idade > 18:
#     status = "Pode entrar"
# else:
#     status = "acesso Negado"

# #EM UMA LINHA SÓ FICA:
# status = "Pode entrar" if idade >18 else "Acesso Negado"    

#ARMADILHA DO IF => ELE PARA NA PRIMEIRA VERDADE
#EX. ERRADO
if idade >= 18:
    print("Adulto")
elif idade >= 65:
    print("Idoso") #NUNCA SERÁ TESTADO SE A IDADE FOR MAIOR QUE 18
#EX. CERTO
if idade >= 65:
    print("Idoso")
elif idade >= 18:
    print("Adulto")