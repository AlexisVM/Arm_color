import cv2
import numpy as np

im = cv2.imread('img.jpeg')
pixels = np.matrix(im.getdata()).reshape(im.size)

width, height = im.size

add = input("string: ")

def grey (add, pixels):
    if add[0] == 0:
        grey(add[1: ],pixels[len(pixels)//2:, :len(pixels)//2]) == 0
        print("the string is in quadrant 0")

    elif add[0] == 1:
        grey(add[1: ],pixels[:len(pixels)//2, :len(pixels)//2]) == 1
        print("the string is in quadrant 1")

    elif add[0] == 2:
        grey(add[1: ],pixels[len(pixels)//2:, len(pixels)//2:]) == 2
        print("the string is in quadrant 2")

    elif add[0] == 3:
        grey(add[1: ],pixels[:len(pixels)//2, len(pixels)//2:]) == 3
        print("the string is in quadrant 3")

    else:
        grey(add,pixels) == 4
    print("error")
    return add,pixels