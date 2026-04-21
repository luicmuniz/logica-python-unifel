# #exemp_xx (login): Crie duas variaveis user_db = "admin" e pass_db = "123".
# #Receba via input o usuario e senha e exiba True se ambos baterem.

# #exemp_x (Elegibilidade): Um eleitor só vota se tiver idade entre 16 e 70 anos. Receba do usuário
# #a idade, e então exiba True ou False para o candidato (teste candidatos com 15 anos, e também 
# # com 75 anos para ver se o código funciona).

# user_db = "admin"
# pass_db = "123"

# db_user = input("Digite p nome do user: ")
# password_db = str(input("Agora digite a senha: "))

# print(user_db == db_user and pass_db == password_db)

#MELHORAR O E MESMO EXERCICIO

#exemp_xx (login): Crie duas variaveis user_db = "admin" e pass_db = "123".
#Receba via input o usuario e senha e exiba True se ambos baterem.
#Exiba uma msg: "Login autorizado!!"  True?False
#Exiba uma msg personalizada: "Ben-vindo Administrador" ou "User ou Senha incorretos" para
#o caso de ser True ou False

#exemp_x (Elegibilidade): Um eleitor só vota se tiver idade entre 16 e 70 anos. Receba do usuário
#a idade, e então exiba True ou False para o candidato (teste candidatos com 15 anos, e também 
# com 75 anos para ver se o código funciona).

#print(user_db == db_user and pass_db == password_db)

# user_db = "admin"
# pass_db = "123"

# print("-" * 30)
# print(f" {'SISTEMA DE ACESSO':^30}")
# print("-" * 30)


# db_user = input("Digite p nome do user: ")
# password_db = str(input("Agora digite a senha: "))

# acesso_concedido = (user_db == db_user) and (pass_db == password_db)

# print(f"\n Login autorizado! {acesso_concedido}")
# print("-" * 30)

# msg_personalizada = acesso_concedido and "Ben-vindo Administrador" or "User ou Senha incorretos"

# print(f"STATUS LOGIN: {msg_personalizada}")

# print("-" * 30)


#Outro ex.


#(Sensor)Crie um sistema que exiba True se uma temperatura estiver
# entre 20 e 30 graus (faixa ideal). Receba a temperatura do usuário.

# print("-" * 30)
# print(f" {'SISTEMA DE ACESSO':^30}")
# print("-" * 30)

#temp = float(input("Digite a temperatura: "))

# if 20 <= temp <= 30:
#     print(f"Temperatura: {temp} => {20 <= temp <= 30}")



#EX. A mesma ideia mas usar o if, feito pelo aluno Wallace


# temp_user = float(input("Digite a temperatura: "))

# faixa_ideal = 20 <= temp_user <= 30
# temp_ideal = faixa_ideal and "A temperatura está na faixa ideal." or "A temperatura está fora da faixa ideal."

# print(temp_ideal)


#exemp_x (Elegibilidade): Um eleitor só vota se tiver idade entre 16 e 70 anos. Receba do usuário
#a idade, e então exiba True ou False para o candidato (teste candidatos com 15 anos, e também 
# com 75 anos para ver se o código funciona).

idade = int(input("Digite sua idade: "))

pode_votar = (16 <= idade <= 70 and "\n\n Você pode votar!" or "\n Candidato não elegível a voto.")

print(f"Candidato com {idade} anos!")
print(f"Pode votar! {pode_votar}")