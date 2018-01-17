def pendiente(datos_conocidos,ti, xi):
    xiti=[]
    sum_xiti = 0
    sum_xi = 0
    sum_ti = 0
    square_ti = []
    sum_square_ti = 0
    square_sum_ti = 0
    b = 0

    for i in range(datos_conocidos):
        xiti.append(xi[i]*ti[i])
    print(xiti)
    for i in range(datos_conocidos):
        sum_xiti = sum_xiti + xiti[i]
    print(sum_xiti)

    for i in range(datos_conocidos):
        sum_xi = sum_xi + xi[i]
    print(sum_xi)

    for i in range(datos_conocidos):
        sum_ti = sum_ti + ti[i]
    print(sum_ti)

    for i in range(datos_conocidos):
        square_ti.append(ti[i]**2)
    print(square_ti)
    for i in range(datos_conocidos):
        sum_square_ti = sum_square_ti + square_ti[i]
    print(sum_square_ti)

    square_sum_ti = sum_ti**2
    print(square_sum_ti)

    b = ((datos_conocidos*sum_xiti)-(sum_xi*sum_ti))/((datos_conocidos*sum_square_ti)-square_sum_ti)

    print(b)

    punto_inter(datos_conocidos, sum_ti, sum_xi, b)

def punto_inter(datos_conocidos, sum_ti, sum_xi, b):
    a = sum_xi/datos_conocidos - (b*(sum_ti/datos_conocidos))
    print(a)

    regresion(a,b,incognita)

def regresion(a,b,incognita):
    pronostico = a + (b*incognita)

    print(pronostico)




if __name__ == '__main__':
    ti = []
    xi = []
    print('Haremos una regresión lineal')
    datos_conocidos = int(input('¿Cuantos número relacionados se tienen?'))
    for i in range(datos_conocidos):
        ti.append(int(input('Agrega un t({})'.format(i))))
        xi.append(int(input('Agrega un x({})'.format(i))))

    incognita = int(input('¿Que valor quieres conocer?'))

    pendiente(datos_conocidos,ti, xi)
