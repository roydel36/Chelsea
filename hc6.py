#name: Roy Delgado
#email: roy.delgado63@myhunter.cuny.edu
#HC 6: Highlighted Map

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('drippy.png')

#height = img.shape[0]
#width = img.shape[1]
#print(height)
#print(width)

img[:443.3,:,3] = 0.5
img[784:,:,3] = 0.5
img[392:784,:443.3,3] = 0.5
img[392:784,-443:,3] = 0.5

plt.imshow(img)
plt.show()

plt.imsave('chelsea.png', img)


