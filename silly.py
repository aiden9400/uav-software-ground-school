import cv2 as cv, sys

filename = "in.png"

img = cv.imread(filename)

#image[:,:,1] = 0
#image[:,:,2] = 0
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("out.png", img)

"""
b = image[:,:,0].copy()
g = image[:,:,1].copy()
r = image[:,:,2].copy()

image[:,:,0] = g
image[:,:,1] = r
image[:,:,2] = b

#image = cv2.resize(image, (4000, 1000))

cv2.imwrite("out.png", image)"""