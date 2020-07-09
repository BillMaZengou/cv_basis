import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == "__main__":
    name = "flower"
    img = cv2.imread('../image/{}.jpg'.format(name), cv2.IMREAD_UNCHANGED)

    scale_percent = 5      # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    resized_area = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite("../Result/{}_Resized_image.jpg".format(name),resized)
    cv2.imwrite("../Result/{}_INTER_AREA_image.jpg".format(name),resized_area)

    fx = 1.5
    fy = 1.5

    resized1 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_NEAREST)
    resized2 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)
    resized3 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_CUBIC)
    resized4 = cv2.resize(resized, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LANCZOS4)
    cv2.imwrite("../Result/{}_INTER_NEAREST_image.jpg".format(name),resized1)
    cv2.imwrite("../Result/{}_INTER_LINEAR_image.jpg".format(name),resized2)
    cv2.imwrite("../Result/{}INTER_CUBIC_image.jpg".format(name),resized3)
    cv2.imwrite("../Result/{}INTER_LANCZOS4_image.jpg".format(name),resized4)

    resized1 = cv2.resize(resized_area, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_NEAREST)
    resized2 = cv2.resize(resized_area, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LINEAR)
    resized3 = cv2.resize(resized_area, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_CUBIC)
    resized4 = cv2.resize(resized_area, dsize=None, fx=fx, fy=fy, interpolation = cv2.INTER_LANCZOS4)
    cv2.imwrite("../Result/{}_INTER_NEAREST_image_area.jpg".format(name),resized1)
    cv2.imwrite("../Result/{}_INTER_LINEAR_image_area.jpg".format(name),resized2)
    cv2.imwrite("../Result/{}INTER_CUBIC_image_area.jpg".format(name),resized3)
    cv2.imwrite("../Result/{}INTER_LANCZOS4_image_area.jpg".format(name),resized4)

    # Should reconstruct original image
    original_dim = (img.shape[0], img.shape[1])
    resized1 = cv2.resize(resized, original_dim, interpolation = cv2.INTER_NEAREST)
    resized2 = cv2.resize(resized, original_dim, interpolation = cv2.INTER_LINEAR)
    resized3 = cv2.resize(resized, original_dim, interpolation = cv2.INTER_CUBIC)
    resized4 = cv2.resize(resized, original_dim, interpolation = cv2.INTER_LANCZOS4)

    num_of_grid = img.shape[0] * img.shape[1]
    Diff_nearest = np.sum((resized1.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_linear = np.sum((resized2.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_cubic = np.sum((resized3.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_lanczos4 = np.sum((resized4.transpose(1, 0, 2)-img)**2)/num_of_grid

    # print(Diff_nearest, Diff_linear, Diff_cubic, Diff_lanczos4)

    resized1 = cv2.resize(resized_area, original_dim, interpolation = cv2.INTER_NEAREST)
    resized2 = cv2.resize(resized_area, original_dim, interpolation = cv2.INTER_LINEAR)
    resized3 = cv2.resize(resized_area, original_dim, interpolation = cv2.INTER_CUBIC)
    resized4 = cv2.resize(resized_area, original_dim, interpolation = cv2.INTER_LANCZOS4)

    num_of_grid = img.shape[0] * img.shape[1]
    Diff_nearest_area = np.sum((resized1.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_linear_area = np.sum((resized2.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_cubic_area = np.sum((resized3.transpose(1, 0, 2)-img)**2)/num_of_grid
    Diff_lanczos4_area = np.sum((resized4.transpose(1, 0, 2)-img)**2)/num_of_grid

    # print(Diff_nearest_area, Diff_linear_area, Diff_cubic_area, Diff_lanczos4_area)

    n_groups = 4
    error_linear = (Diff_nearest, Diff_linear, Diff_cubic, Diff_lanczos4)
    error_area = (Diff_nearest_area, Diff_linear_area, Diff_cubic_area, Diff_lanczos4_area)

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.5
    rects1 = plt.bar(index, error_linear, bar_width, alpha=opacity, color='b', label='Linear')
    rects2 = plt.bar(index + bar_width, error_area, bar_width, alpha=opacity, color='r', label='Area')

    plt.xlabel('Interpolation')
    plt.ylabel('Error')
    plt.ylim(303, 305)
    plt.title('Error From Interpolation')
    plt.xticks(index + bar_width, ('Nearest', 'Bilinear', 'Cubic', 'Lanczos4'))
    plt.yticks(np.arange(303, 305.5, 0.5))
    plt.legend()

    plt.savefig('../Result/interpolation_errors.jpg')
    plt.show()




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
