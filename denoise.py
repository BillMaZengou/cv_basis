import numpy as np
import cv2

if __name__ == "__main__":
    name = "flower"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    # print(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise = np.random.normal(loc=0, scale=0.5, size=img.shape)
    # print(noise)
    noisy_img = img+noise
    # high = noisy_img > 255
    # low = noisy_img < 255
    # noisy_img[high] = 255
    # noisy_img[low] = 0
    # print(np.any(noisy_img <0 ))
    cv2.imshow("Original image", noisy_img)
    #
    # # Box Filter using two different methods
    # uni_blur_less = cv2.blur(img, (5, 5))
    #
    # # Gaussian Filter with different sigma
    # gauss_blur_uniform = cv2.GaussianBlur(img, (9, 9), sigmaX=5, sigmaY=0)  # Uniform distorsion in x and y direciton
    #
    # cv2.imshow("Blur image with small kernel", uni_blur_less)
    # cv2.imshow("Blur image with large kernel", uni_blur_more)
    #
    # # Press 's' for saving the imageq
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    # elif k == ord('s'): # wait for 's' key to save and exit
    #     cv2.imwrite("Result/{}_original.jpg".format(name),img)
    #     cv2.imwrite("Result/{}_less_blur.jpg".format(name),uni_blur_less)
    #     cv2.imwrite("Result/{}_more_blur.jpg".format(name),uni_blur_more)
    #     cv2.destroyAllWindows()



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
