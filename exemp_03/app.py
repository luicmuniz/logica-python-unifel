#sobrecarga de operadores
print(int("10")+5)
print(str(10)+"5")

#Repetição
print("A" * 3)

minha_lista = [1,2]

print([1, 2] * 3)

print((10, 20) * 2)


#Pertencimento
print("a" in "banana") #true - a existe no objeto banaba?
print(4 in [4, 5, 6, 7]) #true - 4 existe na lista?
print("\n\n")
#print("abacate" * 2.5) #multiplicacao so funciona com numero int
#print("jorge" - "dantas") #str não se subtrai

def minha_função():
    print("Olá, sou uma função!")
    idade = 37
    print(f"A minha idade é: {idade} ")

print(minha_função())

print("\n\n")


a = 10
b = 30

a = b
b = 40

print(f"Aqui é a: {a}")
print(f"Aqui é a: {b}")
