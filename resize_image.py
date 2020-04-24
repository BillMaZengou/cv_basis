import cv2

if __name__ == "__main__":
    name = "kekelo"
    img = cv2.imread('./{}.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    # cv2.imshow("Original image", img)
    print('Original Dimensions : ',img.shape)

    scale_percent = 40       # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

    fx = 1.5
    fy = 1.5

    resized1 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_NEAREST)

    resized2 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)
    print('Resized Dimensions : ',resized.shape)

    cv2.imshow("Resized image", resized)
    cv2.imshow("INTER_NEAREST image", resized1)
    cv2.imshow("INTER_LINEAR image", resized2)

    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_Resized_image.jpg".format(name),resized)
        cv2.imwrite("Result/{}_INTER_NEAREST_image.jpg".format(name),resized1)
        cv2.imwrite("Result/{}_INTER_LINEAR_image.jpg".format(name),resized2)
        cv2.destroyAllWindows()
