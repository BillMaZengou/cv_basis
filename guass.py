# Incomplete
# import numpy as np

# height = 3
# width = 3
# kernel = np.zeros((height, width))
# centre_h = (height - 1) // 2
# centre_w = (width - 1) // 2
# print(centre_h, centre_w)
# weight = 0
#
# print(kernel)

"""
---
"""

import cv2
a = cv2.getGaussianKernel(3, sigma=-1)
print(a)
