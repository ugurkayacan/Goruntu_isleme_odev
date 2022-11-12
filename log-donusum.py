import cv2
import numpy as np

import matplotlib.pyplot as plt
import math
r=cv2.imread("agac.jpg",0)


def log_donusumu(r,c):
    r=r.astype(float)#renk skalasını 255'in üzerine getirdik.
    s=c*np.log(1+r)
    return s.astype(np.uint8)#resmi tekrar 8bit pozisyonuna getirdik.

def donusum(foto):#belli bir bit düzeyi aralığına sıkışan resmi 0-255 arasında açıyor
    s=foto.astype(float)
    s-=np.min(s)
    s/=np.max(s)

    return (s*255).astype(np.uint8)#resmi 0 ile 255 arasına getirdik
log_foto=log_donusumu(r,c=1)
log_foto=donusum(log_foto)


cv2.imshow("foto",r)
cv2.waitKey(0)
cv2.imshow("log_foto",log_foto)
cv2.waitKey(0)







