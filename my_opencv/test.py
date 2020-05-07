from resize import scale
import cv2

img = cv2.imread('./temp.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./temp_g.jpg",img)

resized = scale(img, 1.5, 1.5)
cv2.imwrite("./temp_c.jpg",resized)
resized = cv2.imread('./temp_c.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow("resize", resized)
print("The original size is {}, and the size after scaling is {}".format(img.shape, resized.shape))

cv2.waitKey(0)
cv2.destroyAllWindows()
