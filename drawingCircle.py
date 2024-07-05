import cv2
import numpy as np

         
img1 = np.zeros((300, 300), dtype = 'uint8')
img2 = np.zeros((300, 300), dtype = 'uint8')
cv2.rectangle(img1, (25,25), (275, 275), 255, -1)
cv2.circle(img2, (150,150),150, 255, -1)

b_and = cv2.bitwise_and(img1, img2)
b_or = cv2.bitwise_or(img1, img2)
b_xor = cv2.bitwise_xor(img1, img2)
b_not_a = cv2.bitwise_not(img1)

cv2.imshow("Rectangle", img1)
cv2.imshow("Circle", img2)
cv2.imshow("B_and", b_and)
cv2.imshow("B_or", b_or)
cv2.imshow("B_xor", b_xor)
cv2.imshow("B_notA", b_not_a)

cv2.waitKey()
cv2.destroyAIwindows()




