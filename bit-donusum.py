import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
foto=cv2.imread("agac2.jpg",0)
print(foto.dtype)
cv2.imshow("foto",foto)
a=np.min(foto)
b=np.max(foto)
print("min:",a)
print("max:",b)
print(foto)

def donusum(foto):# fotoğraf 16 bit düzeyine çekildi
    s=foto.astype(float)
    s-=np.min(s)
    s/=np.max(s)
    return (s*65535)  # 2^32,2^64 ....
foto=donusum(foto)
a=np.min(foto)
b=np.max(foto)
print("min:",a)
print("max:",b)
print(type(foto))
print(foto)
cv2.imshow("foto",foto)
cv2.waitKey(0)