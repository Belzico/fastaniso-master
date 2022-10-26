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


# img,niter=1,kappa=50,gamma=0.1,step=(1.,1.),option=1,ploton=False):
#photo =   fastaniso.anisodiff()
#f = misc.face()
#imageio.imsave('dog.1.jpg', f)
# plt.imshow(f)
# plt.show()


#image = cv2.imread("Boob.jpg")
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
# cv2.imshow("Original",image)
# cv2.waitKey()

# Detección de borde de Laplace
# lap = cv2.Canny(image,100,200)# Detección de borde de Laplace
# lap = np.uint8(np.absolute(lap))## Ir al valor absoluto de vuelta
# cv2.imshow("Laplacian",lap)
# cv2.imwrite('Bordes.png',lap)


#multiple images
rute_up="d:\\escuela\\tesis\\AniDif\\fastaniso-master\\ds_ini"
rute_down="d:\\escuela\\tesis\\AniDif\\fastaniso-master\\ds_final"
print(str(pathlib.Path(__file__).parent.absolute()))
number_of_iterations=100

def image_retrieve():
    rootDir = rute_up
    rootFinal = rute_down
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        
        for fname in fileList:
            # creamos la carpeta asociada a la foto
            if not (os.path.isdir(str(rootFinal)+"\\"+str(fname)[:len(str(fname))-4] + str('_') + str(i))):
                os.mkdir(str(rootFinal)+"\\"+str(fname)[:len(str(fname))-4] + str('_') + str(i))
            # aca cuando metamos concurrencia
            # concurrency_handler()
            print(dirName)
            print("-----------------------")
            print(subdirList)
            print("-----------------------")
            print(fileList)
            print("-----------------------")
            print(fname)
            print("-----------------------")
            result_list=[]
            img_PIL = io.imread(str(dirName)+'\\'+str(fname))

            j=0
            os.chdir(rute_down+'\\'+str(fname)[:len(str(fname))-4]+ str('_') + str(i))
            io.imsave( str(i)+'_ite_'+str(0)+'.jpg', img_PIL)
            

            fastaniso.anisodiff(img_PIL, number_of_iterations,result_list)
            for item in result_list:
                j+=1
                io.imsave(str(i)+'_ite_'+str(j)+'.jpg', result_list[j-1])
                
            i+=1


image_retrieve()
img_PIL = io.imread('fastaniso_master\\leoimage.jpg')
ani = fastaniso.anisodiff(img_PIL, 700)

print(type(img_PIL))
print(img_PIL.dtype)
print(img_PIL.shape)
print(img_PIL.min(), img_PIL.max())
plt.imshow(img_PIL)
io.imsave('wawa700.jpg', ani)
print("a")
