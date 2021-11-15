import cv2 as cv
import numpy as np

'''
    银行卡
'''


def th_ostu():
    img = cv.imread("../image/image/xingtai/card.png")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret,th = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV, cv.THRESH_OTSU)
    res = np.hstack((gray, th))
    cv.imshow('res',res)


def to_top_ostu():
    img = cv.imread("./picture/credit_card_04.png")
    img = cv.resize(img,None,fy=0.7,fx=0.7)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(21,21))
    tophat = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    ret,th = cv.threshold(tophat,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    res = np.hstack((gray,tophat,th))
    cv.imshow('res',res)


if __name__ == '__main__':
    # th_ostu()
    to_top_ostu()
    cv.waitKey(0)
    cv.destroyAllWindows()