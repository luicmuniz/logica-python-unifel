from decimal import Decimal
# exmp_05: O ingresso do festival (Básico: Operadores e F-Strings)
#Cenário: Você está organizando um festival de música.
#Um Cliente quer comprar 4 ingressos do setor VIP.
#Objetivo: Calcule o valor total da compra e exiba um recibo organizado.

#Preço VIP: R$ 450.00
#Taxa de conviniência por ingresso: R$ 35.00
#SUB TOTAL = Preço do VIP * qantidade
#TAXA TOTAL = Conveniencia * quantidade
#VALOR FINAL = Sub-Total + Taxa total

#Saída esperada: Um cabeçalho com "-" * 30, o subtotal, a taxa total e o valor final.

preco_vip = 450.00
taxa_conveniencia = 35.00
quant_ingressos = 4

#PROCESSAMENTO
sub_total = preco_vip * quant_ingressos #FLOAT
taxa_total = taxa_conveniencia * quant_ingressos #FLOAT
valor_final = sub_total + taxa_total #FLOAT + FLOAT
#SAÍDA (Recibo organizado)
print("\n" * 1)
print("-" * 30)

print(f" {"RECIBO DA COMPRA":^30} ") #'^ Centraliza em 30 de largura
print("-" * 30)
print(f"SUB-TOTAL: R$ {sub_total:>6.2F}")
print(f"TAXA TOTAL: R$ {taxa_total:>6.2F}")
print("-" * 30)
print(f"VALOR FINAL (TOTAL): R$ {valor_final:>6.2F}")

print("-" * 30)
print("\n\n" * 30)

#print("TIPOS DAS VARIÁVEIS COM NOSSAS CONTAS: ")
#print(type(sub_total))
#print(type(taxa_total))
#print(type(valor_final))
