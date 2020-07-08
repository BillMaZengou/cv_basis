import cv2
from matplotlib import pyplot as plt
import numpy as np

# detector parameters
block_size = 3
sobel_size = 3
k = 0.06

name = 'Solvay_Conferences.jpeg'
image = cv2.imread('./faces/{}'.format(name), cv2.IMREAD_UNCHANGED)

print(image.shape)
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
print("width: %s  height: %s  channels: %s"%(width, height, channels))

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# modify the data type setting to 32-bit floating point
gray_img = np.float32(gray_img)

# detect the corners with appropriate values as input parameters
corners_img = cv2.cornerHarris(gray_img, block_size, sobel_size, k)
# plt.imshow(corners_img)

# result is dilated for marking the corners, not necessary
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dst = cv2.dilate(corners_img, kernel, iterations=1)

# Threshold for an optimal value, marking the corners in Green
image[corners_img>0.01*dst.max()] = [0,255,0]

# for r in range(height):
#         for c in range(width):
#             pix=dst[r,c]
#             if pix>0.01*dst.max():
#                cv2.circle(image,(c,r),1,(0,0,255),0)
#
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(image)
# plt.show()

# Press 's' for saving the image
cv2.imshow("Points", image)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite("Result/{}_interest_points.jpg".format(name), image)
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
