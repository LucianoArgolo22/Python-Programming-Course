cadena = 'Geringoso'
capadepenapa = ''
lista_de_letras = []

for c in cadena:
    if c == "e":
        c = c + "pe"
    elif c == 'i':
        c = c + 'pi'
    elif c == 'o':
        c = c + 'po'
    elif c == 'a':
        c = c + 'pa'
    elif c == 'u':
        c = c + 'pu'
    
    lista_de_letras.append(c)

capadepenapa = ''.join(lista_de_letras)
