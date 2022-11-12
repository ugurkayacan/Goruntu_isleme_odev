import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

foto=cv2.imread("nokta_resim.jpg")
foto2=cv2.imread("nokta_resim.jpg")
for k in range (3):
    for i in range(1200):
        for j in range(1600):
            if foto2[i,j,k]<150:
                foto2[i,j,k]-=80
            else:
                continue



yan_yana=np.hstack((foto,foto2))
plt.imshow(yan_yana)
plt.show()
cv2.waitKey(0)