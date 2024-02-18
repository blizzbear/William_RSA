#PRACTICA DE RSA
import Crypto.Util.number

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

msg = "CU CU PUMAS"
print('msg = ', msg)
print('msg = ',len(msg.encode('utf-8')))


m= int.from_bytes(msg.encode('utf-8'), byteorder='big')
print('mensaje convertido en entero', m)


#cifrar mensaje lo hace alice con las llave publica de bob


c = pow(m, e, nB)
print('cifrado = ', c)


#bob lo descifra con su llave privada 


des = pow(c, dB, nB)
print('descifrado = ', des)



#para la tarea alice tiene que firmar con su llave privada y Bob descifra con su llave publica de tal forma que Bob sepa que Alice ha firmado el mensaje













      












