# Addició (operador XOR)
def xor(a,b):
  c = []
  for i in range(0,8):
    if (a[i]==0 and b[i]==0) or (a[i]==1 and b[i]==1):
      c.append(0)
    else:
      c.append(1)
  return c

# Multiplicació (en mòdul m(x)=x^8+x^4+x^3+x+1)
def mult(a,b):
  p = [0]*15
  for i in range(0,8):
    for j in range(0,8):
      c = a[i]*b[j]
      p[i+j] += c
  for k in range(0,15):
    p[k] = p[k]%2
  grado = -1
  i=0
  while grado == -1 and i<=14:
    if p[i] == 1:
      grado = 14-i
    i += 1
  if grado == -1:
    grado = 0

  # Reducció pel polinomi irreductible x^8 + x^4 + x^3 + x + 1
  while grado > 7:
    n = 14-grado
    p[n] = 0
    # aplicar xor amb els coeficients del polinomi (desplaçaments 4,5,7,8 respecte a n)
    p[n+4] = (p[n+4] + 1) % 2
    p[n+5] = (p[n+5] + 1) % 2
    p[n+7] = (p[n+7] + 1) % 2
    p[n+8] = (p[n+8] + 1) % 2

    grado = -1
    i=0
    while grado == -1 and i<=14:
      if p[i] == 1:
        grado = 14-i
      i += 1
    if grado == -1:
      grado = 0

  # quedem amb els 8 coeficients de grau 7..0
  # p actual té longitud 15; volem els últims 8 elements (p[7]..p[14])
  res = p[7:15]
  return res

# Invers multiplicatiu en GF(2^8). Si a == 0 retorna vector zero.
def invers(a):
  # a: vector de 8 bits
  # si a és 0 retorna 0
  if all(bit == 0 for bit in a):
    return [0]*8
  one = [0,0,0,0,0,0,0,1]
  # busquem b tal que mult(a,b) == one
  # prova tots els valors 1..255
  for v in range(1,256):
    # convertir v a vector de 8 bits
    bv = [(v >> (7-i)) & 1 for i in range(8)]
    prod = mult(a,bv)
    if prod == one:
      return bv
  # no ha de passar mai
  return [0]*8

# SubBytes (substitució de bytes)
def sub_bytes():
  matriu_inv = []   # vector amb els inversos (mòdul m(x)) de tots els nombres, de 0 a 255
  for i in range(0,256):
    j = f"{i:08b}"
    n = [int(j[k]) for k in range(8)]
    m = invers(n)
    matriu_inv.append(m)

  sbox = []
  c = [0,1,1,0,0,0,1,1]
  for i in range(0,256):
    bi = matriu_inv[i]
    si = []
    for j in range(0,8):
      j1 = (j-4)%8
      j2 = (j-5)%8
      j3 = (j-6)%8
      j4 = (j-7)%8
      num = (bi[j]+bi[j1]+bi[j2]+bi[j3]+bi[j4]+c[j])%2
      si.append(num)
    sbox.append(si)

  return sbox

# Funció per convertir un vector de 8 components en el seu corresponent nombre decimal
def vector_to_dec(a):
  res = 0
  for i in range(0,8):
    res = res + a[i]*2**(7-i)
  return res

# AddRoundKey
def AddRoundKey(state,words):
  nou = []
  for i in range(0,16):
    suma = xor(state[i],words[i])
    nou.append(suma)
  return nou

# ShiftRows
def ShiftRows(state):
  # state: llista de 16 vectors (bytes)
  nou = [None]*16
 
  for r in range(4):
    for c in range(4):
      src_pos = 4*c + r
      dst_col = (c - r) % 4 
      dst_pos = 4*dst_col + r
      nou[dst_pos] = state[src_pos]
  return nou

# MixColumns
def MixColumns(state):
  nou = []
  b2 = [0,0,0,0,0,0,1,0]
  b3 = [0,0,0,0,0,0,1,1]
  for k in range(0,4):
    i0 = 4*k
    a0 = state[i0]
    a1 = state[i0+1]
    a2 = state[i0+2]
    a3 = state[i0+3]

    vec1a = xor(mult(b2,a0),mult(b3,a1))
    vec1b = xor(a2,a3)
    nou.append(xor(vec1a,vec1b))

    vec2a = xor(a0,mult(b2,a1))
    vec2b = xor(mult(b3,a2),a3)
    nou.append(xor(vec2a,vec2b))

    vec3a = xor(a0,a1)
    vec3b = xor(mult(b2,a2),mult(b3,a3))
    nou.append(xor(vec3a,vec3b))

    vec4a = xor(mult(b3,a0),a1)
    vec4b = xor(a2,mult(b2,a3))
    nou.append(xor(vec4a,vec4b))
  return nou

# --------- Programa principal ----------
nrounds = 10   # nombre de rondes d'AES-128
sbox = sub_bytes()   # sbox és la matriu 8*8 que substitueix un byte per un altre

