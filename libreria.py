import tkinter
from tkinter import simpledialog
import feedparser
  
#------------------------------------------------------------------------------------#

'''
En la funcion externo se utiliza la libreria tkinter para recopilar la informacion sobre
que seccion seleccionar del usuario. 
'''

#------------------------------------------------------------------------------------#

def externo ():      
    
    tkinter.messagebox.showinfo("Opciones", "Las opciones disponibles son: accion, humor, horror")
    pagina = simpledialog.askstring("Entrada", "De que pagina quieres guardar los datos")

    recogida(pagina)        
            
#------------------------------------------------------------------------------------#

'''
En la funcion recogida se utiliza la eleccion del usuario ya sea por tkinter o por argv
para, usando la direccion del diccionario, recoger el feed xml de la pagina.
'''

#------------------------------------------------------------------------------------#
    
def recogida (decision):
    
    paginas={'accion':'https://www.fictionpress.com/atom/l/?&cid1=1531&r=10&s=1','humor':'https://www.fictionpress.com/atom/l/?&cid1=919&r=103&s=1','horror':'https://www.fictionpress.com/atom/l/?&cid1=314&r=103&s=1'}
    
    pagina1 = feedparser.parse(paginas[decision])['entries']
    
    guardado (pagina1,decision)
    
#------------------------------------------------------------------------------------#

'''
En la funcion guardado se le pide al usuario usando la funcion tkinter que introduzca 
cual sera el nombre del archivo de destino y cuantas publicaciones desea guardar y realiza
el guardado del archivo.
Ya que la seccion summary del feed de FictionPress.com devuelve un bloque html de debe buscar
el texto resumen mediante la funcion split.
'''
    
#------------------------------------------------------------------------------------#

def guardado (pagina,seccion):  
    
    tkinter.messagebox.showinfo("Archivo", "Escriba el nombre del archivo y cuantos resumenes quieres.")    
    archivo = open(simpledialog.askstring("Entrada", "Nombre del archivo a guardar."),"w")
    cuantos = int(simpledialog.askstring("Entrada", "Cuantos resumenes."))
      

    archivo.write("Estos son los "+str(cuantos)+" primeros trabajos mas actualizados de la pagina Fictionpress en la seccion de " + seccion)        
    archivo.write(" \n---------------------------------------------- \n ")  
    
    n=0    
    
    while n < cuantos:
        
        resumen=pagina[n].summary.split('>')
        archivo.write(pagina[n].title + " \n \n " + resumen[9])        
        archivo.write(" \n---------------------------------------------- \n ")  
        n += 1
    
    archivo.close()
        
#------------------------------------------------------------------------------------#