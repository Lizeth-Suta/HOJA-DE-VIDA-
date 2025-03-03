def caracter_a_binario(caracter):
    # Obtener el código ASCII del caracter
    codigo_ascii = ord(caracter)
    
    # Convertir el código ASCII a binario
    binario = bin(codigo_ascii)[2:]
    
    return binario

def main():
    caracter = input("Ingrese un caracter: ")
    
    binario = caracter_a_binario(caracter)
    
    print(f"El caracter '{caracter}' en binario es: {binario}")

if __name__ == "__main__":
    main()
