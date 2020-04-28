import cv2

if __name__ == "__main__":
    name = "flower"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    # cv2.imshow("Original image", img)

    # Box Filter using two different methods
    uni_blur_less = cv2.blur(img, (5, 5))
    uni_blur_more = cv2.boxFilter(img, -1, (9, 9))

    # Gaussian Filter with different sigma
    gauss_blur_uniform = cv2.GaussianBlur(img, (9, 9), sigmaX=5, sigmaY=0)  # Uniform distorsion in x and y direciton
    gauss_blur_x = cv2.GaussianBlur(img, (9, 9), sigmaX=10, sigmaY=1)  # Main distorsion in x direciton
    gauss_blur_y = cv2.GaussianBlur(img, (9, 9), sigmaX=1, sigmaY=10)  # Main distorsion in y direciton

    cv2.imshow("Blur image with small kernel", uni_blur_less)
    cv2.imshow("Blur image with large kernel", uni_blur_more)
    cv2.imshow("Blur image with gaussian kernel (sigmaX = sigmaY)", gauss_blur_uniform)
    cv2.imshow("Blur image with gaussian kernel (sigmaX > sigmaY)", gauss_blur_x)
    cv2.imshow("Blur image with gaussian kernel (sigmaX < sigmaY)", gauss_blur_y)

    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        # cv2.imwrite("Result/{}_original.jpg".format(name),img)
        cv2.imwrite("Result/{}_less_blur.jpg".format(name),uni_blur_less)
        cv2.imwrite("Result/{}_more_blur.jpg".format(name),uni_blur_more)
        cv2.imwrite("Result/{}_gauss_blur_uniform.jpg".format(name),gauss_blur_uniform)
        cv2.imwrite("Result/{}_gauss_blur_x.jpg".format(name),gauss_blur_x)
        cv2.imwrite("Result/{}_gauss_blur_y.jpg".format(name),gauss_blur_y)
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
