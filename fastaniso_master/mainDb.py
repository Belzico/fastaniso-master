#import generateDS.my_globals as globals
#import generateDS.methods as methods
#from PIL import Image
import matplotlib
import cv2
from PIL import Image
import fastaniso
import numpy as np


def div_matrix(matrix_3x,number_x):
    for i in matrix_3x:
        for j in matrix_3x:
            for k in matrix_3x:
                pass
    
def mul_matrix(matrix_3x,number_x):
    pass
def pow_matrix(matrix_3x,number_x):
    pass

def main():
    #img = cv2.imread("leoimage.jpg", cv2.IMREAD_GRAYSCALE)
    # print(cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow("Input")
    #cv2.imshow("Input", img)
    #cv2.imshow('graycsale image',img)
    # print("a")
    # cv2.im
    img_PIL = Image.open(r'leoimage.jpg')
    img_PIL.show()
    # img,niter=1,kappa=50,gamma=0.1,step=(1.,1.),option=1,ploton=False):
    ani = fastaniso.anisodiff(img_PIL)
    img_PIL.save(ani)
    pass


#np_array = np.array([[[1,1,1],[2,2,2],[3,3,3]],[[1,1,1],[2,2,2],[3,3,3]],[[1,1,1],[2,2,2],[3,3,3]]])
# second_np_array=np.zeros_like(np_array)
np_array = np.array([[1, 1,1], [3, 4,5]])
second_np_array = np.zeros_like(np_array)
third_np_array = np.zeros_like(np_array)

second_np_array[:-1, :] = np.diff(np_array, axis=0)

third_np_array[:, :-1] = np.diff(np_array, axis=1)

print(np.e**3)

print(np_array)
print("--------")
print(np.exp(np_array) )
print("--------")
print(np_array/2)
print("--------")
print(second_np_array)
print("--------")
print(third_np_array)
main()
print("a")


