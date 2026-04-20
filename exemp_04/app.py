from decimal import Decimal

#Operadores básicos

print(f"Soma: 10 + 3 = {10 + 3}")
print(f"Potência: 2^3 = {2 ** 3}")
print(f"Divisão Float: 10 / 3 = {10 / 3}")
print(f"Divisão Inteira (Truncado): 10 // 3 = {10 // 3}")
print(f"Resto da Divisão (Módulo): 10 % 3 = {10 % 3}")

#Sobrecarga de operadores
print("-" * 30)

print(f"FLOAT 0.8 + 0.1 = {0.8 + 0.1}")
print("\n\n")
valor_decimal1 = Decimal("0.8")
valor_decimal2 = Decimal("0.1")

print(f"DECIMAL 0.8 + 0.1 = {valor_decimal1 + valor_decimal2:.15f}")