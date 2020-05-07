from PIL import Image
import numpy as np

def scale(img, x_fac, y_fac, interpolation="NN"):
    x, y = img.shape
    x_new = int(x * x_fac)
    y_new = int(y * y_fac)

    if interpolation=="NN":
        scaled_img = np.zeros((x_new, y_new))
        for i in range(x_new):
            for j in range(y_new):
                scaled_img[i, j] = img[int(i//x_fac), int(j//y_fac)]
        return scaled_img


if __name__ == '__main__':
    # Create an image
    size = 50
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

    scale_img = scale(img_t, 1.5, 1.5, interpolation="NN")
    Image.fromarray(scale_img.astype(np.uint8)).save('./temp2.jpg')
    print("The original size is {}, and the size after scaling is {}".format(img_t.shape, scale_img.shape))
