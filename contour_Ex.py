import cv2
import numpy as np
# PIL ( Python Image Library)
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((480, 640, 3), dtype=np.uint8)

img[:,:,:] = (255, 0, 0)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = np.zeros((480, 640, 3), dtype=np.uint8)

img[100:200, 200:300] = ( 255, 255, 255)
# 세로영역, 가로 영역 기준으로 원하는 색을 채움
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 직선 그려보기
img = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = ( 0, 255, 255) # BGR : yellow
THICKNESS = 3 # 두께

# 그릴 위치, 시작점, 끝 점, 색깔, 두께, 선 종류
cv2.line(img, (50,100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50,200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 원 그리기
# 그릴 위치, 원의 중심점, 반지름 색깔, 두께, 선 종류
COLOR =(255, 255, 0)
RADIUS = 50
THICKNESS = 10
cv2.circle(img,(200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)
cv2.circle(img,(400, 100), RADIUS, COLOR,  cv2.FILLED, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#사각형 그리기
# 그릴 위치 (왼쪽 위 좌표, 오른쪽 아래 좌표), 색깔, 두께
COLOR = (0, 255, 0) # BGR : 녹색
THICKNESS = 3    # 두께
cv2.rectangle(img, (100,100), (200, 200), COLOR, THICKNESS)  # 속이 빈 사각형
cv2.rectangle(img, (300,100), (400, 300), COLOR, cv2.FILLED)   # 속이 꽉 찬 사각형
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

COLOR = (0, 0, 255) # BGR : 빨간색
THICKNESS = 3    # 두께
pts1 = np.array([[100, 100],[200,100],[100,200]])
pts2 = np.array([[200, 100],[300,100],[300,200]])
#cv2.polylines(img,[pts1], True, COLOR, THICKNESS, cv2.LINE_AA) # 다각형 값을 리스트에 넣어야함
# True 는 다각형이 닫힘, False 다각형이 열림
#cv2.polylines(img,[pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 다각형 값을 리스트에 넣어야함
cv2.polylines(img,[pts1 , pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 다각형
# 그릴위치 , 그릴 좌표, 닫힘 여부, 색깔, 두께, 선 종류
pts3 = np.array([[[100, 300], [200, 300], [100, 400]],[[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표들, 색깔, 선 종류
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 한글을 OpenCV에서 사용하는 방법 글자를 그리는 방식으로 진행
def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('font/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)
# OpenCV에서 한글 지원을 하지 않기 때문에 위 함수를 만들어 사용
img = np.zeros((480, 640, 3), dtype=np.uint8)
img1 = np.zeros((480, 640, 3), dtype=np.uint8)
FONT_SIZE = 30
COLOR1 = (255, 255, 255) # 흰색
COLOR2 = (0, 0, 255) # 흰색
# 그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, 'Coding', (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, COLOR, THICKNESS)
# cv2.putText(img, '코딩', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS) : 이렇게하면 폰트 깨짐

img1 = myPutText(img1, "코딩", (20, 50), FONT_SIZE, COLOR2 )  # 함수르 사용하여 한글 지원cv2.imshow('img', img)
cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 빈 캔버스 생성(높이, 너비, 채널) - 3개의 색상 채널, 너비 400, 높이 300
w = 700
h = 800
canvas_accessdenied = np.zeros((w,h,3),dtype="uint8")

# 좌표 (x=100,y=230)에 색상 (255,255,0), 선 두께가 2인  직사각형 추가
cv2.rectangle(canvas_accessdenied, (w//7, h//5), (700, 300), (255,255,0), 2)

# 좌표 (x=150,y=320)에 색상(100,100,255), 글꼴 크기 2, 선 두께 5인 텍스트 추가
cv2.putText(canvas_accessdenied, "ACCESS DENIED", (150,250), cv2.FONT_HERSHEY_SIMPLEX, 2, (100,100,255), 5)

# 좌표 (x=100,y=230)에 색상 (255,255,0), 선 두께가 2인 직사각형 추가
cv2.rectangle(canvas_accessdenied, (w//7, h//5+300), (700, 580), (255,255,0), 2)

# 좌표 (x=130,y=320)에 색상 (255,100,100), 글꼴 크기 2, 선 두께 5인 텍스트 추가
cv2.putText(canvas_accessdenied, "ACCESS GRANTED", (130,540), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,100,100), 5)

cv2.imshow("Canvas Access Granted",canvas_accessdenied)
cv2.waitKey(0)                             # 아무 키나 누른 후 창 종료
cv2.destroyAllWindows()



