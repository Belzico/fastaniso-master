import os
import my_globals as globals
import pathlib
import time
import random
import threading

#clase que tiene los parametros
class Parameters2():
    def __init__(self):
        self.value = True
        self.edge = "Scharr"
        self.coeff = "Perona and Malik II"
        #cantidad de iteraciones
        self.t = 9
        self.updb = 0.1765
        self.updf = 0.0179
        self.sigma = 1
        self.num_seg = 8






def image_retrieve():
    rootDir=globals.root_dir
    rootFinal=globals.root_dir 
    for dirName, subdirList, fileList in os.walk(rootDir):
        i=0
        for fname in fileList:
            #creamos la carpeta asociada a la foto
            os.mkdir( str(rootFinal)+"\\"+str(fname) + str(i))
            concurrency_handler()
            


def concurrency_handler():
    
    globals.my_lock.acquire()
    
    while globals.max_threads==3:
        time.sleep(1+random.randint(1,10)/10)
    threading.Timer(1,image_dir_create,["b"]).start() 
    globals.my_lock.release()

#pasar una funcion
def image_dir_create(method_difusion,number_of_img=4):
    
    print("done")
    print("a")
    


print(str(pathlib.Path(__file__).parent.absolute()))
print("a")