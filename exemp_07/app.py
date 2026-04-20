#exemp_07: O Arquiteto de Piscinas (Potencia e Float)
#Cenario: Um arquiteto precisa calcular o volume de uma piscina cubica para decidir a bomba de filtragem
#Objetivo: Peça ao usuario (via imput) o lado do cubo em metros e calcule o volume em litros.

#Formula do Volume: Lado^3

#Conversão: 1m^3 = 1000 litros

#Saída esperada: "A piscina de lado "X"m suporta Y litros de água. "
print("\n" * 1)

lado_em_metros = input("Digite o tamanho do lado da piscina (metros): ")
lado = float(lado_em_metros.replace(",", ".")) #Método: quer dizer tanto faz virgla como ponto  
print(f"Lado da piscina (em metros) = {lado}")

# Formula so Volume: Lado^3
volume_metro_cubico = lado**3
volume_litros = volume_metro_cubico * 1000



print("-" * 30)
print(f"A piscina de lado {lado}m suporta {volume_litros} litros de água. ")
print("\n" * 2)

