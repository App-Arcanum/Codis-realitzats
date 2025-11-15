import random
import sympy
from sympy import isprime, primerange, primitive_root

import os
import time

import diffie_hellman_db_controller

# Para el limpiado de terminal
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def genera_nombre_primer(min_val, max_val):
    primers = list(primerange(min_val, max_val))
    return random.choice(primers)


def genGlobalKey(p:int):
    q = primitive_root(p)
    
    while not isprime(q):
        possibles = [g for g in range(2, p) if pow(g, (p - 1) // 2, p) != 1]
        q = random.choice(possibles)

    diffie_hellman_db_controller.writePublicKey(p,q)
    return q

def printPQ(p,q):
    print(".............................................................")
    print(f"Numero primo p: {p}")
    print(f"Raiz primitiva y prima q: {q}")
    print(".............................................................")

def printHelpInfo():
    print("HELP INFO ...................................................")
    print("GenPubKey: Genera Clave Public para la comunicacion entre los dos extremos")
    print("GenPriKey: Genera Clave Privada, no compartir con nadie")
    print("GenMezcla: Genera la Mezcla que se compartira publicamente para permitir la comunicacion bidireccional")
    print("SC: Genera la Clave Secreta para la comunicacion con el usuario deseado")
    print("EndTrans: Termina la transmision y se elimina toda la informacion de la BD")
    print("exit: Termina la ejecuccion")
    print("clear: Limpia la terminal")
    print("Help: Informacion sobre los comandos")

def printInfoAboutProgram():
    print("Diffie-Hellman Key Exchange (Demo Version)")
    print("Starting program...")
    time.sleep(3)
    limpiar_terminal()

def main():
    p = None
    q = None
    claup = None
    Mezcla = None
    Clausecreta = None

    printInfoAboutProgram()

    usuari = input("Nom usuari: ")

    while True:
        i = input("Operacion: ")
        if (i == "GenPubKey"):
            p = genera_nombre_primer(100,500)
            q = genGlobalKey(p)
            printPQ(p,q)
        elif (i == "GenPriKey"):
            p,q = diffie_hellman_db_controller.readPublicKey()
            if (p == None or q == None): continue
            printPQ(p,q)
            claup = genera_nombre_primer(2,p-1)
            print("La Private Key es: ",claup)
        elif (i == "GenMezcla"):
            p,q = diffie_hellman_db_controller.readPublicKey()
            if (p == None or q == None): continue
            printPQ(p,q)
            Mezcla = pow(q, claup, p)
            print(".............................................................")
            print("Nuestra Mezcla es: ",Mezcla)
            print(".............................................................")
            diffie_hellman_db_controller.writeMezcla(usuari,Mezcla)
        elif (i == "SC"):
            p, q = diffie_hellman_db_controller.readPublicKey()
            if (p == None or q == None): continue
            printPQ(p,q)
            usn = input("Usuario con el que se desea comunicar: ")
            Mezcla = diffie_hellman_db_controller.readMezclaKey(usn)
            if (Mezcla == None): continue
            print(".............................................................")
            print("La Mezcla del usuario es: ",Mezcla)
            print(".............................................................")
            if (Mezcla == None): 
                print("Usuario no encontrado") 
                continue
            else: print("La Mezcla del Usuario es: ",Mezcla)
            
            Clausecreta = pow(Mezcla,claup,p)
            print(".............................................................")
            print("Clave Secreta: ",Clausecreta)
            print(".............................................................")
            
        elif (i == "EndTrans"): 
            confI = input("Estas Seguro [Y/N]: ")
            if (confI == "Y"): diffie_hellman_db_controller.borrar_todo()
            else: print("Operacion Cancelada")
        elif (i == "exit"): break
        elif (i == "clear"):
            limpiar_terminal()
            continue
        elif (i == "Help"):
            printHelpInfo()
        else: 
            print("Comando no existente")

        print("> ",i," :##################################################################")


if __name__ == "__main__":
    main()