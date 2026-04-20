#exemp_08: Cashback do E-commerce (Sobrecarga de Operadores)
#Cenário: Uma loja quer gerar uma barra de progresso visual para o cashback do cliente.
#OBJETIVO: O cliente ganhou 10 pontos. Cada ponto vale um caractere █.

#Desafio: Crie a barra de progresso usando "multiplicação de strings" e concatene com a posrcentagem final.

#Saída esperada: Progressão: [██████████] 100% (Use o + para colar os textos).  

pontos = 10
ponto_barra_progressao = "█"
porcentagem = "100%"

#Relacionando os conceitos para o python saber lidar
barra_visual = ponto_barra_progressao * pontos

#concatenação, nesse caso (com +)  na outra linha tem a versao concatenada (sem +)
#barra_final = "Progressão: [" + barra_visual+ " ] ]" + porcentagem
#print(barra_visual)
print("\n" * 1)
#interpolada ficaria:
barra_final = f"Progressão:[{barra_visual}] {porcentagem}"
print(barra_final)

print("-" * 30)
print("\n" * 2)

