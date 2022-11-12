import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


foto=cv2.imread("agac.jpg")

c=1
gamma=4 #3,4,5
def donusum(foto):
    s=foto.astype(float)
    s-=np.min(s)
    s/=np.max(s)
    return (s*255).astype(np.uint8)#resmi 0 ile 255 arasına getirdik

def gamma_donusumu(r,c,gamma):
    r=r.astype(float)
    s=c*r**gamma
    s=donusum(s)
    return s

gamma_donusmu_foto=gamma_donusumu(foto,c,gamma)

yan_yana=np.hstack((foto,gamma_donusmu_foto))
plt.imshow(yan_yana)
plt.show()
cv2.waitKey(0)


