from resize import scale
from hsv import rgb_to_hsv
import cv2

img = cv2.imread('./temp.jpg', cv2.IMREAD_UNCHANGED)

hsv = rgb_to_hsv(img)
cv2.imwrite("./temp_hsv.jpg",hsv)
hsv = cv2.imread('./temp_hsv.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
