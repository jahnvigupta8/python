from PIL import Image
import numpy as np

i = Image.open('C:\Users\Inspiron\Desktop\IMG_20160409_220016.jpg')
iar = np.asarray(i)
print iar
