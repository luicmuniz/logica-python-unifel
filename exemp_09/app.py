#exemp_11: A Herança Dividida (Divisão e Resto Real)
#Cenario: Um investidor deixou 1.000 barras de ouro para 7 herdeiros.
#O que não puder ser dividido igualmente (a sobra) deve ser doado para um museu.
#Objetivo: Calcule quantas barras cada herdeiro recebe e quantas barras serão doadas.

#Saída esperada: "Herdeiros: X barras cada. Museu: Y barras"

total_barras = 1000
herdeiros = 7
#Quanto cada herdeiro recebe
barra_por_herdeiro = total_barras // herdeiros

#Sobra do museu
doacao_museu = total_barras % herdeiros

# print("PARTILHA: ")
# print(f"HERDEIROS: {barra_por_herdeiro} barras para cada!")
# print(f"MUSEU (doação): {doacao_museu} barras")


# CURTO CICUITO
# print(False and print("Olá"))
# print(True or print("Oi"))


# resultado = 10 > 5
# print(resultado)

#Ex. 1
# nome_user = ""
# login = nome_user or "visitante" #OU retorna o verdadeiro da expressão 
# print(login)

#Ex. 2
# user_ativo = True
# permissao_adm = "Acesso Total"
# status = user_ativo and permissao_adm
# print(status) #resultado="Acesso total" => pegou a true mais significativa


#Ex. 3
cupom_desconto = 0
desconto_padrao = 5.0

# valor_deconto = cupom_desconto or desconto_padrao
# print(f"Desconto aplicado: {valor_deconto} \n")

#Ex. 4
resultado = "Conexão OK!" and 0.1 and "Dados recebidos"
print(resultado) #resultado= 0, pois 0 é falso, ele encerra na primeira expressão e retorna 0, 
#mesmo sendo Falso ele o 0 precede a string 

#Ex. 5
config_servidor = ""
server_padrão = "192.168.1.100"
server_ativo = config_servidor or server_padrão
print(server_ativo) 

#resumo
# Use and para condições de segurança, prevenção de erro
# filtro de acesso (autorização) validação em cadeia

#or use para ter um plano B (um valor que sera usado caso o outro não sirva),
# uma alternativa que funcione, quando vc precisa ter um valor padrão.
