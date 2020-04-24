import cv2
import numpy as np

def bgr_to_gray(img):
    cols, rows, channels = img.shape
    gray = np.zeros((cols, rows))
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    gray[:, :] = 0.229*r + 0.587*g + 0.114*b
    return gray

if __name__ == "__main__":
    name = "flower"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", img)
    cols, rows, channels = img.shape

    average = np.mean(img, axis=2)
    gray = bgr_to_gray(img)

    cv2.imwrite('Grey image with average weight.jpg', average)
    cv2.imwrite('Grey image with Rec601 weight.jpg', gray)
    bgr2grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    average = cv2.imread('Grey image with average weight.jpg', cv2.IMREAD_UNCHANGED)
    gray = cv2.imread('Grey image with Rec601 weight.jpg', cv2.IMREAD_UNCHANGED)

    cv2.imshow("Gray image", gray)
    cv2.imshow("Grey image", average)
    cv2.imshow("BGR to Grey image", bgr2grey)

    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_original.jpg".format(name), img)
        cv2.imwrite("Result/{}_Mean_Grey.jpg".format(name), average)
        cv2.imwrite("Result/{}_RGB_to_Grey.jpg".format(name), bgr2grey)
        cv2.imwrite("Result/My_{}_RGB_to_Grey.jpg".format(name), bgr2grey)
        cv2.destroyAllWindows()



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
