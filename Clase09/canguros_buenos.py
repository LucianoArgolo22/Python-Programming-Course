#%%
class Canguro():
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, lista_opcional = None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.contenido_marsupio = lista_opcional if lista_opcional else []
        self.nombre = nombre
    
    def meter_en_marsupio(self,elemento):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(str(elemento))
    
    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        return "(" + ", ".join([str(element) for element in self.contenido_marsupio]) + ")"

# %%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)

#el problema parece resuelto, cangurito ya no devuelve nada