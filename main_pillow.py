from PIL import Image

image = Image.open("elcin_img.jpeg")
watermark = Image.open("watermark_white.png")


# resize watermark with respect to image
w_resize_percentage = 70
h_resize_percentage = 10
img_w, img_h = image.size
print(img_w, img_h)
wm_sizes = (int(img_w*w_resize_percentage/100), int(img_h*h_resize_percentage/100))
resized_wm = watermark.resize(wm_sizes, Image.ANTIALIAS)

# find the center of the image
how_top = 10
how_left = 100
image_center = (int(img_w/how_left), int(img_h/how_top))

image.paste(resized_wm, image_center, resized_wm)
image.show()

#image.save("watermarked.png")