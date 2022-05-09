import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

image = cv2.imread("test.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_invert = cv2.bitwise_not(image_gray)
image_smooth = cv2.GaussianBlur(image_invert, (21, 21), sigmaX = 0, sigmaY = 0)
"""

def edge(image):
    image_edge = cv2.Canny(image, 200, 300)
    blur = cv2.GaussianBlur(image_edge, (3,3), 0)
    dil = cv2.dilate(image_edge, (np.ones((2,2),np.uint8)), iterations = 1)
    image_gray = 255 - dil
    image_rgba = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2RGBA)
    white = np.all(image_rgba == [255,255,255,255], axis = -1)
    image_rgba[white, -1] = 0
    return image_gray
image_gray = edge(image)
ret, mask = cv2.threshold(image_gray, 1, 255, cv2.THRESH_BINARY)
sketch = cv2.bitwise_and(image_gray, 255-image_smooth, mask = mask)

"""
sketch = cv2.divide(image_gray, 255-image_smooth, scale = 255)
plt.figure(figsize = (8,8))
plt.imshow(sketch, cmap="gray")
plt.axis("off")
plt.title("Sketch")
plt.show()