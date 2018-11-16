from sys import argv
import libreria
  
#------------------------------------------------------------------------------------#

'''
Codigo principal, en este se realiza la comprobacion si se ha introducido por argumento el
tema de las publicaciones, si es asi se procede con la recogida y guardado, si no es asi
se pide a traves de la funcion tkinter al usuario que lo introduzca.
'''
    
#------------------------------------------------------------------------------------#

if len(argv) == 2:
    libreria.recogida(argv[1])
    
else:
    libreria.externo()

