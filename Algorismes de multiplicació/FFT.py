import numpy as np

a = [int(d) for d in str(input("Primer nombre: "))]  
b = [int(d) for d in  str(input("Segon nombre: "))]  

def multiplicar_fft(a, b):
    # Converteix les llistes de dígits en arrays de numpy
    n = len(a) + len(b)
    n_fft = 1 << (n - 1).bit_length() 
    fa = np.fft.fft(a, n_fft)
    fb = np.fft.fft(b, n_fft)

   
    fc = fa * fb

    # Transformada inversa per obtenir coeficients del polinomi resultant
    c = np.fft.ifft(fc)
    c = np.round(c.real).astype(int)

    # Gestió dels arrossegaments
    resultat = []
    carry = 0
    for x in c:
        total = x + carry
        resultat.append(total % 10)
        carry = total // 10

    while carry:
        resultat.append(carry % 10)
        carry //= 10

    # Elimina zeros inicials
    while len(resultat) > 1 and resultat[-1] == 0:
        resultat.pop()

    return resultat[::-1]  # Invertim per tenir el nombre correctament



resultat = multiplicar_fft(a[::-1], b[::-1])
print("Resultat:", ''.join(map(str, resultat)))

