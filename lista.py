def estaEnRango(valor, minimo, maximo):
    try:
        return minimo <= int(valor) <= maximo
    except ValueError:
        return False

def estaEnLista(valor, lista):
    try:
        return int(valor) in lista
    except ValueError:
        return False

try:
    numero_usuario = int(input("Introduce un número del 1 al 20: "))
    
    if estaEnRango(numero_usuario, 1, 20):
        lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]
        
        if estaEnLista(numero_usuario, lista_numeros):
            print(f"El número {numero_usuario} está en la lista.")
        else:
            print(f"El número {numero_usuario} no está en la lista.")
    else:
        print("Error: El número debe estar en el rango del 1 al 20.")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")
