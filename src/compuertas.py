def find(pesos):
    funcion =  'g(-10 + 20x1 + 20x2)'
    entrada_a = [0,0,1,1]
    entrada_b = [0,1,0,1]
    output_obtenido = []
    output_binario = []
    output_esperado_or = [0, 1, 1, 1]
    output_esperado_and = [0, 0, 0, 1]
    comparacion_or = []
    comparacion_and = []
    for i in range(4):
        output_obtenido.append(int(pesos[0]+(pesos[1]*entrada_a[i])+(pesos[2]*entrada_b[i])))

    for i in range(4):
        if output_obtenido[i] < 0:
            output_binario.append(0)
        else:
            output_binario.append(1)

    print(output_binario)

    for item in output_binario:
        if output_binario[item] == output_esperado_or[item]:
            comparacion_or.append(item)

    for item in output_binario:
        if output_binario[item] == output_esperado_and[item]:
            comparacion_and.append(item)

    if len(comparacion_or) == 4:
        print('Es una Compuerta OR')

    elif len(comparacion_and) == 4:
        print('Es una Compuerta AND')

    else:
        print('Es otro tipo de compuerta')

if __name__ == '__main__':
    print('Compuertas lógicas AND Y OR')
    pesos = []
    for i in range(3):
        pesos.append(int(input('Agrega un x({})'.format(i))))

    find(pesos)
