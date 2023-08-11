lista = []
for i in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista.append(valor)
for i in range(len(lista)-1): #Hace los recorridos
    for j in range(len(lista)-1 - i): #Hace los intercambios
        if lista[j] > lista[j+1]:
            lista[j], lista[j + 1] = lista[j + 1], lista [j]
print(lista)
            