#Se debe crear la carpets de imagenes sobre el path en el que se este trabajando
import os
directorio_trabajo = os.getcwd()
format_img = ['.jpg','.jpeg','.bmp','png']
path_carpeta = ''
nom_img = []
ob_img = []

#Se modificará para que se acceda a cualquier carpeta de la Pc.
def comprobar_carpeta(nombre_carpeta):
    list_dir_t = os.list_dir_t(directorio_trabajo)
    if nombre_carpeta is list_dir_t:
        print Bien
    else:
        print "La carpeta no se encuentra en: ", directorio_trabajo
#____

def nom_file(nombre_carpeta,path_carpeta,nom_img):
    path_carpeta = directorio_trabajo + '/'+ nombre_carpeta
    nom_img = os.listdir(path_carpeta)
    print nom_img

def crear_ob_img(nom_img,path_carpeta,ob_img):
    num = 1
    for i in nom_img:
        imagen = Imagen()
        imagen.ruta = path_carpeta + '/' + i
        imagen.num = num
        ob_img.append(imagen)
        num = num + 1

class Imagen:
    def __init__(self):
        self.ruta = ''
        self.num = None
        self.tags = []
    def etiquetar(self,tags):
        for i in tags:
            self.tags.append(
