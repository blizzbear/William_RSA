#PRACTICA DE RSA
import Crypto.Util.number
import Crypto.Util.number
import hashlib

bits = 1024

#Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print('pA = ', pA)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print('qA = ', qA)
#Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print('pA = ', pB)
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print('qA = ', qB)

nA = pA * qA
nB = pB * qB 
print('nA = ', nA)
print('nB = ', nB)
#indicador de euler de Alice
phiA = (pA - 1) * (qA - 1)
print('phiA = ', phiA)
#indicador de euler de Bob
phiB = (pB - 1) * (qB - 1)
print('phiB = ', phiB)

#por razones de eficiencia se elige el 65537 o el numero 4 de Fermat
e = 65537
print('e = ', e)
#llaves privadas
dA = Crypto.Util.number.inverse(e, phiA)
print('dA = ', dA)
dB = Crypto.Util.number.inverse(e, phiB)
print('dA = ', dB)

# Alice genera un HASH h(M) de un mensaje
msg = "CU CU PUMAS"
hashed_msg = hashlib.sha256(msg.encode('utf-8')).digest()
print('hashed_msg =', hashed_msg)

# Alice firma el mensaje con su llave privada
signature = pow(int.from_bytes(hashed_msg, byteorder='big'), dA, nA)
print('signature =', signature)

# Alice cifra el mensaje original con la llave pública de Bob
c = pow(int.from_bytes(hashed_msg, byteorder='big'), e, nB)
print('cifrado =', c)

# Bob recibe el mensaje cifrado y la firma
# Bob verifica la firma utilizando la llave pública de Alice
hashed_msg_received = pow(signature, e, nA)

# Verificar si el hash recibido coincide con el hash del mensaje original
if hashed_msg_received == int.from_bytes(hashed_msg, byteorder='big'):
    print("La firma es válida. Alice ha firmado el mensaje.")
    # Bob descifra el mensaje cifrado por Alice
    decrypted_msg = pow(c, dB, nB)
    print('mensaje descifrado por Bob:', decrypted_msg)
else:
    print("La firma no es válida. El mensaje no fue firmado por Alice.")
