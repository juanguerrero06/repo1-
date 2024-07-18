def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se permite la división entre 0"

# Ejemplo de uso:
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Selecciona la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", suma(num1, num2))
elif operacion == "-":
    print("Resultado:", resta(num1, num2))
elif operacion == "*":
    print("Resultado:", multiplicacion(num1, num2))
elif operacion == "/":
    print("Resultado:", division(num1, num2))
else:
    print("Operación no válida")
