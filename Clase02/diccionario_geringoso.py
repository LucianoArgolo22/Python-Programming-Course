def geringoso(palabra):
    llave = palabra
    lista_de_letras = []

    for c in palabra:
        if c.lower() in ["a","e","i","o","u"]:
            c = c + "p" + c
        lista_de_letras.append(c)

    palabra_geringoso = ''.join(lista_de_letras)
    return palabra_geringoso


if __name__ == '__main__':

    try:
        lista_de_frutas = ["banana","manzana","mandarina"]
        diccionario_geringoso = {}

        for palabra in lista_de_frutas:
            diccionario_geringoso[palabra] = geringoso(palabra)

        print(diccionario_geringoso)
    except:
        raise Exception
