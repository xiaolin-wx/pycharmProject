import cv2 as cv
import numpy as np


img = cv.imread("./picture/card9.png")
# 二值化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 除去杂点
blurred = cv.GaussianBlur(gray, (3, 3), 0)
ret, thresh = cv.threshold(blurred, 220, 255, cv.THRESH_BINARY)

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

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 210, 255, cv.THRESH_BINARY)

# 膨胀操作  将中间的白块去掉
kernel = np.ones((27, 24), np.uint8)
dilate = cv.dilate(thresh, kernel, iterations=1)

cv.imshow("",dilate)
cv.waitKey(0)

binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(contours)  # 轮廓点
cnts = sorted(contours, key=cv.contourArea, reverse=True)
# 所有轮廓
res_img = img.copy()
res = cv.drawContours(res_img, contours, -1, (0, 0, 255), 2)

# 数字区域 3 4 5 6
res1_img = img1.copy()
res1 = cv.drawContours(res1_img, contours[4], -1, (0, 0, 255), 2)

# cv.imshow("",res1)
# cv.waitKey(0)


list = [1,3,2,4]
number_list = []
for l in list:
    x, y, w, h = cv.boundingRect(contours[l])
    img2 = cv.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x, y, w, h)
    # cv.imshow("img1", img2)     # 数字轮廓

    img_c = thresh.copy()
    img_number = img_c[y: y+h, x+8:x+w-6]
    # cv.imshow("img_number", img_number)  # 银行卡数字截取
    # cv.waitKey(0)

    w_4 = int((w- 14) / 4 )

    for i in range(4):
        if i == 0:
            left = 0
            right = w_4
        else:
            left = (w_4) * i
            right = (w_4) * (i + 1)
        img_number_x = img_number.copy()
        # img_number_x = cv.cvtColor(img_number_x, cv.COLOR_BGR2GRAY)
        # 银行卡单个数字提取
        img_number_1 = img_number_x[:, left:right]

        # 读取模板图片
        img_template = cv.imread("./picture/ocr_a_reference.png", 0)
        template_size = cv.resize(img_template, None, fx=0.30, fy=0.30)
        template_size = 255 - template_size
        res_list = []  # 相似度列表
        for j in range(10):
            left_m = 24 * j
            right_m = 24 * (j + 1)
            img_template_c = template_size.copy()
            template_number = img_template_c[0:, left_m:right_m]
            cv.imshow("img_number_1", img_number_1)
            cv.imshow("template_number", template_number)
            cv.waitKey(0)
            # 模板匹配
            res = cv.matchTemplate(img_number_1, template_number, cv.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # print(min_val, max_val, min_loc, max_loc)
            res_list.append(max_val)
        # print(res_list.index(max(res_list)))
        number_list.append(res_list.index(max(res_list)))
print(number_list)
cv.imshow("img", img1)

cv.waitKey(0)
cv.destroyAllWindows()