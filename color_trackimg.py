import cv2
import numpy as np

#Detectar colores
greenLowerBound = np.array([33, 80, 40])
greenUpperBound = np.array([102, 255, 255])
orangeLowerBound = np.array([18, 40, 90])
orangeUpperBound = np.array([27, 255, 255])
yellowLowerBound = np.array([20, 100, 100])
yellowUpperBound = np.array([30, 255, 255])
redLowerBound = np.array([0, 100, 100])
redUpperBound = np.array([10, 255, 255])

#Iniciar la captura de video
#cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    img = cv2.imread('img2.jpeg')
    img = cv2.resize(img, (510, 330))

    #  BGR a HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # crear la máscara
    #mask = cv2.inRange(imgHSV, redLowerBound, redUpperBound)
    greenmask = cv2.inRange(imgHSV, greenLowerBound, greenUpperBound)
    yellowmask = cv2.inRange(imgHSV, yellowLowerBound, yellowUpperBound)
    redmask = cv2.inRange(imgHSV, redLowerBound, redUpperBound)

    # morfología
    # amarillo
    yellowmaskOpen = cv2.morphologyEx(yellowmask, cv2.MORPH_OPEN, kernelOpen)
    yellowmaskClose = cv2.morphologyEx(yellowmaskOpen, cv2.MORPH_CLOSE, kernelClose)
    yellowmaskFinal = yellowmaskClose
    yellowconts, hy = cv2.findContours(yellowmaskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, yellowconts, -1, (255, 255, 255), 3)
    # rojo
    redmaskOpen = cv2.morphologyEx(redmask, cv2.MORPH_OPEN, kernelOpen)
    redmaskClose = cv2.morphologyEx(redmaskOpen, cv2.MORPH_CLOSE, kernelClose)
    redmaskFinal = redmaskClose
    redconts, hr = cv2.findContours(redmaskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, redconts, -1, (255, 255, 255), 3)
    # verde
    greenmaskOpen = cv2.morphologyEx(greenmask, cv2.MORPH_OPEN, kernelOpen)
    greenmaskClose = cv2.morphologyEx(greenmaskOpen, cv2.MORPH_CLOSE, kernelClose)
    greenmaskFinal = greenmaskClose
    greenconts, hg = cv2.findContours(greenmaskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, greenconts, -1, (255, 255, 255), 3)

    for i in range(len(yellowconts)):
        x, y, w, h = cv2.boundingRect(yellowconts[i])
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        if ((x+w) <= 255) and ((y+h) <= 190): cv2.putText(img, "[1,1]", (0, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) <= 255) and ((y+h) >= 190): cv2.putText(img, "[1,3]", (0, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) <= 190): cv2.putText(img, "[1,2]", (255, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) >= 190): cv2.putText(img, "[1,4]", (255, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    for i in range(len(redconts)):
        x, y, w, h = cv2.boundingRect(redconts[i])
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        if ((x+w) <= 255) and ((y+h) <= 190): cv2.putText(img, "[2,1]", (0, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) <= 255) and ((y+h) >= 190): cv2.putText(img, "[2,3]", (0, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) <= 190): cv2.putText(img, "[2,2]", (255, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) >= 190): cv2.putText(img, "[2,4]", (255, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    for i in range(len(greenconts)):
        x, y, w, h = cv2.boundingRect(greenconts[i])
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        if ((x+w) <= 255) and ((y+h) <= 190): cv2.putText(img, "[3,1]", (0, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) <= 255) and ((y+h) >= 190): cv2.putText(img, "[3,3]", (0, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) <= 190): cv2.putText(img, "[3,2]", (255, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        elif ((x+w) >= 255) and ((y+h) >= 190): cv2.putText(img, "[3,4]", (255, 320), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("yellow", yellowmaskFinal)
    cv2.imshow("green", greenmaskFinal)
    cv2.imshow("red", redmaskFinal)
    cv2.line(img, (255,330), (255, 0), (0,0,255),2)
    cv2.line(img, (0, 165), (510, 165), (0, 0, 255), 2)
    cv2.putText(img, "1", (0, 20), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "2", (255, 20), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "3", (0, 190), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "4", (255, 190), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("cam", img)
    cv2.waitKey(10)