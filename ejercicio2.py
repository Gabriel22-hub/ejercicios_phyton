print('Por favor, ingresa 3 números enteros')
try:
    num1=int(input('Ingresa el primer número:'))
    print('-------------------------------------')
    num2=int(input('Ingresa el segundo número:'))
    print('-------------------------------------')
    num3=int(input('Ingresa el tercer número:'))
    print('-------------------------------------')
    sumatoria=num1 + num2 + num3
    promedio=float(sumatoria) / 3
    print('La media de los números',num1,',', num2, 'y', num3, 'es de', promedio)
except ValueError:
    print('Ese número no es entero')