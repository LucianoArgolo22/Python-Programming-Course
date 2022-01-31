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

                registros = []

                #sino tiene headers, devuelvo lista de tupla de valores
                if has_headers == False:

                    for i,row in enumerate(rows):

                        lock3 = Lock()
                        lock3.acquire()
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

        elif isinstance(texto_o_archivo,list):
            rows = texto_o_archivo
            registros = []
            #sino tiene headers, devuelvo lista de tupla de valores
            if has_headers == False:

                for i,row in enumerate(rows):
                    row = row.split(",")
                    lock3 = Lock()
                    lock3.acquire()
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
                
                encabezados = rows.pop(0).split(",")

                if select:
                    indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                    encabezados = select

                else:
                    indices = []

                for i,row in enumerate(rows):
                    row = row.split(",")
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
        if silence_errors == True:
            if select and has_headers == True:
                print(RuntimeError("Para seleccionar, necesito encabezados."))
        else:
            pass

    finally:
        lock.release()

# #%%
# camion = parse_csv('../Data/missing.csv', types = [str,int,float],has_headers = True)
# #%%
# lista = ['nombre,cajones,precio','Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
# lista2 = ['Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
# camion2 = parse_csv(lista, types=[str,int,float],has_headers = True)
# # %%
# camion,camion2
#%%
# f = open("../Data/missing.csv","rt")
# headers = next(f)
# #%%
# headers = next(f)
# #%%
# headers
# #%%

# r = [x * y for x in range(-10,10) if x > 0 and x%2==1 for y in [1,0,-1] if y!=0]
# # %%
# lista = [2,4,6,8,10]
# {x: x**2 for x in range(10) if x in lista}