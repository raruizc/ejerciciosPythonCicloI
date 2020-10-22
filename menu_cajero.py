#Menu de cajero electrónico
saldo = 1000000
def consultar(saldo_cuenta):
  return saldo_cuenta

def consignar(saldo_cuenta, valor):
  saldo_cuenta = saldo_cuenta + valor
  return saldo_cuenta

def retirar(saldo_cuenta, valor):
  saldo_cuenta -= valor
  return saldo_cuenta

bandera = True

while bandera: 

    print("Bienvenidos a Nuestro Cajero\nPor favor elija una de las siguientes opciones: ")
    print("\n1 -Para consultar saldo")
    print("2 -Para consignar")
    print("3 -Para retirar")
    print("0 -Para salir")

    opcion = int(input("\nIngrese la opción: "))
    
    if opcion == 1:
      print("Su saldo es:" , end="")
      print(consultar(saldo))
    elif opcion == 2:
      valor_consignar = float(input("Ingrese el valor a consignar: "))
      saldo = consignar(saldo, valor_consignar)
      print("\nEl saldo de su cuenta es:", saldo)
    elif opcion == 3:
      valor_retirar = float(input("Ingrese el valor a retirar: "))
      saldo = retirar(saldo, valor_retirar)
      print("\nEl saldo de su cuenta es:", saldo)  
    elif opcion == 0:
      print("\nGracias por utilizar nuestros servicios!!!")
      bandera = False
    else:
      print("\nOpcion no valida")