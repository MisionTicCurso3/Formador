import math

# c = 8
# elevado = c ** 2
# print("Res", elevado)

# print("Pow", math.pow(8,2))


# print("Raiz cuadrada POW", math.pow(25, 0.5))
# print("Raiz cuadrada Sqrt", math.sqrt(25))

# print("PI",math.pi)
# print("Euler",math.e)
# print("2pi",math.tau)


#Sin parametro y que no retorne
# def miNombre():
#     x = 1
#     b = 2
#     c = x + b
#     print("Res", c)


# miNombre()

#Me reciba parametro y que no retorne

def imc(peso, altura):
    res = peso / math.pow(altura, 2)
    print("Res", res)

print("INtroduce primero tu peso y luego tu altura")
imc(float(input()), float(input()))




