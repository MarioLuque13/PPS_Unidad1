def esBinario(strbinario):
    return all(bit == '0' or bit == '1' for bit in strbinario)

def binario_a_decimal(strbinario):
    if not esBinario(strbinario):
        raise ValueError("Error: La entrada no es un número binario válido.")

    decimal = 0
    for i, bit in enumerate(reversed(strbinario)):
        decimal += int(bit) * (2 ** i)

    return decimal

try:
    numero_binario = input("Introduce un número binario: ")
    resultado = binario_a_decimal(numero_binario)
    print(f"El número binario {numero_binario} en formato decimal es: {resultado}")
except ValueError as e:
    print(e)