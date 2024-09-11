def es_multiplo(numero1: int, numero2: int) -> str:

    if numero1 % numero2 == 0:
        return f"{numero1} es múltiplo de {numero2}"
    elif numero2 % numero1 == 0:
        return f"{numero2} es múltiplo de {numero1}"
    else:
        return f"{numero1} y {numero2} no son múltiplos entre sí"

def verificar_multiplos(numero1: str, numero2: str) -> str:
   
    try:
        num1 = int(numero1)
        num2 = int(numero2)

        if num1 <= 0 or num2 <= 0:
            return "Por favor, ingrese solo números enteros positivos."

        return es_multiplo(num1, num2)

    except ValueError:
        return "Por favor, ingrese solo números enteros válidos."

def main():
   
    print("Bienvenido al verificador de múltiplos.")
    print("Ingrese dos números enteros positivos para verificar si son múltiplos.")
    print("Para salir, ingrese 'q' en cualquier momento.")

    while True:
        numero1 = input("\nIngrese el primer número (o 'q' para salir): ")
        if numero1.lower() == 'q':
            break

        numero2 = input("Ingrese el segundo número: ")
        if numero2.lower() == 'q':
            break

        resultado = verificar_multiplos(numero1, numero2)
        print(resultado)

    print("filalizacion del verificador de multiplos")

if __name__ == "__main__":
    main()