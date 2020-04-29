import cv2

if __name__ == "__main__":
    name = "laptop"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", img)

    # Convert to grey images if input is an RGB image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey image", img)

    _, simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Simple thresholding image", simple)

    retval, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("Otsu thresholding image", otsu)
    print(retval)

    mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("Mean Adaptive Thresholding image", mean)
    cv2.imshow("Gaussian Adaptive Thresholding image", gauss)


    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_original.jpg".format(name),img)
        cv2.imwrite("Result/{}_simple_threshold.jpg".format(name),simple)
        cv2.imwrite("Result/{}_otsu.jpg".format(name),otsu)
        cv2.imwrite("Result/{}_mean_adaptive_threshold.jpg".format(name),mean)
        cv2.imwrite("Result/{}_gaussian_adaptive_threshold.jpg".format(name),gauss)
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
