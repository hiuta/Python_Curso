print('ingrese codigo')

print('CALCULO POR:')
print('1.piezas')
print('2.Ml Parcial')
print('3.Ml Entero')
print('4.Dia')
seleccion = input()
print(seleccion)

match seleccion:
    case '1':
        print("el calculo por piezas es")
        a=250/3
        print(a)
    case '2':
        print("el calculo por Ml parcial es")
        a = 250 / 3
        print(a)
    case '3':
        print("el calculo por Ml Entero es")
        a = 250 / 3
        print(a)
    case '4':
        print("el calculo por Dia es")
        a = 250 / 3
        print(a)
    case _:
        print('operacion no encotrado')

