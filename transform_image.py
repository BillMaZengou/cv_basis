import numpy as np
import cv2

if __name__ == "__main__":
    name = "flower"
    img = cv2.imread('Result/{}_Resized_image.jpg'.format(name), cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original image", img)
    rows, cols, _ = img.shape
    # print(img.shape)

    T = np.array(([1, 0, 100], [0, 1, 50]), dtype=np.float32)
    R = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    convert = np.array(([1, 0, 0], [0, -1, 0], [cols/2, rows/2, 1]), dtype=np.float32)
    inverse = np.array(([1, 0, 0], [0, -1, 0], [-cols/2, rows/2, 1]), dtype=np.float32)
    S = np.array(([1, 0, 0], [0.5, 1, 0], [0, 0, 1]), dtype=np.float32)  # unit vector (0, 1) to (1, 1), shear to x direction
    S = inverse@S@convert
    # To match OpenCV convention
    S = np.transpose(S[:, :-1])

    translated = cv2.warpAffine(img, T, (cols, rows))
    rotated = cv2.warpAffine(img, R, (cols, rows))
    sheared = cv2.warpAffine(img, S, (cols, rows))

    cv2.imshow("Translated image", translated)
    cv2.imshow("Rotated image", rotated)
    cv2.imshow("Sheared image", sheared)

    # Press 's' for saving the image
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("Result/{}_Translated.jpg".format(name),translated)
        cv2.imwrite("Result/{}_Rotated.jpg".format(name),rotated)
        cv2.imwrite("Result/{}_Sheared.jpg".format(name),sheared)
        cv2.destroyAllWindows()
