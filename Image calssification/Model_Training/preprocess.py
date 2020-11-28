from keras.preprocessing import image
from PIL import Image, ImageOps
import numpy as np

def resizeImage(srcfile, new_width=32, new_height=32):
    pil_image = Image.open(srcfile)
    pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)
    pil_image_rgb = pil_image.convert('RGB')
    return np.asarray(pil_image_rgb).flatten()
