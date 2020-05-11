from PIL import Image
import numpy as np

def affine_transform(img, operation):
    dst = np.zeros_like(img)
    cols = img.shape[0]
    rows = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            after = np.array([i, j, 1])
            before = after@np.linalg.inv(operation)
            if (before[0] >= 0) & (before[1] >= 0) & (before[0] < rows) & (before[1] < cols):
                dst[j, i] = img[int(before[1]), int(before[0])]
    return dst

def translate(dx, dy):
    t = np.eye(3)
    t[2, 0] = dx
    t[2, 1] = dy
    return t

def rotation(img, theta, direction="anticlockwise"):
    t = np.eye(3)
    cols = img.shape[0]
    rows = img.shape[1]
    convert = np.array(([1, 0, 0], [0, -1, 0], [cols/2, rows/2, 1]), dtype=np.float32)
    inverse = np.array(([1, 0, 0], [0, -1, 0], [-cols/2, rows/2, 1]), dtype=np.float32)
    if direction=="clockwise":
        theta = theta/180 * np.pi
    elif direction=="anticlockwise":
        theta = - theta/180 * np.pi
    else:
        raise Exception("Error: diretion should be either anticlockwise or clockwise")

    t[0, 0] = np.cos(theta)
    t[0, 1] = np.sin(theta)
    t[1, 0] = -np.sin(theta)
    t[1, 1] = np.cos(theta)
    return inverse@t@convert

def shear(img, step, direction="x"):
    t = np.eye(3)
    cols = img.shape[0]
    rows = img.shape[1]
    convert = np.array(([1, 0, 0], [0, -1, 0], [cols/2, rows/2, 1]), dtype=np.float32)
    inverse = np.array(([1, 0, 0], [0, -1, 0], [-cols/2, rows/2, 1]), dtype=np.float32)

    if direction=="x":
        t[1, 0] = step
    elif direction=="y":
        t[0, 1] = step
    else:
        raise Exception("Error: diretion should be either x or y")
    return inverse@t@convert


if __name__ == '__main__':
    # Create an image
    size = 250
    img_t = np.zeros((size,size))
    for i in range(size):
        if i > size/2:
            for j in range(size):
                if j > size/2:
                    img_t[i, j] = 255.0
        else:
            for j in range(size):
                if j < size/2:
                    img_t[i, j] = 255.0

    Image.fromarray(img_t.astype(np.uint8)).save('./temp1.jpg')
    trans = translate(50, 100)
    R = rotation(img_t, 45, direction="clockwise")
    s = shear(img_t, 0.5)

    result_t = affine_transform(img_t, trans)
    result_R = affine_transform(img_t, R)
    result_s = affine_transform(img_t, s)

    Image.fromarray(result_t.astype(np.uint8)).save('./tempt.jpg')
    Image.fromarray(result_R.astype(np.uint8)).save('./tempR.jpg')
    Image.fromarray(result_s.astype(np.uint8)).save('./temps.jpg')


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
