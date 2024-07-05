import cv2
import numpy as np

path = 'cat.jpg'


image = cv2.imread(path)
print(image.shape)
print(image.shape[0])

# 정 가운데에다가 동그라미그리기. 

cv2.circle(image, (image.shape[1] // 2, image.shape[0] // 2), 20, (0, 0, 255), 10)
# _, image =cap.read()


# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #frame에 들어온 색을 그레이컬러로 바꾸기. frame = image
# canny_image = cv2.Canny(gray_image, low, high)
# blur_frame = cv2.GaussianBlur(frame, (11,11), 10)
# rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

cv2.imshow("Cat", image)
# cv2.imshow("Cat", gray_image)
# cv2.imshow("Cat", canny_image)

cv2.waitKey() # While True와 다르게 아무키나 누를때 창이 닫힌다.
cv2.destroyAllWindows








