comprobar = True
fila = " - "
columna = " | "

while comprobar == True:
    n = int(input("Ingrese un número: "))
    if n > 0:
        i = 1
        print(" ----------------------")
        while i < 11:
            print(" | ", n, " | ", i, "  | ", n*i, " | ")
            print(" ----------------------")
            i = i + 1
        comprobar = False
    else:
        "Por favor ingrese un número válido."

