#%%
import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('template.jpg')
image2 = cv2.imread('test1.jpg')

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
edged2 = cv2.Canny(gray2, 30, 200)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 = cv2.findContours(edged2,
                                         cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#cv2.imshow('Canny Edges After Contouring', edged)
#cv2.imshow('Canny Edges After Contouring 2', edged2)

print("Number of Contours found = " + str(len(contours)))
print("Number of Contours found = " + str(len(contours2)))


# Draw all contours
# -1 signifies drawing all contours
#cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
#cv2.drawContours(image2, contours2, -1, (0, 255, 0), 3)

#cv2.imshow('Contours', image)
#cv2.imshow('Contours 2', image2)

res = cv2.matchShapes(contours[0], contours2[0], 1,0)
print(res)

res = cv2.matchShapes(contours[1], contours2[0], 1, 0)
print(res)

cv2.drawContours(image, contours[0], -1, (0, 255, 0), 3)
cv2.imshow('Contours', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
