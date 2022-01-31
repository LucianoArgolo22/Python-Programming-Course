#%%
# directorio = os.path.join('c:\\', 'usuario', 'ejercicios_python')
# os.chdir(directorio)    
# os.getcwd()
# '/home/usuario/ejercicios_python'
# os.listdir('../Data')
# os.mkdir('test')          # creo el directorio test
# os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
# os.listdir('test')
# #-------
# import os
# for root, dirs, files in os.walk("."):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

#------


def archivos_png(path):
    """
    función que recibe por argumento una carpeta (path)
    y recorre recursivamente en busca de todos los los
    archivos png que haya, imprimiéndolos en pantalla
    """
    lista_de_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if "png" in file:
                print(file)
                #lista_de_files.append(file)
    #return lista_de_files


if __name__ == '__main__':
    import os
    import sys
    path = sys.argv[1]

    archivos_png(path)
