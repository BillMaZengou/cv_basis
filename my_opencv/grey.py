from PIL import Image
import numpy as np

def rgb_to_grey(img):
    cols = img.shape[0]
    rows = img.shape[1]

    grey = np.zeros((cols, rows))
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    grey[:, :] = 0.229*r + 0.587*g + 0.114*b
    return grey

def grey_to_rgb(img):
    if len(img.shape) != 2:
        print("Input should be a greyscale image")
    else:
        dst = np.zeros((img.shape[0], img.shape[1], 3))
        dst[:, :, 0] = img[:, :]
        dst[:, :, 1] = img[:, :]
        dst[:, :, 2] = img[:, :]
        return dst

def generate_color():
    r = np.random.randint(0, 255)
    g = np.random.randint(0, 255)
    b = np.random.randint(0, 255)
    return r, g, b

def create_image():
    # Create an image
    size = 250
    img_t = np.zeros((size,size, 3))
    r_1, g_1, b_1 = generate_color()
    r_2, g_2, b_2 = generate_color()
    r_3, g_3, b_3 = generate_color()
    r_4, g_4, b_4 = generate_color()
    for i in range(size):
        if i > size/2 and i <= size * 3/4:
            for j in range(size):
                if j > size * 3/4:
                    img_t[i, j, 0] = r_1
                    img_t[i, j, 1] = g_1
                    img_t[i, j, 2] = b_1
                elif j > size/2 and j <= size * 3/4:
                    img_t[i, j, 0] = 255.0
                    img_t[i, j, 1] = 255.0
                    img_t[i, j, 2] = 255.0
        elif i > size * 3/4:
            for j in range(size):
                if j > size/2 and j <= size * 3/4:
                    img_t[i, j, 0] = r_2
                    img_t[i, j, 1] = g_2
                    img_t[i, j, 2] = b_2
                elif j > size * 3/4:
                    img_t[i, j, 0] = 255.0
                    img_t[i, j, 1] = 255.0
                    img_t[i, j, 2] = 255.0
        elif i > size/4 and i <= size/2:
            for j in range(size):
                if j < size/4:
                    img_t[i, j, 0] = r_3
                    img_t[i, j, 1] = g_3
                    img_t[i, j, 2] = b_3
                elif j >= size/4 and j < size/2:
                    img_t[i, j, 0] = 255.0
                    img_t[i, j, 1] = 255.0
                    img_t[i, j, 2] = 255.0
        else:
            for j in range(size):
                if j >= size/4 and j < size/2:
                    img_t[i, j, 0] = r_4
                    img_t[i, j, 1] = g_4
                    img_t[i, j, 2] = b_4
                elif j < size/4:
                    img_t[i, j, 0] = 255.0
                    img_t[i, j, 1] = 255.0
                    img_t[i, j, 2] = 255.0

    Image.fromarray(img_t.astype(np.uint8)).save('./temp1.jpg')
    return img_t

if __name__ == '__main__':
    img_t = create_image()
    result_grey = rgb_to_grey(img_t)
    Image.fromarray(result_grey.astype(np.uint8)).save('./tempG.jpg')

    # dst = grey_to_rgb(result_grey)
    # print(result_grey)
    # print(dst)


"""""""""
 ________  _______   ________  ___  ___  ___  _______   _____ ______   ________
|\   __  \|\  ___ \ |\   __  \|\  \|\  \|\  \|\  ___ \ |\   _ \  _   \|\   __  \
\ \  \|\  \ \   __/|\ \  \|\  \ \  \\\  \ \  \ \   __/|\ \  \\\__\ \  \ \  \|\  \
 \ \   _  _\ \  \_|/_\ \  \\\  \ \  \\\  \ \  \ \  \_|/_\ \  \\|__| \  \ \   __  \
  \ \  \\  \\ \  \_|\ \ \  \\\  \ \  \\\  \ \  \ \  \_|\ \ \  \    \ \  \ \  \ \  \
   \ \__\\ _\\ \_______\ \_____  \ \_______\ \__\ \_______\ \__\    \ \__\ \__\ \__\
    \|__|\|__|\|_______|\|___| \__\|_______|\|__|\|_______|\|__|     \|__|\|__|\|__|
                              \|__|
"""""""""
