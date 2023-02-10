import cv2
import numpy as np

# =========================================================================================
# np.zeros((x,y,z)) that means matriks with x*ysize, and when we store them on the images, that will be a blank image, and z mean how much the matriks will stored
# np.uint8 mean that value on the matriks will stored by integer type, not a float type
img = np.zeros((512,512,3), np.uint8)
print(img)

# =========================================================================================
# that statement will change the basic color of the matriks, that means (b,g,r)
# furthermore, we can use that statement to change the color or crop with spesific height and width
img[:] = 0,0,255 #--> that means we'll change whole px images color to blue
img[120:412, 12:512] = 0,255,0 #--> that means we'll change the color at height(120 - 412) and width(12-512) to green.


# =========================================================================================
# Create Line with cv2 in our images
# cv2.line(img, start, end, color, thickness)
cv2.line(img,(512,0), (0,213), (213,12,31), 3)

# =========================================================================================
# Create rectangle (segi4)
# cv2.rectangle(img, start(x,y), end(x,y), color, thickness/filled(cv2.FILLED))
cv2.rectangle(img, (0,100), (200,32), (231,123,0), cv2.FILLED)

# =========================================================================================
# Create Circle Function
# cv2.circle(img, (centerpoint), radius, color, thickness/cv2.FILLED)
cv2.circle(img, (256,256), 20, (2,123,211), 2)

# =========================================================================================
# Put Text Function
# cv2.putText(img , 'text', xypoint, cv2.font, thickness, color)
cv2.putText(img, 'This is the text', (75,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))




cv2.imshow('images', img)
cv2.waitKey()