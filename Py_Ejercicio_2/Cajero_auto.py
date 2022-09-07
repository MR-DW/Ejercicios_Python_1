# Ejercicio: Cajero Automatico.
cajero_automatico={
    'Deposito':[],
    'Extracción':[],
    'Transferencia':[],
    'Salir':"Gracias por utilizar nuestro cajero"
}

print("Bienvenido a su Cajero Automático.")
opcion = int(input("Elija su operación:\n\t 1-Depositos,\n\t 2-Extracción,\n\t 3-Transferencia,\n\t 4-Salir\n"))

if opcion == 1 :
    print(cajero_automatico[0][0])
elif opcion == 2:
    print(cajero_automatico[1][0])
elif opcion == 3:
    print(cajero_automatico[2][0])
elif opcion == 4:
    print(cajero_automatico[3][0])
else: print("No marco ninguna pción correcta")