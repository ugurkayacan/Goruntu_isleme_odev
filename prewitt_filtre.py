import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
foto=cv2.imread("agac.jpg",0)



prewit_x=np.zeros((350,545)) #0 matrisler oluşturuldu
prewit_y=np.zeros((350,545))
sonuc=0
satir=350
sutun=545
K_X=[[-1,0,1],
     [-1,0,1],
     [-1,0,1]]


for i in range(satir-3):#out of index hatası verdiğinden dolayı satır ve sütun değerlerinde değişikliğe gidildi.
    for j in range(sutun-3):
        for z in range(3):
            for k in range(3):

                carpimx=foto[i+z][j+k]*K_X[z][k]
                sonuc+=carpimx

        prewit_x[i+1][j+1] = sonuc
        carpim = 0;
        sonuc = 0;


K_Y=[[1,1,1],
     [0,0,0],
     [-1,-1,-1]]
carpim = 0;
sonuc = 0;
for i in range(satir-3):
    for j in range(sutun-3):
        for z in range(3):
            for k in range(3):

                carpimy=foto[i+z][j+k]*K_Y[z][k]
                sonuc+=carpimy

        prewit_y[i+1][j+1]=sonuc
        carpim = 0;
        sonuc = 0;

prewit=prewit_y+prewit_x


cv2.imshow("foto",foto)
cv2.waitKey(0)

cv2.imshow("prewit_foto_for",prewit)
cv2.waitKey(0)
