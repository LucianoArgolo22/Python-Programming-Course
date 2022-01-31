def ord_burbujeo(list):
    hubo_cambio = True
    while(hubo_cambio):
        #corto la secuencia si no hay nada que cambiar, o sea que ya está ordenado
        hubo_cambio = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                # Swap
                list[i], list[i+1] = list[i+1], list[i]
                hubo_cambio = True
 
#para el cálculo de la complejidad algorítmica lo que hago es:
#el while a lo sumo se ejecuta la misma cantidad de veces que el primer for
# esto es   n * n para el peor caso, y a su vez hago una comparación en el if, que sucede n veces
#entonces en total por cada cambio que haya, hay que recorrer la lista otra vez
# o sea que la complejidad logarítmica sería n * n + n, que son la cantidad de comparaciones del if
