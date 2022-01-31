# #%%
# fecha_nacimiento = "14/06/1993"

import datetime
def vida(fecha_nacimiento):
    '''
    Recibe por parámetro una fecha en formato "dd/mm/AAAA"
    hace la diferencia de la fecha actual y el nacimiento en segundos
    devolviendo la cantidad de segundos vividos
    '''
    nacimiento = datetime.datetime(year = int(fecha_nacimiento[-4:]), month = int(fecha_nacimiento[-7:-5]),day = int(fecha_nacimiento[0:2])).timestamp()
    fecha_actual = datetime.datetime.now().timestamp()
    return int(fecha_actual - nacimiento)
# #%%
# vida(fecha_nacimiento)