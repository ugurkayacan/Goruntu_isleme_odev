import cv2
import numpy as np
import matplotlib.pyplot as plt
foto=cv2.imread("agac.jpg")
# numpy ile
"""
def fotograf_negatif(foto):
    L=  np.max(foto)
    negatif_foto=L-foto
    return negatif_foto


negatif_foto=fotograf_negatif(foto)
cv2.imshow("fotograf-negatif",negatif_foto)
cv2.waitKey(0)
cv2.imshow("fotograf",foto)
cv2.waitKey(0)
yan_yana=np.hstack((foto,negatif_foto))
plt.imshow(yan_yana)
"""
#for dögüsü ile
print(np.max(foto))
foto_negatif=cv2.imread("agac.jpg")
for x in range(350):
    for y in range(545):

        #foto_negatif[x,y,:]=np.max(foto_negatif)-foto_negatif[x,y,:]
        foto_negatif[x, y,:] = np.max(foto_negatif) - foto_negatif[x, y,:]
        print(foto_negatif[x, y, :])

cv2.imshow("fotograf-negatif",foto_negatif)
cv2.waitKey(0)
cv2.imshow("fotograf",foto)
cv2.waitKey(0)
print(foto_negatif[x, y,:])
"""
yan_yana=np.hstack((foto,foto_negatif))
plt.imshow(yan_yana)
plt.show()
"""
cv2.waitKey(0)
cv2.destroyAllWindows()