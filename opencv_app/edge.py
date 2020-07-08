import cv2

if __name__ == "__main__":
    name = "laptop"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", img)

    # Convert to grey images if input is an RGB image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey image", img)

    img = cv2.GaussianBlur(img, (3, 3), sigmaX=3, sigmaY=0)  # Uniform distorsion in x and y direciton

    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
    edges = cv2.Canny(img,30,60)

    cv2.imshow("X edges", sobelx)
    cv2.imshow("Y edges", sobely)
    cv2.imshow("Canny", edges)

    # # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_gray.jpg".format(name),img)
        cv2.imwrite("Result/{}_x.jpg".format(name),sobelx)
        cv2.imwrite("Result/{}_y.jpg".format(name),sobely)
        cv2.imwrite("Result/{}_edges.jpg".format(name),edges)
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
