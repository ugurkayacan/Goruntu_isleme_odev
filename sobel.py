import cv2
import numpy as np
import matplotlib.pyplot as plt
foto=cv2.imread("agac.jpg",0)





sobelx = cv2.Sobel(foto,cv2.CV_8U,1,0,ksize=5)  # x
sobely = cv2.Sobel(foto,cv2.CV_8U,0,1,ksize=5)
img_sobel=sobely+sobelx

#FOR DONGUSU İLE

#X

sobel_x=np.zeros((350,545))
sobel_y=np.zeros((350,545))
sonuc=0

K_X=[[-1,0,1],
     [-2,0,2],
     [-1,0,1]]


for i in range(345):
    for j in range(535):
        for z in range(3):
            for k in range(3):

                carpimx=foto[i+z][j+k]*K_X[z][k]
                sonuc+=carpimx

        sobel_x[i][j] = sonuc
        carpim = 0;
        sonuc = 0;


K_Y=[[1,2,1],
     [0,0,0],
     [-1,-2,-1]]

for i in range(345):# out of index hatası verdiği için satır sütun değerleri bir miktar geriye çekildi.
    for j in range(543):
        for z in range(3):
            for k in range(3):

                carpimy=foto[i+z][j+k]*K_Y[z][k]
                sonuc+=carpimy

        sobel_y[i][j]=sonuc
        carpim = 0;
        sonuc = 0;

sobel=sobel_y+sobel_x

cv2.imshow("foto",foto)
cv2.waitKey(0)
cv2.imshow("sobel_foto_opencv",img_sobel)
cv2.waitKey(0)
cv2.imshow("sobel_foto_for",sobel)

"""""
sobel*=-1
yan_yana=np.hstack((foto,img_sobel,sobel))
plt.imshow(yan_yana)
plt.show()
"""
cv2.waitKey(0)