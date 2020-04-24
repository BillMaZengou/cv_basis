import cv2

if __name__ == "__main__":
    name = "kekelo"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", img)

    bgr2grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(bgr2grey.shape)
    grey2bgr = cv2.cvtColor(bgr2grey, cv2.COLOR_GRAY2BGR)
    # print(grey2bgr.shape)
    bgr2hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv2bgr = cv2.cvtColor(bgr2hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("BGR to Grey image", bgr2grey)
    cv2.imshow("Grey to RGB image", grey2bgr)
    cv2.imshow("RGB to HSV image", bgr2hsv)
    cv2.imshow("HSV to RGB image", hsv2bgr)
    #
    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_original.jpg".format(name),img)
        cv2.imwrite("Result/{}_RGB_to_Grey.jpg".format(name),bgr2grey)
        cv2.imwrite("Result/{}_Grey_to_RGB.jpg".format(name),grey2bgr)
        cv2.imwrite("Result/{}_RGB_to_HSV.jpg".format(name),bgr2hsv)
        cv2.imwrite("Result/{}_HSV_to_RGB.jpg".format(name),hsv2bgr)
        cv2.destroyAllWindows()
