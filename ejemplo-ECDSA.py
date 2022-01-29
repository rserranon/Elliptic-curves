import ecdsa

# Definir los parametros de la curva de Bitcoin simplificada
_a = 0
_b = 7
_p = 37
ec_order = 13

print(f"a = {_a}")
print(f"b = {_b}")
print(f"p = {_p}")
print(f"ec_order = {ec_order}")

print('Ecuación y^2 = x^3 ',end='')
if _a != 0:
    print('+ {}x'.format(_a),end='')
print('+ {}'.format( _b))

# definir la curva eliptica
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)

# definir el punto generador G
_Gx = 8
_Gy = 1
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, ec_order)
G = generator_secp256k1
print(f"G = {G}")

# definir la llave privada
k_prv = 9
print(f"k_prv = {k_prv}")

# calcular la llave publica 
K_pub = k_prv * G
print(f"K_pub = {K_pub}")

# proceso de cifrado

# definir hash del mensaje
z = 4
print(f"z = {z}")

# seleccionar un numero aleatorio y calclular el punto P 
k = 7
P = k * G
print(f"P = {P}")

# calcular r, es la coordenada x de P
r = P.x() % ec_order
print(f"r = {r}")

# encontrar el inverso mutiplicativo de k
k_inv = pow(k, -1, ec_order)
s = (k_inv * (z + r * k_prv)) % ec_order
print(f"s = {s}")

print('La firma es el par (r,s) -> ({0},{1})'.format(r,s))

# proceso de verificacion

# calcular el inverso multiplicativo de s y calcular u y v
s_inv = pow(s, -1, ec_order)
u = (s_inv * z) % ec_order
v = (s_inv * r) % ec_order
print(f"u = {u}")
print(f"v = {v}")

# calcular P_point
P_point = u * G + v * K_pub
print(f"P_point = {P_point}")

# verificar si la coordenada x de P_point es igual a r
if P_point.x() % ec_order == r:
    print('el mensaje z = {0} fue firmado por el originador de la firma.'.format(z))
else:
    print('el mensaje  z = {0} no fue firmado por el originador de la firma.'.format(z))
