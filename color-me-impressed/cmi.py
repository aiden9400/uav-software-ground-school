import cv2 as cv, sys, numpy as np

name = input("image filepath pls: ")

img = cv.imread(name)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

masks = []
res = []

def avg_pos(mask):
    y, x = np.where(mask == 255)
    if len(x) == 0:
        return None
    return int(np.mean(x)), int(np.mean(y))

for i in range(0, 180, 30):
    mask = cv.inRange(hsv, np.array([i, 20, 20]), np.array([i + 30, 255, 255]))
    masks.append(mask)
    res.append(cv.resize(cv.bitwise_and(img, img, mask=mask), None, fx = 1.0, fy = 1.0))

for i in range(len(masks)):
    pos = avg_pos(masks[i])
    if pos is not None:
        print(f"Average position of hue {i*30} to {i*30 + 30}: {pos}")

out = np.concatenate(res, axis=0)
cv.imshow("Display window", out)
cv.waitKey(0)
cv.imwrite("res.png", out)
"""
cv.namedWindow("Display window")
for i in range(len(res)):
    cv.imshow("Display window", res[i])

cv.waitKey(0)
"""
"""
mask = cv.inRange(hsv, np.array([0, 20, 20]), np.array([30, 255, 255]))

res = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Display window", res)
cv.waitKey(0)"""