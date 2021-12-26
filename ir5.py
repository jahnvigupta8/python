from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('C:\Users\Inspiron\Desktop\images/numbers/y0.5.png')
iar = np.asarray(i)

plt.imshow(iar)
print iar
plt.show()
