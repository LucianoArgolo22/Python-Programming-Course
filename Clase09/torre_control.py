#%%
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl():
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.en_pista = []
        self.arribo = []
        self.partida = []

    def nuevo_arribo(self, x):
        '''Se agrega el avion a lista de atterizaje.'''
        self.arribo.append(x)

    def nueva_partida(self, x):
        '''Se agrega el avion a lista de
        partida. 
        Si la cola esta vacia, levanta ValueError.'''
        self.partida.append(x)

    def asignar_pista(self):
        '''Se agrega el avion a lista de los que están en pista
        o se los quita de la lista si despegan 
        Si la cola esta vacia, levanta ValueError.'''

        if self.esta_vacia():
            return ('No hay vuelos en espera.')

        elif len(self.arribo) > 0:
            return f'El vuelo {self.arribo.pop(0)} aterrizó con éxito.'

        elif len(self.partida) > 0:
            return (f'El vuelo {self.partida.pop(0)} aterrizó con éxito.')

    def ver_estado(self):
        '''Se verifica el estado de arribo y de despegue
        de los aviones'''
        print(f'Vuelos esperando para aterrizar: {", ".join(self.arribo)} \nVuelos esperando para despegar: {", ".join(self.partida)}')

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return (len(self.arribo) == 0) and (len(self.partida) == 0)
#%%

torre = TorreDeControl()
#%%
torre.nuevo_arribo('AR156')
#%%
torre.nueva_partida('KLM1267')
#%%
torre.nuevo_arribo('AR32')
#%%
torre.ver_estado()
#%%
#Vuelos esperando para aterrizar: AR156, AR32
#Vuelos esperando para despegar: KLM1267
torre.asignar_pista()
#%%
#El vuelo AR156 aterrizó con éxito.
torre.asignar_pista()
#%%
#El vuelo AR32 aterrizó con éxito.
torre.asignar_pista()
#%%
#El vuelo KLM1267 despegó con éxito.
torre.asignar_pista()
#No hay vuelos en espera.
# %%
