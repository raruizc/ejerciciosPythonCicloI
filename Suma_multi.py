def multiplicacion(suma, multiplicador):
    acumulador = 0
    for a in range(multiplicador):
        acumulador = acumulador + suma
    return acumulador
    
suma = int(input("Digite el número a multiplicar: "))
multiplicador=int(input("Digite el número multiplicador: "))

print(multiplicacion(suma,multiplicador))