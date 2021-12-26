from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            print eachPix
            
            time.sleep(5)

i = Image.open('C:\Users\Inspiron\Desktop\images/numbers/0.1.png')
iar = np.asarray(i)

i2 = Image.open('C:\Users\Inspiron\Desktop\images/numbers/y0.4.png')
iar2 = np.asarray(i2)

i3 = Image.open('C:\Users\Inspiron\Desktop\images/numbers/y0.5.png')
iar3 = np.asarray(i3)

i4 = Image.open('C:\Users\Inspiron\Desktop\images/sentdex.png')
iar4 = np.asarray(i4)

ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()
