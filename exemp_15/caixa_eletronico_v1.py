#Simulador de ATM (Caixa Eletronico): Peça um valor de saque. Verifique se o valor é multiplo do
#Se for, use a estrutura apropriada para simular a entrega de notas; se não for, avise que a máquina
# #OBS: Emitir o aviso "Saque de alto valor: Verifique o limite diário." caso o saque seja Maior que

valor_saque = int(input("Quanto vai sacar? (notas de 10, 20 e 50): "))

if valor_saque % 10 == 0:
    match valor_saque: 
        case 10:
            print("Entregando 1 nota de R$ 10,00...")
        case 20:
            print("Entregando 1 nota de R$ 20,00...")
        case 50:
            print("Entregando 1 nota de R$ 50,00...")
        case _ if valor_saque > 500:
            print("Saque de alto valor: Verifique o limite diário.")
            print(f"Sacando o valor de {valor_saque} reais")
        case _:
            print(f"Sacando o valor de {valor_saque} reais")

else:
    print("[ERRO]: Valor inválido!")
    print("Este caixa só trabalha com notas de 10,00 | 20,00 | 50,00")

print("-" * 30) 

