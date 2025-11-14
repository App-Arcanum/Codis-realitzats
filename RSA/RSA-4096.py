import random

def miller_rabin(n, repeticions=5):
    if n % 2 == 0 or n <= 1:
        return False

    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

    for _ in range(repeticions):
        a = random.randint(2, n - 2)
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generar_primer(bits=2048):
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1
        if miller_rabin(n):
            return n

def algoritme_euclides_extes(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        mcd, x1, y1 = algoritme_euclides_extes(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (mcd, x, y)

def invers_modular(a, m):
    mcd, x, _ = algoritme_euclides_extes(a, m)
    if mcd != 1:
        raise ValueError(f"No existeix l’invers modular de {a} mod {m}")
    else:
        return x % m

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generar_e(phi_n):
    candidats = [65537, 131071, 524287, 1048573]
    for e in candidats:
        if mcd(e, phi_n) == 1:
            return e
    e = 3
    while e < phi_n:
        if mcd(e, phi_n) == 1:
            return e
        e += 2
    raise Exception("No s’ha pogut trobar un valor vàlid per a e.")

def generar_claus_rsa():
    print("=== GENERADOR RSA ===")
    
    p = generar_primer()
    q = generar_primer()

    print("Nombres processats")

    if p == q:
        print("Error: p i q han de ser diferents.")
        return

    n = p * q
    phi_n = (p - 1) * (q - 1)

    print(f"\nn = p * q = {n}")
    print(f"φ(n) = (p - 1)(q - 1) = {phi_n}")

    e = generar_e(phi_n)
    d = invers_modular(e, phi_n)

    print("\n=== RESULTATS ===")
    print(f"Clau pública: (n = {n}, e = {e})")
    print(f"Clau privada: (d = {d})")
    print(f"Verificació: (e * d) % φ(n) = {(e * d) % phi_n} (ha de ser 1)")

    return e, d, n

def encriptar(e, n):
    m = str(input("Escriu el missatge: "))
    missatge_encriptat = []
    for i in m:
        c = (ord(i)) ** e % n
        missatge_encriptat.append(c)

    text = ""
    for i in missatge_encriptat:
        text += str(i)
        text += ", "

    nom = input("Posa nom al document: ")
    with open(f'{nom}.text', 'w') as f:
        f.write(text)

def desencriptar(c, n, d):
    missatge = ""
    for i in c:
        m = chr(pow(i, d, n))
        missatge += m
    print(missatge)

# Interfície d’usuari
print("=" * 50)
print("======== Encriptador i desencriptador amb RSA ======")
print("=" * 50)
print("Benvingut a l’eina per encriptar i desencriptar missatges amb RSA.")
print("Pots triar una de les dues opcions següents:")
print("1 - Encriptar missatges")
print("2 - Desencriptar missatges")
opcio = int(input("Selecciona l’opció que desitges executar: "))
print("=" * 50)

if opcio == 1:
    e, d, n = generar_claus_rsa()
    encriptar(e, n)
elif opcio == 2:
    nom_arxiu = str(input("Nom de l’arxiu: "))
    with open(f'{nom_arxiu}.text', 'r') as f:
        entrada = f.read()

    entrada = entrada.replace('[', '').replace(']', '').replace(',', '')
    c = [int(x) for x in entrada.split()]

    n = int(input("Clau pública: "))
    d = int(input("Clau privada: "))
    desencriptar(c, n, d)
else:
    print("Opció inexistent")
