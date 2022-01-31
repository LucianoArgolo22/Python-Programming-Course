


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {"cambio":>10s}')
        print('---------- ---------- ---------- ----------')
        
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        for r in rowdata:
           print(f'{r[0]:>10s} {r[1]:>10d} {"$"+str(r[2]):>10s} {r[3]:>10.2f}')

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