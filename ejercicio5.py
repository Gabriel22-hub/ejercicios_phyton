print('Calcular ingredientes de tortillas')
comensales=int(input('Introduce el número de comensales: '))

patatas=comensales * 200
huevos=(patatas // 1000) * 5
cebolla=(patatas // 1000) * 300

print('Para', comensales, 'comensales, necesitas: ')
print(patatas, 'gramos de patatas')
print(huevos, 'unidades de huevos')
print(cebolla, 'gramos de cebolla')