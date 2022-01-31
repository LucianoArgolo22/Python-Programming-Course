#%%
#-------hojas_ISO

def medidas_hojas_A_aux(N):
    if N == 0:
        return [(841,1189)]
    else:
        hoja = medidas_hojas_A(N-1)
        hoja += [(int(hoja[-1][1]/2),hoja[-1][0])]
    return hoja



def medidas_hojas_B(N):
    valorfinal = medidas_hojas_A_aux(N)
    return valorfinal


medidas_hojas_B(10)