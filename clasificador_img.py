# -*- coding: utf-8 -*-

import os
from Tkinter import *
from PIL import Image,ImageTk


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
    if tag ! = '':
        for i in ob_img:
            if i.num == numID:
                i.tags.append(tag)

#Funcion que abre en el formato gif a una imagen
def abrir_img(path_img):
  img = Image.open(path_img)
  tkimage = ImageTk.PhotoImage(img)
  return tkimage

def buscar_avance(path_carpeta):
    dirct = os.listdir(path_carpeta)
    avance = open('avance.txt','a')
    s = len(avance.readlines())
    return s

def guardar_avance(avance):
    archivo = open("avance.txt", "w")
    for i in avance:
        nueva_linea = [i.nom,i.tags]
        contenido = archivo.read()
        final_de_archivo = archivo.tell()
        archivo.write(nueva_linea)
        archivo.seek(final_de_archivo)
        archivo.close()

def actualizarLabel(clave,lable,num,ob_img):
    if clave == anterior:
        if num-1>=0:
            new_label = label.config(image = abrir_img(ob_img[num-1].ruta))
            mostrar_interfaz(ob_img,path_carpeta,new_label)

        else:
            print "No hay imagen anterior"
    else:
        if num+1< len(ob_img):
            new_label = label.config(image = abrir_img(ob_img[num+1].ruta))
            mostrar_interfaz(ob_img,path_carpeta,new_label)
        else:
            print "No hay imagen siguiente"

def mostrar_interfaz(ob_img,label):
    avance = []
    for i in ob_img:
        if ob_img[i].tags!=[]:
            avance.append([i.nom,i.tags])
    ventana = Tk()
    ventana.title("Clasificador de Imagenes")
    ventana.config(bg="gray")
    ventana.geometry("600x700")

    label = label
    label.grid(row=1,column=2)

    anterior = Button(root,text="anterior",relief=FLAT)
    anterior.bind(<Button-1>, actualizarLabel(anterior,label,num,ob_img))
    anterior.grid(row=3,column=2)


    siguiente = Button(root,text="siguiente",relief=FLAT)
    siguiente.bind(<Button-1>, actualizarLabel(siguiente,label,num,ob_img) )
    siguiente.grid(row=3,column=2)

    caja = Entry(ventana,textvariable = nueva_etiqueta)
    caja.grid(row=2,column=2)
    etiqueta = caja.get()

    enviar = Button(root,text="Etiquetar",relief=FLAT)
    enviar.bind(<Button-1>, tag(ob_img[num].num,etiqueta,ob_img) )
    enviar.grid(row=2,column=3)

    save = Button(root,text="Guardar",relief=FLAT)
    save.bind(<Button-1>, guardar_avance(avance) )
    save.grid(row=3,column=2)

    finish = Button(root,text="Salir",relief=FLAT)
    finish.bind(<Button-1>, ventana.quit )
    finish.grid(row=3,column=2)

    ventana.mainloop()

def img_buscar(etiqueta,ob_img):
    img_para_mostrar = []
    for i in ob_img:
        for j in ob_img[i].tags:
            if j == etiqueta:
                img_para_mostrar.append(i)
    return img_para_mostrar


def buscador(ob_img):
    ventana = Tk()
    ventana.title("Clasificador de Imagenes")
    ventana.config(bg="gray")
    ventana.geometry("600x700")

    caja = Entry(ventana,textvariable = etiqueta)
    caja.grid(row=2,column=2)

    ventana.mainloop()

    img_para_mostrar = []
    etiqueta = caja.get()
    if etiqueta != '':
        for i in ob_img:
            for j in ob_img[i].tags:
                if j == etiqueta:
                    img_para_mostrar.append(i)
        ventana.quit()
        mostrar_etiquetadas(img_para_mostrar,0)


def mostrar_etiquetadas(img_para_mostrar,n):
    if n<len(img_para_mostrar):
            if n<0:
                print "No hay imagenes"
            else:
                ventana = Tk()
                ventana.title("Etiquetadas")
                ventana.config(bg="gray")
                ventana.geometry("600x700")

                label = Label(ventana, image = abrir_img(img_para_mostrar[n].ruta))
                label.grid(row=3,column=2)

                anterior = Button(root,text="anterior",relief=FLAT)
                anterior.bind(<Button-1>, mostrar_etiquetadas(img_para_mostrar,n-1))
                anterior.grid(row=4,column=1)

                siguiente = Button(root,text="siguiente",relief=FLAT)
                siguiente.bind(<Button-1>, mostrar_etiquetadas(img_para_mostrar,n+1))
                siguiente.grid(row=4,column=3)

                finish = Button(root,text="Salir",relief=FLAT)
                finish.bind(<Button-1>, ventana.quit )
                finish.grid(row=6,column=3)

                ventana.mainloop()
        else:
            print "No hay imagenes"

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

num = buscar_avance(path_carpeta)
label = Label(ventana, image = abrir_img(ob_img[num].ruta))
if num < len(ob_img):
    mostrar_interfaz(ob_img, path_carpeta,label)
else:
    buscador(ob_img)
