#Ejemplos de integracion compleja
import numpy as np
from scipy import integrate
def f(z):
    return np.exp(-z**2)
def g(x, y):
    z = x + 1j*y
    return f(z)

def p(z):
    return 2*z**3 - 3*z**2 + 4*z - 5
def h(theta):
    z = np.exp(1j*theta)
    return p(z)

def q(z):
    return 1/z
def j(theta):
    z = np.exp(1j*theta)
    return q(z)

result1, error1 = integrate.quad(j, 0, 2*np.pi)
result2,erro2 = integrate.quad(h, 0, 2*np.pi)

print("Resultado de 1/z, sobre el contorno del circulo unitario"+ str(result1))
print("Resultado de 2*z**3 - 3*z**2 + 4*z - 5, sobre el contorno del circulo unitario"+ str(result1))

result_real, error_real = integrate.quad(lambda x: integrate.quad(lambda y: g(x, y).real, -1, 1)[0], -1, 1) #Calcula el resultado real
result_imag, error_imag = integrate.quad(lambda x: integrate.quad(lambda y: g(x, y).imag, -1, 1)[0], -1, 1) #Calcula el resultado imaginario
result = result_real + 1j * result_imag
print("Resultado de exp(-z**2)"+str(result))