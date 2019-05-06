import cv2
import numpy as np

# Detectar colores
greenLowerBound = np.array([33, 80, 40])
greenUpperBound = np.array([102, 255, 255])
orangeLowerBound = np.array([18, 40, 90])
orangeUpperBound = np.array([27, 255, 255])
yellowLowerBound = np.array([20, 100, 100])
yellowUpperBound = np.array([30, 255, 255])
redLowerBound = np.array([0, 100, 100])
redUpperBound = np.array([10, 255, 255])

# Iniciar la captura de video
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cam.read()
    img = cv2.resize(img, (340, 220))

    #  BGR a HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # crear la máscara
    mask = cv2.inRange(imgHSV, redLowerBound, redUpperBound)
    greenmask = cv2.inRange(imgHSV, greenLowerBound, greenUpperBound)
    yellowmask = cv2.inRange(imgHSV, yellowLowerBound, yellowUpperBound)
    redmask = cv2.inRange(imgHSV, redLowerBound, redUpperBound)

    # morfología
    maskOpen = cv2.morphologyEx(yellowmask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose
    conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, str(i + 1), (x, y + h), font, 4, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("maskClose", maskClose)
    cv2.imshow("maskOpen", maskOpen)
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    cv2.waitKey(10)