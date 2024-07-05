import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

# hsv = np.load("hsv.npy")
# lower = hsv[0]
# upper = hsv[1]
# hsv = [lower, upper]

cv2.namedWindow('Color Detector',cv2.WINDOW_NORMAL)

cv2.createTrackbar('Low H', 'Color Detector', 0, 179, nothing)
cv2.createTrackbar('Low S', 'Color Detector', 0, 225, nothing)
cv2.createTrackbar('Low V', 'Color Detector', 0, 225, nothing)

cv2.createTrackbar('High H', 'Color Detector', 179, 179, nothing)
cv2.createTrackbar('High S', 'Color Detector', 225, 225, nothing)
cv2.createTrackbar('High V', 'Color Detector', 225, 225, nothing)

while True :
    _, frame = cap.read()

    low_h = cv2.getTrackbarPos('Low H', 'Color Detector')
    low_s = cv2.getTrackbarPos('Low S', 'Color Detector')
    low_v = cv2.getTrackbarPos('Low V', 'Color Detector')
    
    high_h = cv2.getTrackbarPos('High H', 'Color Detector')
    high_s = cv2.getTrackbarPos('High S', 'Color Detector')
    high_v = cv2.getTrackbarPos('High V', 'Color Detector')

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV에서의 lower/upper 임계값
    lower_color = np.array([low_h, low_s, low_v])
    # upper_color
    upper_color = np.array([high_h, high_s, high_v])
    # lower/upper 임계값을 이용하여 마스크 생성
    
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

# 노이즈 제거를 위한 모폴로지 연산 적용
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea (max_contour) > 100: # >1000: 더 큰 범위를 잡을때 숫자를 높인다.
            cv2.drawContours(frame, [max_contour], -1, (0,225,0),2)
             # 윤곽선의 무게 중심 계산
            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # 추적된 위치에 원 그리기
                cv2.circle(frame, (cx, cy), 20, (0, 255, 0), -1)


    # 원본 이미지에 마스크 적용

    result = cv2.bitwise_and(frame, frame, mask=mask)
    hsv = [lower_color, upper_color]

    cv2.imshow('Original Image', frame)
    cv2.imshow('Color Detector', result)

    if cv2.waitKey(10) & 0xff ==27:
        break

    if cv2.waitKey(10) & 0xff == ord('s'):
        np.save("hsv_value.npy", hsv)
        print("Save succesful")

    if cv2.waitKey(10) & 0xff ==27:
        break

cap.release()                              

cv2.destroyAllWindows()  






