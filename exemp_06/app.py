#exemp_06: O Checkout do Hotel (Módulo e Divisão Inteira)
#Cenário: Um hotel cobra por diárias de 24 horas. Um hóspede ficou 80 horas no hotel.
#Objetivo: Transforme essas horas em "Dias" e "Horas restantes" para o extrato.
#Dica: Use // para os dias e % para as horas que sobram.
# Saída esperada: "O Hóspede ficou X dias e Y horas." 

print("\n" * 1)

horas_hospede = 80
dias = horas_hospede // 24 #divisao precisa ser inteira
horas_restantes = horas_hospede % 24

print("-" * 30)
print("EXTRATO DA ESTADIA: ")
print(f"O hópede ficou {dias} dias e {horas_restantes} horas.")
