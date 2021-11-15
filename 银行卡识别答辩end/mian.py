import cv2 as cv
import numpy as np
import Template
import Card


def card_1():
    img_1 = cv.imread("images/credit_card_01.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 240)
    kernel = np.ones((5, 35), np.uint8)
    close = Card.card.close_method(thresh, kernel, 1)
    kernel = np.ones((15, 27), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    arraylist = [5, 4, 3, 2]
    img_number = Template.tmp.matching_card(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_2():
    img_1 = cv.imread("images/credit_card_02.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 230)
    kernel = np.ones((2, 2), np.uint8)
    erosion = cv.erode(thresh, kernel, iterations=1)
    kernel = np.ones((30, 40), np.uint8)
    close = Card.card.close_method(erosion, kernel, 1)
    kernel = np.ones((10, 18), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    arraylist = [5, 4, 3, 2]
    img_number = Template.tmp.matching_card2(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_3():
    img_1 = cv.imread("images/credit_card_03.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 127)
    kernel = np.ones((10, 18), np.uint8)
    dilate = Card.card.dilate_method(thresh, kernel, 1)
    kernels = np.ones((1, 3), np.uint8)
    er = cv.erode(dilate, kernels, iterations=1)
    ers = 255 - er
    binary, contours, hierarchy = Card.card.find_contours(ers)

    img1 = Card.card.transform_img(img_1, contours,1,2,3)

    gray = Card.card.gray_img(img1)
    ret, thresh = Card.card.threshold_method(gray, 85)

    kernel = np.ones((5, 35), np.uint8)
    close = Card.card.close_method(thresh, kernel, 1)
    kernel = np.ones((10, 22), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    arraylist = [7,6,5,4]
    img_number = Template.tmp.matching_card(arraylist, contours, img1, gray, thresh)
    Card.card.show_img(img_number)


def card_4():
    img_1 = cv.imread("images/credit_card_04.png")
    gray = Card.card.gray_img(img_1)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (13, 13))
    tophat = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    ret, thresh = Card.card.outs_method(tophat)
    kernel = np.ones((12, 35), np.uint8)
    close = Card.card.close_method(thresh, kernel, 1)
    kernel = np.ones((13, 32), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    res1_img = img_1.copy()
    res1 = cv.drawContours(res1_img, contours, -1, (0, 0, 255), 2)

    # 数组轮廓集合    (争取函数实现)
    arraylist = [6, 5, 4, 3]
    img_number = Template.tmp.matching_card(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_5():
    img_1 = cv.imread("images/credit_card_05.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 155)
    kernel = np.ones((9, 15), np.uint8)
    close = Card.card.close_method(thresh, kernel, 2)
    median = cv.medianBlur(close, 7)
    kernel = np.ones((8, 22), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    # 数组轮廓集合    (争取函数实现)
    arraylist = [11, 9, 8, 7]
    img_number = Template.tmp.matching_card(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_6():
    img = cv.imread("images/card6.png")
    gauss = Card.card.guss_method(img, (3, 3), 0)
    gray = Card.card.gray_img(gauss)
    kernel = np.ones((2, 2), np.uint8)
    black = Card.card.blackhat_method(gray, kernel, 1)
    black = Card.card.change_color(black)
    canny = Card.card.check_canny(black, 50, 160, 10)
    kernel = np.ones((10, 40), np.uint8)
    close = Card.card.close_method(canny, kernel, 1)
    kernel = np.ones((20, 20), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)
    arraylist = [6, 5]
    img = Template.tmp.matching_card6(img,gray,arraylist,contours)
    Card.card.show_img(img)



def card_7():
    img_1 = cv.imread("images/card7.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 210)
    kernel = np.ones((10, 29), np.uint8)
    dilate = Card.card.dilate_method(thresh, kernel, 1)
    kernels = np.ones((1, 1), np.uint8)
    er = cv.erode(dilate, kernels, iterations=1)
    ers = 255 - er
    binary, contours, hierarchy = Card.card.find_contours(ers)
    img1 = Card.card.transform_img(img_1, contours,1,2,3)
    gray = Card.card.gray_img(img1)
    ret, thresh = Card.card.threshold_method(gray, 210)
    kernel = np.ones((5, 20), np.uint8)
    close = Card.card.close_method(thresh, kernel, 1)
    kernel = np.ones((13, 30), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    arraylist = [6,5,4,3]
    img_number = Template.tmp.matching_card(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_8():
    img_1 = cv.imread("images/card8.png")
    gray = Card.card.gray_img(img_1)
    ret, thresh = Card.card.threshold_method(gray, 250)
    kernel = np.ones((12, 28), np.uint8)
    dilate = Card.card.dilate_method(thresh, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)
    # 数组轮廓集合    (争取函数实现)
    arraylist = [7,6,5,4]
    img_number = Template.tmp.matching_card(arraylist, contours, img_1, gray, thresh)
    Card.card.show_img(img_number)


def card_9():
    img_1 = cv.imread("images/card9.png")
    gray = Card.card.gray_img(img_1)
    blurred = Card.card.guss_method(gray,(5,5),0)
    ret, thresh = Card.card.threshold_method(blurred, 220)
    binary, contours, hierarchy = Card.card.find_contours(thresh)
    img1 = Card.card.transform_img_9(img_1, contours, 2, 3, 0)
    gray = Card.card.gray_img(img1)
    ret, thresh = Card.card.threshold_method(gray, 210)
    kernel = np.ones((25, 23), np.uint8)
    dilate = Card.card.dilate_method(thresh, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)
    arraylist = [3,5,4,6]
    img_number = Template.tmp.matching_card9(arraylist, contours, img1, gray, thresh)
    Card.card.show_img(img_number)


def card_10():
    img = cv.imread("images/card10.png")
    gauss = Card.card.guss_method(img, (3, 3), 1)
    gray = Card.card.gray_img(gauss)
    ret, thresh = Card.card.threshold_method(gray, 60)
    kernel = np.ones((10, 10), np.uint8)
    erode = Card.card.erode_method(thresh, kernel, 1)
    erode_change = Card.card.change_color(erode)
    kernel = np.ones((5, 2), np.uint8)
    close = Card.card.close_method(erode_change, kernel, 1)
    kernel = np.ones((10, 2), np.uint8)
    dilate = Card.card.dilate_method(close, kernel, 1)
    binary, contours, hierarchy = Card.card.find_contours(dilate)

    arraylist = [11, 10, 9, 8, 7]
    img = Template.tmp.matching_card10(img, arraylist, contours)
    Card.card.show_img(img)


if __name__ == '__main__':
    card_9()

