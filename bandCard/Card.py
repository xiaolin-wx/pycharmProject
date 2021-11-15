import numpy as np
import cv2 as cv

class Card:

    """
        二值化
    """

    # 银行卡1
    def base_img1(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡2
    def base_img2(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡3
    def base_img3(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡4
    def base_img4(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (13, 13))
        tophat = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
        ret, thresh = cv.threshold(tophat, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        thresh = 255 - thresh
        return thresh,gray

    # 银行卡5
    def base_img5(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡7
    def base_img7(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 210, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡8
    def base_img8(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡9 转正之前的操作
    def base_img9(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (5, 5), 0)
        ret, thresh = cv.threshold(blurred, 220, 255, cv.THRESH_BINARY)
        return thresh,gray

    # 银行卡9 转正后的操作
    def base_img9_1(self, img):
        gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 210, 255, cv.THRESH_BINARY)
        return thresh,gray

    '''闭操作 数字涂白'''

    def close_white1_2(self, thresh):
        kernel = np.ones((5, 35), np.uint8)
        close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, 1)
        return close

    def close_white4(self, thresh):
        kernel = np.ones((12, 35), np.uint8)
        close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, 1)
        return close

    def close_white5(self, thresh):
        kernel = np.ones((9, 15), np.uint8)
        close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, 2)
        return close

    # 银行卡9 转正后的闭操作
    def close_white9_1(self, thresh):
        kernel = np.ones((20, 20), np.uint8)
        close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, 1)
        return close



    '''膨胀操作  将中间的去掉'''
    def dilate_white1_2(self, close):
        kernel = np.ones((15, 27), np.uint8)
        dilate = cv.dilate(close, kernel, iterations=1)
        return  dilate

    def dilate_white3(self, close):
        kernel = np.ones((10, 18), np.uint8)
        dilate = cv.dilate(thresh, kernel, iterations=1)

        kernels = np.ones((1, 3), np.uint8)
        er = cv.erode(dilate, kernels, iterations=1)
        ers = 255 - er
        return  dilate

    def dilate_white4(self, close):
        kernel = np.ones((13, 32), np.uint8)
        dilate = cv.dilate(close, kernel, iterations=1)
        return  dilate

    def dilate_white5(self, close):
        # 中值模糊
        median = cv.medianBlur(close, 7)
        kernel = np.ones((8, 22), np.uint8)
        dilate = cv.dilate(median, kernel, iterations=1)
        return  dilate

    def dilate_white7(self, close):
        kernel = np.ones((10, 29), np.uint8)
        dilate = cv.dilate(thresh, kernel, iterations=1)

        kernels = np.ones((1, 1), np.uint8)
        er = cv.erode(dilate, kernels, iterations=1)
        ers = 255 - er
        return  dilate

    def dilate_white8(self, close):
        kernel = np.ones((12, 28), np.uint8)
        dilate = cv.dilate(thresh, kernel, iterations=1)
        return  dilate

    # 银行卡9 转正后的膨胀
    def dilate_white9_1(self, close):
        kernel = np.ones((23, 22), np.uint8)
        dilate = cv.dilate(close, kernel, iterations=1)
        return  dilate

    # 获取数字轮廓
    def get_contours(self, dilate):
        binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        cnts = sorted(contours, key=cv.contourArea, reverse=True)
        return contours

    # 获取银行卡9的反转图
    def getReal_contours9(self, dilate):
        binary, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        draw_img = img.copy()
        res = cv.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
        # 获取选出图形的数组
        cnts = sorted(contours, key=cv.contourArea, reverse=True)
        rect = cnts[1]
        res1 = cv.drawContours(img.copy(), rect, -1, (0, 0, 255), 2)
        # 获得最小的矩形
        rect = cv.minAreaRect(rect)
        # 获取矩形的四个顶点坐标
        box = cv.boxPoints(rect)
        print(box)
        # 取整数
        box = np.int0(box)
        rato_rect = cv.drawContours(img.copy(), [box], -1, (0, 0, 255), 2)
        # 对应的点
        points1 = np.float32([box[2], box[3], box[0]])
        points2 = np.float32([[0, 0], [583, 0], [583, 368]])
        # 变换矩阵M
        M = cv.getAffineTransform(points1, points2)
        # 变换后的图像
        img1 = cv.warpAffine(img, M, (583, 362))
        return img1



card = Card()

