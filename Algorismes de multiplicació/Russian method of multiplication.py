print("Multiplica dos nombres amb l'algoritmo de Russ: ")
n1 = int(input("Valor Número más grande: ")) 
n2 = int(input("Valor Número más pequeño: ")) 


def multrusa2(petit, gran):
    resultat = gran
    sumaImpa = 0
    while petit > 1:
        if petit%2 != 0:
            sumaImpa += resultat
        resultat *= 2
        petit = petit // 2
    
    print("Resultat",resultat + sumaImpa)


multrusa2(n2, n1)