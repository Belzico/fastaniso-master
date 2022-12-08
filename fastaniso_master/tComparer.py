import fastaniso
from scipy import misc
import imageio
import matplotlib.pyplot as plt
from skimage import io
import cv2
import numpy as np
import os
#import generateDS.my_globals as globals
import pathlib


rute_up = "d:\\escuela\\tesis\\AniDif\\fastaniso-master\\images_perona"
rute_down = "d:\\escuela\\tesis\\AniDif\\fastaniso-master\\final_fasta"
print(len(rute_down))
rute_save = "d:\\escuela\\tesis\\AniDif\\fastaniso-master\\finalt\\"

print(str(pathlib.Path(__file__).parent.absolute()))

error_list=[]
def compareImage(a,b):
    if(len(a)!=len(b)):
        return 1000000000
    res=np.zeros_like(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j]=abs(abs(a[i][j])-abs(b[i][j]))
            
   
    sum=0
    for i in range(len(res)):
        for j in range(len(res[0])):
            sum+=res[i][j]
    return  sum/(len(res)*len(res[0]))   

def image_retrieve():
    rootPerona = rute_up
    rootFasta = rute_down
    i = 0
    count=0
    result1={}
    result2={}
    for dirName, subdirList, fileList in os.walk(rootPerona):

        for fname in fileList:
            # creamos la carpeta asociada a la foto
            #if not (os.path.isdir(str(rootFinal)+"\\"+str(fname)[:len(str(fname))-4] + str('_') + str(i))):
            #    os.mkdir(str(rootFinal)+"\\"+str(fname)
            #             [:len(str(fname))-4] + str('_') + str(i))
            # aca cuando metamos concurrencia
            # concurrency_handler()
            #print(dirName)
            print("-----------------------")
            #print(subdirList)
            print("-----------------------")
            #print(fileList)
            print("-----------------------")
            print(fname)
            print("-----------------------")
            
            result1[fname]=(1000000,"None")
            result2[fname]=(1000000,"None")
            a = io.imread(str(dirName)+'\\'+str(fname))
            b=0
            for dirName2, subdirList2, fileList2 in os.walk(rootFasta):
                
                if dirName2== rootFasta+"\\circ_1.4reduce_t5":
                    print("a")
                if fname=="circ_1.4reduce_t5.jpg":
                    print("a")
                    
                for fname2 in fileList2:
                    sub=dirName2[len(rute_down)+1:len(dirName2)]+".jpg"
                    
                    if dirName2==rute_down+"\\ini_cir_200x200" or dirName2==rute_down+"\\ini_cir_30x30":
                            
                        b = io.imread(str(dirName2)+'\\'+str(fname2))
                        diff= compareImage(a,b)
                        #print(result2[fname])
                        if diff<result2[fname][0]:
                            result2[fname]=(diff,b,fname2)
                    
                    if sub[0:10] ==  fname[0:10] :
                        
                        b = io.imread(str(dirName2)+'\\'+str(fname2))
                        diff= compareImage(a,b)
                        #print(result1[fname])
                        if diff<result1[fname][0]:
                            result1[fname]=(diff,b,fname2)
                        
                   
                        
            
            if  result1[fname][1]=="None":
                continue
            if  result2[fname][1]=="None":
                continue
            io.imsave(rute_save+str(count)+fname, a)
            io.imsave(rute_save+str(count)+result1[fname][2], result1[fname][1])
            io.imsave(rute_save+str(count)+result2[fname][2], result2[fname][1])
            error_list.append((fname,result1[fname][0],result2[fname][0]))
            count+=1
            
    
            
           


image_retrieve()
filehandler = open("error_list", 'wt')
data = str(error_list)
filehandler.write(data)
filehandler.closed()
print("a")