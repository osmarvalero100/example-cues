print('Hola CUES')
print('Cambiado desde github')
print('Cambio desde mi PC')

def suma(num1, num2):
    """Suma dos numeros

    Args:
        num1 (int): Número 1 a sumar
        num2 (int): Número 2 a suma

    Returns:
        int: Resultado de la suma
    """
    return num1 + num2

def resta(num1, num2):
    """Resta dos numeros

    Args:
        num1 (int): Número 1 a restar
        num2 (int): Número 2 a restar

    Returns:
        int: Resultado de la resta
    """
    return num1 - num2

if __name__ == '__main__':
    num1 = 4
    num2 = 8
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    print(f'\n{"-"*10} SUMAR {"-"*10}')
    print(f'La suma entre {num1} y {num2} es: {resultado_suma}')
    print(f'\n{"-"*10} RESTAR {"-"*10}')
    print(f'La resta entre {num1} y {num2} es: {resultado_resta}')
