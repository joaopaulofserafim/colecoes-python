lista1 = {
    "Andrei", "Nicolas", "José"
}

print(lista1)


#Adicionando

lista1.add("Maria")

print(lista1)

#Removendo

lista1.remove("Maria")
print(lista1)

#Discarte
lista1.discard("José")
print(lista1)


#Adicionando mais itens só para teste

lista1.add("João")
lista1.add("Pedro")
lista1.add("Vitor")
lista1.add("Maria")
lista1.add("Joaquim")
print(lista1)

#POP (Tira qualqer um)
lista1.pop()
print(lista1)


#Unindo 

lista2 = {
    "Frio", "Calor", "Sol", "Joaquim"
}

unir = lista1.union(lista2)
print(unir)

# Interseção (item igual nas duas listas)
intersecao = lista1.intersection(lista2)
print(intersecao)


# Issuperset verifica se o segundo conjunto contém o primeiro conjunto dentro 

Ex1 = {
    "Carro", "Avião", "Navio"
}
Ex2 = {
    "Carro", "Avião"
}

issu = Ex1.issuperset(Ex2)
print(issu)

#Issubset verifica se o segundo conjunto contém o primeiro conjunto dentro 
Ex3 = {
    "Macaco", "Cachorro"
}

Ex4 = {
    "Macaco", "Cachorro", "Gato"
}

bset = Ex3.issubset(Ex4)
print(bset)

# Diferença retorna itens que contém no primeiro conjunto e não contém no segundo conjunto utilizando o método 'difference'

Ex5 = {
    "Filme", "Serie"
}
Ex6 = {
    "Filme", "Serie", "Livro", 
}

diferenca = Ex5.symmetric_difference(Ex6)
print(diferenca)

# Clear limpa os itens do conjuntos


Ex7 = {
    "Sapato", "Chinelo", "Bota"
}

Ex7.clear()
print(Ex7)
