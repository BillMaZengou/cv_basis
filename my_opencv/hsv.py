from PIL import Image
import numpy as np
from grey import create_image

def rgb_to_hsv(img):
    cols, rows, channels = img.shape
    hsv = np.zeros((cols, rows, channels))

    for i in range(cols):
        for j in range(rows):
            r = img[i, j, 0]
            g = img[i, j, 1]
            b = img[i, j, 2]
            # V
            V = max([r, g, b])
            # S
            if V == 0:
                S = 0
            else:
                S = (V - min([r, g, b])) / V
            # H
            if S == 0:
                H = 0
            else:
                if V == r:
                    H = 60 * (g - b) / (V - min([r, g, b]))
                elif V == g:
                    H = 120 + 60 * (b - r) / (V - min([r, g, b]))
                else:
                    H = 240 + 60 * (r - g) / (V - min([r, g, b]))

                if H < 0:
                    H += 360

            hsv[i, j, :] = [H, S, V]
    return hsv

if __name__ == '__main__':
    img_t = create_image()
    result_hsv = rgb_to_hsv(img_t)
    Image.fromarray(result_hsv.astype(np.uint8)).save('./tempHSV.jpg')
