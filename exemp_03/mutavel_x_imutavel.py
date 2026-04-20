#Imutáveis (Seguro)
x = 10
y = x

x = 20


#Mutáveis
lista_a = [1,2,3]
lista_b = lista_a
lista_a.append(4)

print(f"Mutáveis: LISTA A: {lista_a} | LISTA B: {lista_b}")
#Efeito espelho
print("\n\n")


#Verificando o enderço de memoria dos objetos
print(f" ID da lista A: {id(lista_a)} | ID da lista B:{id(lista_b)}")

print("\n\n")

lista_b = lista_a.copy()

print(f" ID da lista A: {id(lista_a)} | ID da lista B:{id(lista_b)}")

lista_1 = [[1, 2], [3, 4]]
lista_2 = lista_1.copy()

print(f"Conteúdos da lista 1: {lista_1} | ID da lista 2: {lista_2})")
print("\n\n")

lista_2[0][0] = 999
print(f"LISTA 1: {lista_1}\n\n")
#A lista alterou a orignal e não copiou. Isso é perigoso

import copy
lista_2 = copy.deepcop(lista_1)
#Na boa prática da programação o import fica no inicio da linha de programação