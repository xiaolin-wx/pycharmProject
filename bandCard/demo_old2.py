import cv2 as cv
import numpy as np


img = cv.imread("./picture/credit_card_02.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

kernel = np.ones((2, 2), np.uint8)
erosion = cv.erode(thresh, kernel, iterations=1)

kernel = np.ones((30, 40), np.uint8)
close = cv.morphologyEx(erosion, cv.MORPH_CLOSE, kernel, 1)

kernel = np.ones((10, 18), np.uint8)
dilate = cv.dilate(close, kernel, iterations=1)

binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(contours)  # 轮廓点
res_img = img.copy()
res = cv.drawContours(res_img, contours, -1, (0, 0, 255), 2)

res1_img = img.copy()
res1 = cv.drawContours(res1_img, contours[5], -1, (0, 0, 255), 2)
number_list = [5, 4, 3, 2]      # 数字列表

number = []     # 银行卡数字
for l in number_list:
    x, y, w, h = cv.boundingRect(contours[l])

    # img1 = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # print(x, y, w, h)
    # cv.imshow("img1", img1)     # 数字轮廓

    img_c = gray.copy()
    img_number = img_c[y-10: y+h+10, x-10:x+w+10]
    # img_number = img_number[0:, 0:136]
    # cv.imshow("img_number", img_number)  # 银行卡数字截取
    # cv.waitKey(0)
    # print(img_number.shape)
    flag = 0
    while flag < 4:
        if flag == 0:
            img_number = img_number.copy()
            one_number = img_number[:, 5:40]
        elif flag == 1:
            img_number = img_number.copy()
            one_number = img_number[:, 35:79]
        elif flag == 2:
            img_number = img_number.copy()
            one_number = img_number[:, 75:109]
        elif flag == 3:
            img_number = img_number.copy()
            one_number = img_number[:, 105:175]
        flag = flag + 1

    # cv.imshow("one", one_number)
    # cv.waitKey(0)

        img_template = cv.imread("./picture/ocr_a_reference.png", 0)
        template_size = cv.resize(img_template, None, fx=0.40, fy=0.40)
        template_size = 255 - template_size
        res_list = []  # 相似度列表
        for j in range(10):
            left_m = 32 * j
            right_m = 32 * (j + 1)
            img_template_c = template_size.copy()
            template_number = img_template_c[0:, left_m:right_m]
            # cv.imshow("img_number_1", one_number)
            # cv.imshow("template_number", template_number)
            # cv.waitKey(0)
            # 模板匹配
            res = cv.matchTemplate(one_number, template_number, cv.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # print(min_val, max_val, min_loc, max_loc)
            res_list.append(max_val)
        number.append(res_list.index(max(res_list)))
        print(res_list.index(max(res_list)))
print(number)

cv.imshow("img",img)

cv.waitKey(0)
cv.destroyAllWindows()
