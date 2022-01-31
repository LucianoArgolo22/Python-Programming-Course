#%%
# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types= None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        registros = []

        #sino tiene headers, devuelvo lista de tupla de valores
        if has_headers == False:

            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                
                if types:
                    row = [func(val) for func, val in zip(types, row) ]

                registros.append(tuple(row))
            #otra forma para armar la tupla de valores, pero con complicaciones con el if not row
            #registros = [tuple([valor for valor in row]) for row in rows if row]

        #si tiene headers, devuelvo lista de diccionario de valores
        elif has_headers == True:
            
            encabezados = next(rows)

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select

            else:
                indices = []

            for row in rows:

                if not row:    # Saltea filas sin datos
                    continue

                if types:
                    row = [func(val) for func, val in zip(types, row) ]

                if indices:
                    row = [row[index] for index in indices]
                registro = dict(zip(encabezados, row))
                registros.append(registro)


    return registros

