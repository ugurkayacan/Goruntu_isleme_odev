import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
foto=cv2.imread("agac.jpg",0)
#open cv ile

kernelx=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
kernely=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

img_prewitx=cv2.filter2D(foto,-1,kernelx)
img_prewity=cv2.filter2D(foto,-1,kernely)
img_prewit=img_prewity+img_prewitx

#for döngüsü kullanarak:

prewit_x=np.zeros((350,545)) #0 matrisler oluşturuldu
prewit_y=np.zeros((350,545))
sonuc=0

K_X=[[-1,0,1],
     [-1,0,1],
     [-1,0,1]]


for i in range(345):
    for j in range(535):
        for z in range(3):
            for k in range(3):

                carpimx=foto[i+z][j+k]*K_X[z][k]
                sonuc+=carpimx

        prewit_x[i][j] = sonuc
        carpim = 0;
        sonuc = 0;


K_Y=[[1,1,1],
     [0,0,0],
     [-1,-1,-1]]
carpim = 0;
sonuc = 0;
for i in range(345):
    for j in range(543):
        for z in range(3):
            for k in range(3):

                carpimy=foto[i+z][j+k]*K_Y[z][k]
                sonuc+=carpimy

        prewit_y[i][j]=sonuc
        carpim = 0;
        sonuc = 0;

prewit=prewit_y+prewit_x


cv2.imshow("foto",foto)
cv2.waitKey(0)
cv2.imshow("prewit_foto_opencv",img_prewit)
cv2.waitKey(0)
cv2.imshow("prewit_foto_for",prewit)
cv2.waitKey(0)