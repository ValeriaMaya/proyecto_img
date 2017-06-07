#Se debe crear la carpets de imagenes sobre el path en el que se este trabajando
import os
from Tkinter import *
from PIL import Image

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

#Funcion queme crea lista de nombres de archivos
def nom_file(nombre_carpeta):
    global path_carpeta
    global nom_img
    path_carpeta = directorio_trabajo + '/'+ nombre_carpeta
####    ## Ojo este return forza a salir de la funcion el codigo siguiente ya no se ejecuta
    return path_carpeta
    nom_img = os.listdir(path_carpeta)
    return nom_img


#Funcion que crea objeto imagen por cada imagen de carpeta
def crear_ob_img():
    global ob_img
    global path_carpeta
    global nom_img
    num = 1
    for i in nom_img:
        imagen = Imagen()
        imagen.nom = i
        imagen.ruta = path_carpeta + '/' + i
        imagen.num = num
        ob_img.append(imagen)
        num = num + 1

class Imagen:
    def __init__(self):
        self.nom = ''
        self.ruta = ''
        self.num = None
        self.tags = []

def tag(numID,tag,ob_img):
    for i in ob_img:
        if i.num == numID:
            i.tags.append(tag)
def main():
    ### ELiminar este ciclo para utilizar los eventos de la ventana
    for i in ob_img:
        im_temp = i
        imagen =  Image.open(i.ruta())
        try:
            Image.open(i.ruta()).save(i.ruta()+".gif")
        except IOError:
            print("No se puede convertir la imagen")
        imagen1 = PhotoImage(file=i.ruta()+".gif")
        ventana = Tk()
        ventana.title("Clasificador de Imagenes")
        ventana.config(bg="gray")
        ventana.geometry("600x700")

        Label = Label(ventana,image=imagen1)
        Label.grid(row=2,column=1)

        boton_verdes = Bottom(ventana, text="Ojos verdes", command = tag(im_temp,"Ojos verdes",ob_img))
        boton_verdes.grid(row=1,column=1)

        boton_negros = Bottom(ventana, text="Ojos negros", command = tag(im_temp,"Ojos negro",ob_img))
        boton_negros.grid(row=1,column=2)

        boton_azules = Bottom(ventana, text="Ojos azules", command = tag(im_temp,"Ojos azules",ob_img))
        boton_azules.grid(row=1,column=2)

        ventana.mainloop()
  
