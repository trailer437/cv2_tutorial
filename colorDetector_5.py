import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

hsv = np.load("hsv_value.npy", allow_pickle = True)
lower = hsv[0]
upper = hsv[1]

# hsv = [lower, upper]

while True :
    _, frame = cap.read()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(frame_hsv, lower, upper)

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

    cv2.imshow('Original Image', frame)
    cv2.imshow('Color Detector', result)

    if cv2.waitKey(10) & 0xff ==27:
        break

    if cv2.waitKey(10) & 0xff == ord('s'):
        np.save("hsv.npy", hsv)

    if cv2.waitKey(10) & 0xff ==27:
        break

cap.release()                              

cv2.destroyAllWindows()  






