saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
pago_mensual = 2684.11

while saldo > 0:
    meses += 1
	
    if pago_extra_mes_comienzo <= meses and  meses <= pago_extra_mes_fin :
        pago_mensual =  2684.11 + pago_extra
        mensaje = 'Pago extra'
		
    else:
        pago_mensual = 2684.11
        mensaje = ""
    
    resto = saldo 
    saldo = saldo * (1+tasa/12) - pago_mensual
    

    saldo = 0 if saldo < 0 else saldo
    total_pagado =  total_pagado + resto if saldo == 0 else total_pagado + pago_mensual

    print('Meses: ',meses,'Total pagado', round(total_pagado, 2), "Saldo: ",saldo, mensaje)   