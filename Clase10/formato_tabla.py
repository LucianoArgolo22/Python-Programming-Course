# -*- coding: utf-8 -*-



class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        cadena = str('<tr><th>' + '<tr><tr>'.join(headers) +'<tr><th>')
        print(cadena)
    def fila(self, data_fila):
        cadena = str('<tr><th>'+'<tr><th>'.join(data_fila)+'<tr><th>')
        cadena_limpia = cadena.strip()
        print(cadena_limpia)


def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    return formateador

#tratar de hacer
def imprimir_tabla(tabla, columnas, fromato):
    
    for colname in tabla:
        print(getattr(tabla, colname))