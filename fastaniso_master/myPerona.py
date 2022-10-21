import fastaniso
from scipy import misc
import imageio
import matplotlib.pyplot as plt
from skimage import io
import cv2
import numpy as np



# img,niter=1,kappa=50,gamma=0.1,step=(1.,1.),option=1,ploton=False):
#photo =   fastaniso.anisodiff()
#f = misc.face()
#imageio.imsave('dog.1.jpg', f)
#plt.imshow(f)
#plt.show()


#image = cv2.imread("Boob.jpg")
#image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
#cv2.imshow("Original",image)
#cv2.waitKey()

# Detección de borde de Laplace
#lap = cv2.Canny(image,100,200)# Detección de borde de Laplace
#lap = np.uint8(np.absolute(lap))## Ir al valor absoluto de vuelta
#cv2.imshow("Laplacian",lap)
#cv2.imwrite('Bordes.png',lap)



img_PIL = io.imread('boob.jpg')
ani=fastaniso.anisodiff(img_PIL,100)

print(type(img_PIL))
print(img_PIL.dtype)
print(img_PIL.shape)
print(img_PIL.min(), img_PIL.max())
plt.imshow(img_PIL)
io.imsave('boob100.jpg',ani)
print("a")


