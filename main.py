from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from numpy import column_stack



def see_results():
    img_name = image_entry.get()
    wm_name = watermark_entry.get()
    image = Image.open(img_name)
    watermark = Image.open(wm_name)
    img_w, img_h = image.size
    wm_w, wm_h = watermark.size

    # resize watermark with respect to image
    wm_resize_percentage = int(wm_resize_entry.get())
    wm_sizes = (int(wm_w*wm_resize_percentage/100), int(wm_h*wm_resize_percentage/100))
    resized_wm = watermark.resize(wm_sizes, Image.ANTIALIAS)

    # find the center of the image
    how_top = int(text_top_entry.get())
    how_left = int(text_left_entry.get())
    image_center = (int(img_w/how_left), int(img_h/how_top))

    image.paste(resized_wm, image_center, resized_wm)
    image.show()
    return image

def save_results():
    see_results().save("watermarked.png")



# Logo Size Setup
logo = Image.open("watermark_black.png")
logo = logo.resize((200,100), Image.ANTIALIAS)


#-------UI SETUP----------
window = Tk()
window.title("Watermark Adder")
window.config(padx=50, pady=50)

#logo
canvas = Canvas(height=150, width=200)
logo_img = ImageTk.PhotoImage(logo)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# labels
image_label = Label(text="Original Photo File Path: ")
image_label.grid(row=1, column=0)
watermark_label = Label(text="Watermark to add File Path: ")
watermark_label.grid(row=2, column=0)
wm_resize_label = Label(text="Label resize percentile: ")
wm_resize_label.grid(row=3, column=0)
text_top_label = Label(text="How bottom 0-100(bigger=more bottom): ")
text_top_label.grid(row=4, column=0)
text_left_label = Label(text="How left 0-100(bigger=more left): ")
text_left_label.grid(row=5, column=0)

#entries
image_entry = Entry(width=35)
image_entry.grid(row=1, column=1, columnspan=2)
image_entry.insert(0, "photo.jpg")
watermark_entry = Entry(width=35)
watermark_entry.grid(row=2, column=1, columnspan=2)
watermark_entry.insert(0, "watermark_white.png")
wm_resize_entry = Entry(width=35)
wm_resize_entry.grid(row=3, column=1, columnspan=2)
wm_resize_entry.insert(0, "20")
text_top_entry = Entry(width=35)
text_top_entry.grid(row=4, column=1, columnspan=2)
text_top_entry.insert(0, "10")
text_left_entry = Entry(width=35)
text_left_entry.grid(row=5, column=1, columnspan=2)
text_left_entry.insert(0, "100")

# buttons
see_result_button = Button(text="See Result", command=see_results)
see_result_button.grid(row=6, column=1)
save_result_button = Button(text="Save Result", command=save_results)
save_result_button.grid(row=6, column=2)

window.mainloop()