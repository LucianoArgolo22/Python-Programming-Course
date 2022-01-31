#%%
# fileparse.py
import csv
from threading import Lock

def parse_csv(texto_o_archivo, select = None, types= None, has_headers=True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    """
    Verifica mediante un try except si Select y has headers son seleccionados juntos
    """
    lock = Lock()
    lock.acquire()

    try:
        if isinstance(texto_o_archivo,str):
            with open(texto_o_archivo) as f:
                rows = csv.reader(f)

        elif isinstance(texto_o_archivo,list):
            rows = texto_o_archivo

        
        registros = []

        #sino tiene headers, devuelvo lista de tupla de valores
        if has_headers == False:

            for i,row in enumerate(rows):
                try:
                    if not row:    # Saltea filas sin datos
                        continue
                    
                    if types:
                        row = [func(val) for func, val in zip(types, row) ]

                    registros.append(tuple(row))
                #otra forma para armar la tupla de valores, pero con complicaciones con el if not row
                #registros = [tuple([valor for valor in row]) for row in rows if row]
                except:
                    if silence_errors == True:
                        print(ValueError(f"Fila {i}: No pude convertir : {row} \n Fila {i}: Motivo invalid literal for int() with base 10: ''"))
                    else:
                        pass

                finally:
                    lock3.release()

        #si tiene headers, devuelvo lista de diccionario de valores
        elif has_headers == True:
            encabezados = next(rows)

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select

            else:
                indices = []

            for i,row in enumerate(rows):
                print(row)
                lock3 = Lock()
                lock3.acquire()
                try:
                    if not row:    # Saltea filas sin datos
                        continue

                    if types:
                        row = [func(val) for func, val in zip(types, row) ]

                    if indices:
                        row = [row[index] for index in indices]
                    registro = dict(zip(encabezados, row))
                    registros.append(registro)

                except:
                    if silence_errors == True:
                        print(ValueError(f"Fila {i+1}: No pude convertir : {row} \n Fila {i+1}: Motivo invalid literal for int() with base 10: ''"))
                    else:
                        pass

                finally:
                    lock3.release()
        return registros

    
    except:
        if silence_errors == False:
            if select and has_headers == True:
                print(RuntimeError("Para seleccionar, necesito encabezados."))
        else:
            pass

    finally:
        lock.release()

#%%
camion = parse_csv('../Data/missing.csv', types = [str,int,float],has_headers = True)
print(camion)
# %%
#%%
import csv
with open('../Data/camion.csv',"r") as f:
    aver = csv.reader(f)
    lista_nueva = []
    for a in aver:
        lista_nueva.append(",".join(a))
lista_nueva
#%%
import csv
aver = csv.reader(["a,b,c","1,2,3"])
for a in aver:
    print(a)

