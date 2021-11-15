import cv2 as cv
import numpy as np


img = cv.imread("./picture/card6.png")
# img_size = cv.resize(img, None, fx=1.3, fy=1.3)
gauss = cv.GaussianBlur(img, (3, 3), 0)
gray = cv.cvtColor(gauss, cv.COLOR_BGR2GRAY)
kernel = np.ones((2, 2), np.uint8)
open1 = cv.morphologyEx(gray, cv.MORPH_BLACKHAT,kernel,iterations=1)
open1 = 255 - open1
canny = cv.Canny(open1, 50, 150, 3, L2gradient=False)

kernel = np.ones((10, 40), np.uint8)
close = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel, 1)
kernel = np.ones((20, 20), np.uint8)
dilate = cv.dilate(close, kernel, iterations=1)

cv.imshow("",canny)
cv.waitKey(0)

binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# print(contours)  # 轮廓点
cnts = sorted(contours, key=cv.contourArea, reverse=True)
# 所有轮廓
# res_img = img.copy()
# res = cv.drawContours(res_img, contours, -1, (0, 0, 255), 2)
# cv.imshow("res", res)
res1_img = img_size.copy()
# 6 17
res1 = cv.drawContours(res1_img, contours[3], -1, (0, 0, 255), 2)

cv.imshow("11",res1)
cv.waitKey(0)

list = [4,3]
number_list = []
for l in list:
    x, y, w, h = cv.boundingRect(contours[l])
    img2 = cv.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x, y, w, h)
    # cv.imshow("img1", img2)     # 数字轮廓

    img_c = img_size.copy()
    img_number = img_c[y: y+h, x+12:x+w-8]
    cv.imshow("img_number", img_number)  # 银行卡数字截取
    cv.waitKey(0)

    if l == 4:
        w_4 = int((w-20)/6)
        for i in range(6):
            if i == 0:
                left = 0
                right = w_4
            else:
                left = (w_4) * i
                right = (w_4) * (i + 1)
            img_number_x = img_number.copy()
            img_number_x = cv.cvtColor(img_number_x, cv.COLOR_BGR2GRAY)
            # 银行卡单个数字提取
            img_number_1 = img_number_x[:, left:right]

            # 读取模板图片
            img_template = cv.imread("./picture/template_2.png", 0)
            template_size = cv.resize(img_template, None, fx=0.30, fy=0.30)
            template_size = 255 - template_size
            res_list = []  # 相似度列表
            for j in range(10):
                left_m = 30 * j
                right_m = 30 * (j + 1)
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
    # else:
    #     w_4 = int((w-7)/13)
    #
    #     for i in range(13):
    #         if i == 0:
    #             left = 0
    #             right = w_4
    #         else:
    #             left = (w_4) * i
    #             right = (w_4) * (i + 1)
    #         img_number_x = img_number.copy()
    #         img_number_x = cv.cvtColor(img_number_x, cv.COLOR_BGR2GRAY)
    #         # 银行卡单个数字提取
    #         img_number_1 = img_number_x[:, left:right]
    #
    #         # 读取模板图片
    #         img_template = cv.imread("./picture/template_2.png", 0)
    #         template_size = cv.resize(img_template, None, fx=0.15, fy=0.15)
    #         template_size = 255 - template_size
    #         res_list = []  # 相似度列表
    #         for j in range(10):
    #             left_m = 15 * j
    #             right_m = 15 * (j + 1)
    #             img_template_c = template_size.copy()
    #             template_number = img_template_c[0:, left_m:right_m]
    #             # cv.imshow("img_number_1", img_number_1)
    #             # cv.imshow("template_number", template_number)
    #             # cv.waitKey(0)
    #             # 模板匹配
    #             res = cv.matchTemplate(img_number_1, template_number, cv.TM_CCOEFF)
    #             min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    #             # print(min_val, max_val, min_loc, max_loc)
    #             res_list.append(max_val)
    #         # print(res_list.index(max(res_list)))
    #         number_list.append(res_list.index(max(res_list)))
print(number_list)
cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()