# Lectura de la clau de 128 bits (16 bytes)
key = input("Escriu la clau pública (ha de tenir 16 caracters): ")
if len(key) != 16:
  print("La clau pública triada no té 16 caracters")
  exit()
key_alpha = list(key)   # clau pública (llista de 16 caràcters)
key_ascii = []  # clau pública (llista de 16 valors ASCII)
key_bin = []  # clau pública (llista de 16 vectors binaris de longitud 8)
key_hex = []  # clau pública (en una llista de 16 vectors hexadecimals de longitud 2)
for i in range(0,16):
  key_ascii.append(ord(key_alpha[i]))
  n = f"{key_ascii[i]:08b}"
  key_bin_i = [int(n[j]) for j in range(0,8)]
  key_bin.append(key_bin_i)
  nhex = f"{key_ascii[i]:02x}"
  key_hex.append(nhex)

# Expansió de la clau
Rcon = []
Rcon0 =[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon0)
Rcon1 =[[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon1)
Rcon2 =[[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon2)
Rcon3 =[[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon3)
Rcon4 =[[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon4)
Rcon5 =[[0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon5)
Rcon6 =[[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon6)
Rcon7 =[[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon7)
Rcon8 =[[0,0,0,1,1,0,1,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon8)
Rcon9 =[[0,0,1,1,0,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
Rcon.append(Rcon9)

expkey = []
for i in range(0,16):
  expkey.append(key_bin[i])

for i in range(1,nrounds+1):
  for j_word in range(0,4):
    index_word = 4*i+j_word
    if index_word%4 == 0:
      index_byte0 = 4*index_word
      rotword = []
      rotword.append(expkey[index_byte0-3])
      rotword.append(expkey[index_byte0-2])
      rotword.append(expkey[index_byte0-1])
      rotword.append(expkey[index_byte0-4])
      for k in range(0,4):
        index_byte = index_byte0+k
        num1 = vector_to_dec(rotword[k])
        vect1 = xor(sbox[num1],expkey[index_byte-16])
        byte = xor(vect1,Rcon[i-1][k])
        expkey.append(byte)
    else:
      for k in range(0,4):
        index_byte = 4*index_word+k
        byte = xor(expkey[index_byte-4],expkey[index_byte-16])
        expkey.append(byte)

# Mostrem la clau extesa (en format hexadecimal)
expkey_hex=[]
for i in range(0,176):
  n = vector_to_dec(expkey[i])
  n_hex = f"{n:02x}"
  expkey_hex.append(n_hex)
print("Aquesta és la clau extesa:")
for k in range(0,nrounds+1):
  print(expkey_hex[16*k:16*(k+1)])

# Lectura de l'estat 128 bits (16 bytes)
estat = input("Escriu l'estat que vols xifrar (ha de tenir 16 caracters): ")
if len(estat) != 16:
  print("L'estat triat no té 16 caracters")
  # omplim amb caracters nuls fins a 16
  estat = estat + ("\x00" * (16 - len(estat)))

estat_alpha = list(estat)   # estat (llista de 16 caràcters)
estat_ascii = []
estat_bin = []
estat_hex = []
for i in range(0,16):
  estat_ascii.append(ord(estat_alpha[i]))
  n = f"{estat_ascii[i]:08b}"
  estat_bin_i = [int(n[j]) for j in range(0,8)]
  estat_bin.append(estat_bin_i)
  estat_hex.append(f"{estat_ascii[i]:02x}")
print("Estat inicial:",estat_hex)

# Ronda 0: AddRoundKey
vector_w = []
for k in range(0,16):
  vector_w.append(expkey[k])
estat_bin = AddRoundKey(estat_bin,vector_w)

# Fem les 9 primeres rondes, amb els 4 passos
for i_round in range(1,nrounds):
  for k in range(0,16):
    estat_bin[k] = sbox[vector_to_dec(estat_bin[k])]
  estat_bin = ShiftRows(estat_bin)
  estat_bin = MixColumns(estat_bin)
  vector_w =[]
  for k in range(0,16):
    vector_w.append(expkey[16*i_round+k])
  estat_bin = AddRoundKey(estat_bin,vector_w)

  # Mostrem l'estat fins ara (en format hexadecimal):
  estat_hex=[]
  for i in range(0,16):
    n = vector_to_dec(estat_bin[i])
    n_hex = f"{n:02x}"
    estat_hex.append(n_hex)
  print("RONDA",i_round,". Aquest és l'estat fins ara':",estat_hex)

# Ronda número 10 (final)
for k in range(0,16):
  estat_bin[k] = sbox[vector_to_dec(estat_bin[k])]
estat_bin = ShiftRows(estat_bin)
vector_w=[]
for k in range(0,16):
  vector_w.append(expkey[160+k])
estat_bin = AddRoundKey(estat_bin,vector_w)

# Mostrem l'estat final:
estat_hex=[]
for i in range(0,16):
  n = vector_to_dec(estat_bin[i])
  n_hex = f"{n:02x}"
  estat_hex.append(n_hex)
print("AQUEST ÉS L'ESTAT XIFRAT FINAL:",estat_hex)

