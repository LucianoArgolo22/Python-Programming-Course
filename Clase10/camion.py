
import lote
class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total

    def __contains__(self,substr):
        lotes = self.__iter__()
        precios = []
        nombres = []
        cajones = []
        for i in range(len(self.lotes)):
            lote_devuelto = lotes.__next__()
            precios.append(str(lote_devuelto.precio))
            nombres.append(str(lote_devuelto.nombre))
            cajones.append(str(lote_devuelto.cajones))
        return (str(substr) in str(nombres)) or (str(substr) in str(cajones)) or (str(substr) in str(precios)) 

