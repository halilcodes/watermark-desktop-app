from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("elcin_img.jpeg")

# open image in photo viewer
# img.show()
# to get x and y dims
plt.imshow(img)

wm_white = Image.open("watermark_white.png")

print(img.size) #output: (768, 1024)
wm_size = (int(img.size[0]/2), int(img.size[1]/2))
wm_white.thumbnail(wm_size)



copied_img = img.copy()

copied_img.paste(wm_white, (int(img.size[0]/2), int(img.size[1]/2)))

copied_img.show()
plt.imshow(copied_img)
copied_img.save("watermarked.png")

# this one does not have transparent background... so im gonna try with openCV