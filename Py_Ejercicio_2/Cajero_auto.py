# Ejercicio: Cajero Automatico.
cajero_automatico=[
    'Deposito','Extracción','Transferencia','Salir'
]
menu="Bienvenido a su Cajero Automático."
print(menu)
opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))

while opcion != 4:
  
    if opcion == 1 :
        print(cajero_automatico[0])
        dinero=input('\nIngrese un monto de dinero: \n\n')
        print("Transfirió " + dinero + " correctamente\n\n")
        print(menu)
        opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))
       
    elif opcion == 2:
        print(cajero_automatico[1])
        dinero=input('\nIngrese un monto de dinero: \n') 
        print("Extrajo " + dinero + " correctamente\n\n")
        print(menu)
        opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))

    elif opcion == 3:
        print(cajero_automatico[2])
        dinero=input('\nIngrese un monto de dinero: \n\n')
        print("Transfirió " + dinero + " correctamente\n\n")
        print(menu)
        opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))

    else: 
        print("No marco ninguna pción correcta, seleccione una opción valida.\n")
        print(menu)
        opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))

print(cajero_automatico[3] + "\nAdiós")





