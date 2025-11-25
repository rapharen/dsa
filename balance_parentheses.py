"""
"Balance Parentheses".
Análisis del Problema
Condición de Imposibilidad: Una cadena de paréntesis no se puede balancear si tiene una longitud impar o si el número de paréntesis de apertura ( no es igual al de cierre ). En esos casos, devolvemos -1.
Estrategia (Enfoque Greedy):
Recorremos la cadena de izquierda a derecha.
Mantenemos un contador de paréntesis de apertura "mal ubicados" (open_misplaced). Estos son los ( que hemos visto pero que aún no hemos cerrado.
Si encontramos un (, lo añadimos a nuestra cuenta de open_misplaced.
Si encontramos un ) y tenemos open_misplaced > 0, significa que podemos usar uno de los ( que ya vimos para cerrar este ). Así que decrementamos open_misplaced.
Si encontramos un ) y open_misplaced es 0, significa que este ) está mal ubicado (aparece antes que su ( correspondiente). Necesitamos "traer" un ( de más adelante en la cadena para balancear. Esto cuenta como un intercambio (swap). Por lo tanto, incrementamos el contador de swaps y también el de open_misplaced (porque este ( que "trajimos" ahora necesita su propio )).
Este método garantiza que solo hacemos intercambios cuando es estrictamente necesario, dándonos el número mínimo.

"""


def minimumSwaps(brackets):
    # 1. Verificar condiciones imposibles
    if len(brackets) % 2 != 0:
        return -1

    n = len(brackets)
    if brackets.count('(') != n // 2:
        return -1

    # 2. Aplicar el enfoque Greedy
    swaps = 0
    open_misplaced = 0

    for char in brackets:
        if char == '(':
            open_misplaced += 1
        else:  # char == ')'
            if open_misplaced > 0:
                # Este ')' cierra un '(' anterior
                open_misplaced -= 1
            else:
                # Este ')' está mal ubicado.
                # Necesita un swap con un '(' de más adelante.
                swaps += 1
                # El '(' "traído" ahora está abierto y mal ubicado.
                open_misplaced += 1

    return swaps
