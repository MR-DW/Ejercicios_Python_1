# Idear un programa que solicite al usuario dos números enteros y el programa
# deberá retornar aquellos números pares que se encuentren dentro del rango
# formado entre los números ingresados

num_1 = int(input('Ingrese un numero:\t'))
num_2 = int(input('Ingrese otro numero:\t'))

for i in range(num_1,num_2,2):
    if i % 2 == 0:

        print(i)
    else :
        print(i+1)
