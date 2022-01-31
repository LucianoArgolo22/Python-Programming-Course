#%%
'''
El contrato de una función especifica qué condiciones se deben cumplir para que la función pueda ser invocada (precondición), y qué condiciones se garantiza que serán válidas cuando la función termine su ejecución (poscondición).
La documentación tiene como objetivo explicar qué hace el código, y está dirigida a quien desee utilizar la función o módulo.
Es una buena práctica incluir el contrato en la documentación.
Si una función modifica un valor mutable que recibe por parámetro, eso debe estar explícitamente aclarado en su documentación.
Los comentarios tienen como objetivo explicar cómo funciona el código y por qué se decidió implementarlo de esa manera, y están dirigidos a quien esté leyendo el código fuente.
Los invariantes de ciclo son las condiciones que deben cumplirse al comienzo de cada iteración de un ciclo.
'''

def valor_absoluto(n):
    '''
    n debe ser un número.
    Devuelve el elemento n si el mismo es >= 0.
    sino lo modifica y devuelve el equivalente negativo
    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''
    Recibe una lista de números por parámetro
    realiza la suma de todos los números pares,
    sino hay números pares, devuelve 0
    '''
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    Recibe dos números por parámetro
    si b es distinto de 0, y mientras nb lo sea, suma por cada iteración el valor a
    en simultáneo resta a nb 1 por cada iteración
    b tiene que ser un número mayor a 0, de ser negativo el programa ejecutará infinitamente
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''
    Recibe un número por parámetro
    mientras n sea distinto de 1 se sumará 1 al resultado
    '''

    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res