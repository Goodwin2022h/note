import cv2

img=cv2.imread('/home/nrc/weixing.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('weixing_gray.png',img_gray)
