import PIL.Image
import os
import tkinter as tk
from tkinter import filedialog as fd
import threading


ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
WIDTH = 200
OUT_PATH = 'ascii_output/'

root = tk.Tk()
root.withdraw()
#mainloop_thread = threading.Thread(target=root.mainloop, daemon=True, name="Mainloop thread")
#mainloop_thread.start()

def resize_image(image, new_width=WIDTH):
    width,height = image.size
    ratio = (height/2) / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def grayify(image):
    grayscale_image = image.convert('L')
    return(grayscale_image)


def pixle_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width=WIDTH):

    path = fd.askopenfilename()
    try:
        image = PIL.Image.open(path)
        print(image.size)
    except:
        print("Select a valid file path.")
        exit()

    new_image_data = pixle_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    name = OUT_PATH + os.path.splitext(os.path.basename(path))[0] + '_ascii.txt'

    with open(name, 'w') as f:
        f.write(ascii_image)
    
    os.system("notepad " + name)

    
main()