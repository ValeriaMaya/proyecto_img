#Se debe crear la carpets de imagenes sobre el path en el que se este trabajando
import os
import matplotlib.pyplot as plt
directorio_trabajo = os.getcwd()
format_img = ['.jpg','.jpeg','.bmp','png']
path_carpeta = ''
nom_img = []

def comprobar_carpeta(nombre_carpeta):
    list_dir_t = os.list_dir_t(directorio_trabajo)
    if nombre_carpeta is list_dir_t:
        print "La carpeta se localizó correctamente en: ", directorio_trabajo
    else:
        print "La carpeta no se encuentra en: ", directorio_trabajo

def nom_file(nombre_carpeta,path_carpeta,nom_img):
    path_carpeta = directorio_trabajo + '/'+ nombre_carpeta
    nom_img = os.listdir(path_carpeta)
    print nom_img

#http://pillow.readthedocs.io/en/latest/PIL.html
