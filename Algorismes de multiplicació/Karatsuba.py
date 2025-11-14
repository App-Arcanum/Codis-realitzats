def karatsuba(x, y):
  
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
#Separar els dígits hight-->x//10^m low--> x mod 10^m: exemple: n=1234 m=2  1234//100=12  i 1234 % 100= 34
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    z0 = karatsuba(low1, low2)              
    z1 = karatsuba(low1 + high1, low2 + high2)  
    z2 = karatsuba(high1, high2)            
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

print("="*52)
print("Multiplica dos nombres amb l'algoritmo de Karatsuba: ")
print("="*52)
a = int(input("Primer número: "))
b = int(input("Segun número: "))
resultat = karatsuba(a, b)
print(f"{a} * {b} = {resultat}")
if resultat == a*b:
    print("correcte")
else:
    print("Fals")