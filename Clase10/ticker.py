
from os import startfile
from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador

lines = vigilar('../Data/mercadolog.csv')
def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(headers, rows):
    for row in rows:
        yield dict(zip(headers,row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(["Nombre", "Cajones", "Precio"], rows)
    return rows

def filtrar_datos(rows, nombres):
    rows =  (row for row in rows if row['Nombre'] in nombres)
    for row in rows:
        yield row

def imprimir_tabla(rows,fmt):

    if fmt == 'txt':
        headers = tuple(["Nombre", "Cajones", "Precio"])
        print('%10s %10s %10s' % headers)
        print(('-'*10 + ' ')*len(headers))
        for row in rows:
            valores = list(row.values())
            print('%10s %10.2f %10d' % ( tuple(valores) ) )

    elif fmt == 'csv':
        print(",".join(["Nombre", "Cajones", "Precio"]))
        for row in rows:
            values = [func(val) for val,func in zip(row.values(),[str, str, str]) ]
            print(",".join(values))


def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    lines = vigilar(log_file)
    rows = parsear_datos(lines)
    rows = filtrar_datos(rows, camion)
    imprimir_tabla(rows,fmt)


if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')

