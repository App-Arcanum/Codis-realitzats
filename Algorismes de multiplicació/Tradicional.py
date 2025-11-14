import sys
sys.set_int_max_str_digits(10000000)  # permet imprimir nombres molt grans

def multiplicacion_clasica(x, y):
    # Convierte los números a text y luego los invierte
    x_str = str(x)[::-1]
    y_str = str(y)[::-1]

    # Lista para almacenar los dígitos del resultado
    resultado = [0] * (len(x_str) + len(y_str))

    # Multiplicació digit a digit
    for i in range(len(x_str)):
        for j in range(len(y_str)):
            producto = int(x_str[i]) * int(y_str[j])
            resultado[i + j] += producto

            
            resultado[i + j + 1] += resultado[i + j] // 10
            resultado[i + j] %= 10

    # Elimina ceros al final (que están al principio del número real porque está al revés)
    while len(resultado) > 1 and resultado[-1] == 0:
        resultado.pop()

    # Invertimos el resultado para dejarlo en orden correcto
    resultado.reverse()

    print("Resultat: ")
    print(int("".join(map(str, resultado))))

    return int("".join(map(str, resultado)))
print("Multiplica dos nombres amb l'algoritmo de Tradicional: ")
x=int(input("Ingresa numero 1: "))
y=int(input("Ingresa numero 2: "))
multiplicacion_clasica(x,y)