# -*- coding: utf-8 -*-
import os
from Tkinter import *
from PIL import Image


class Imagen:
    def __init__(self):
        self.nom = ''
        self.ruta = ''
        self.num = None
        self.tags = []

class button:
  def __init__(self,root,text,comand):
    self.button = Button(root,text=text,comand=comand)
    self.state = None


#Funcion que revisa si en ella hay otras carpetas interiorer

def comprobar_carpeta(path_carpeta):
  path_carpetas = []
  path_carpetas.append(path_carpeta)
  elementos_carpeta = os.listdir(path_carpeta)
  for i in elementos_carpeta:
    if os.path.isdir(path_carpeta+"/"+i)==True:
      path_carpetas.append(path_carpeta+"/"+i)
  return path_carpetas

    #crea una variable que contiene una lista de subcarpetas de la carpeta indicada si existen, de las cuales se van a clasificar las imagenes que contenga.

#Funcion que me crea lista de nombres de archivos a partir del path de la carpeta respectiva y la devuelve
def nom_files(path_carpeta):
    nom_img_temp = os.listdir(path_carpeta)
    nom_img = []
    for i in nom_img_temp:
        if os.path.isdir(path_carpeta + "/"+i)==False:
            nom_img.append(i)
    return nom_img

#Funcion que crea objeto imagen por cada imagen de carpeta a partir de sus nombres (lista nom_img) y devuelve una la lista de tales objetos
def crear_ob_img(nom_img,path_carpeta):
    num = 1
    ob_img = []
    for i in nom_img:
        imagen = Imagen()
        imagen.nom = i
        imagen.ruta = path_carpeta + '/' + i
        imagen.num = num
        ob_img.append(imagen)
        num = num + 1
    return ob_img

###Hasta aquí terminana las funciones de manipulacion interna de las imagenes

#Funcion que agrega una etiqueta a un objetos por su número de identificacion
def tag(numID,tag,ob_img):
    for i in ob_img:
        if i.num == numID:
            i.tags.append(tag)

#Funcion que abre en el formato gif a una imagen
def abrir_img(path_img):
  path_temp = path_img +".gif"
  try:
      Image.open(path_img).save(path_temp)
  except IOError:
      print("No se puede convertir la imagen")
  imagen1 = PhotoImage(file=path_temp)
  return imagen1

def mostrar_interfaz(ob_img):
    num = buscar_avance(ob_img) ## Falta definir esta funcion
    ventana = Tk()
    ventana.title("Clasificador de Imagenes")
    ventana.config(bg="gray")
    ventana.geometry("600x700")

    Label = Label(ventana, image = abrir_img(ob_img[0].ruta))
    Label.grid(row=1,column=2)

    boton_verdes = button(ventana,"Ojos verdes")
    boton_verdes.button.grid(row=1,column=1)


    boton_negros = button(ventana, "Ojos negros")
    boton_negros.button.grid(row=1,column=2)

    boton_azules = button(ventana, "Ojos azules")
    boton_azules.button.grid(row=1,column=3)

    ventana.mainloop()

###PROGRAMA PRINCIPAL###

ob_img = []
path_carpeta = raw_input("introduce la direcion de la carpeta que contiene las imagenes")

path_carpetas = comprobar_carpeta(path_carpeta)
print path_carpetas
for i in path_carpetas:
    nom_img_temp = nom_files(i)
    ob_img_temp = crear_ob_img(nom_img_temp,i)
    for j in ob_img_temp:
        ob_img.append(j)
for i in ob_img:
    print [i.num,i.nom,i.ruta]
