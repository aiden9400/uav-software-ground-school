import cv2 as cv, numpy as np

name = input("image filepath pls: ")

img = cv.imread(name)

p = cv.SimpleBlobDetector_Params()

p.minThreshold = 0
p.maxThreshold = 440
p.minArea = 15
p.filterByColor = True

detector = cv.SimpleBlobDetector_create(p)
blobs = detector.detect(img)
out = cv.drawKeypoints(img, blobs, np.array([]), (255, 255, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow("Display Window", out)
cv.waitKey(0)
cv.imwrite("res_blobs.png", out)