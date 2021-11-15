import cv2 as cv
import numpy as np


class Card(object):

    # 读取图片
    def read_file(self, filename):
        return cv.imread(filename)

    # 图像阈值二值化处理
    def threshold_method(self, img, low_value):
        ret, thresh = cv.threshold(img, low_value, 255, cv.THRESH_BINARY)
        return ret, thresh

    # outs 阈值二值化
    def outs_method(self, img):
        ret, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
        return ret, thresh

    # 图像灰度图处理
    def gray_img(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return gray

    # 闭操作
    def close_method(self, img, kernel, iteration):
        close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iteration)
        return close

    # 膨胀操作
    def dilate_method(self, img, kernel, iteration):
        dilate = cv.dilate(img, kernel, iterations=iteration)
        return dilate

    # 腐蚀操作
    def erode_method(self, img, kernel, iteration):
        erode = cv.erode(img, kernel, iterations=iteration)
        return erode

    # 二值图像颜色转换
    def change_color(self, img):
        change_img = 255 - img
        return change_img

    # 高斯滤波
    def guss_method(self, img, kernel, iteration):
        guss = cv.GaussianBlur(img, kernel, iteration)
        return guss

    # 黑帽操作
    def blackhat_method(self, img, kernel, iteration):
        blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT,kernel,iterations=iteration)
        return blackhat

    # Canny轮廓检测
    def check_canny(self, img, threshold1, threshold2, aperturesize):
        canny = cv.Canny(img, threshold1, threshold2, aperturesize, L2gradient=False)
        return canny

    # 寻找轮廓
    def find_contours(self, img):
        binary, contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        return binary, contours, hierarchy

    # 寻找最小外接矩形
    def find_minarearect(self, contour):
        rect = cv.minAreaRect(contour)
        box = cv.boxPoints(rect)
        return box

    # 图片展示
    def show_img(self, img):
        cv.imshow("img", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    # 图片透视
    def transform_img(self, img, contours, a, b, c):
        res1_img = img.copy()
        res1 = cv.drawContours(res1_img, contours[0], -1, (0, 0, 255), 2)

        # 获得最小的矩形
        rect = cv.minAreaRect(contours[0])
        # 获取矩形的四个顶点坐标
        box = cv.boxPoints(rect)
        box = np.int0(box)
        # 对应的点
        points1 = np.float32([box[a], box[b], box[c]])
        points2 = np.float32([[0, 0], [583, 0], [583, 368]])
        # 变换矩阵M
        M = cv.getAffineTransform(points1, points2)
        # 变换后的图像
        img1 = cv.warpAffine(img, M, (583, 362))
        return img1


    def transform_img_9(self, img, contours,a,b,c):
        res1_img = img.copy()
        res1 = cv.drawContours(res1_img, contours, -1, (0, 0, 255), 2)

        # 获取选出图形的数组
        cnts = sorted(contours, key=cv.contourArea, reverse=True)
        rect = cnts[1]
        res1 = cv.drawContours(img.copy(), rect, -1, (0, 0, 255), 2)
        # 获得最小的矩形
        rect = cv.minAreaRect(rect)
        # 获取矩形的四个顶点坐标
        box = cv.boxPoints(rect)
        box = np.int0(box)
        rato_rect = cv.drawContours(img.copy(), [box], -1, (0, 0, 255), 2)

        # 对应的点
        points1 = np.float32([box[a], box[b], box[c]])
        points2 = np.float32([[0, 0], [583, 0], [583, 368]])
        # 变换矩阵M
        M = cv.getAffineTransform(points1, points2)
        # 变换后的图像
        img1 = cv.warpAffine(img, M, (583, 362))
        return img1


card = Card()