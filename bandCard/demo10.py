import cv2 as cv
import numpy as np


img = cv.imread("./picture/card10.png")
# print(img.shape)
gauss = cv.GaussianBlur(img, (3, 3), 1)
gray = cv.cvtColor(gauss, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY)
kernel = np.ones((10, 10), np.uint8)
erosion1 = cv.erode(thresh,kernel,iterations=1)
thresh_1 = 255 - erosion1
kernel = np.ones((13,2),np.uint8)
# iterations 次数
dilate = cv.dilate(thresh_1, kernel, iterations=1)

# cv.imshow("",dilate)
# cv.waitKey(0)

binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(contours)  # 轮廓点
cnts = sorted(contours, key=cv.contourArea, reverse=True)
res_img = img.copy()
res = cv.drawContours(res_img, contours[11], -1, (0, 0, 255), 2)

# cv.imshow("",res)
# cv.waitKey(0)

list = [11,10,9,8,7]
number_list = []
for l in list:
    x, y, w, h = cv.boundingRect(contours[l])
    img2 = cv.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x, y, w, h)
    # cv.imshow("img1", img2)     # 数字轮廓

    img_c = thresh.copy()
    img_number = img_c[y: y+h, x:x+w]
    cv.imshow("img_number", img_number)  # 银行卡数字截取
    cv.waitKey(0)

    if l == 7 :
        w_4 = int(w/3)
        for i in range(3):
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
            img_template = cv.imread("./picture/template_2.png", 0)
            template_size = cv.resize(img_template, None, fx=0.20, fy=0.20)
            template_size = 255 - template_size
            res_list = []  # 相似度列表
            for j in range(10):
                left_m = 20 * j
                right_m = 20 * (j + 1)
                img_template_c = template_size.copy()
                template_number = img_template_c[0:, left_m:right_m]
                # cv.imshow("img_number_1", img_number_1)
                # cv.imshow("template_number", template_number)
                # cv.waitKey(0)
                # 模板匹配
                res = cv.matchTemplate(img_number_1, template_number, cv.TM_CCOEFF)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                # print(min_val, max_val, min_loc, max_loc)
                res_list.append(max_val)
            # print(res_list.index(max(res_list)))
            number_list.append(res_list.index(max(res_list)))
    else:
        w_4 = int(w / 4 )

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
        img_template = cv.imread("./picture/template_2.png", 0)
        template_size = cv.resize(img_template, None, fx=0.20, fy=0.20)
        template_size = 255 - template_size
        res_list = []  # 相似度列表
        for j in range(10):
            left_m = 20 * j
            right_m = 20 * (j + 1)
            img_template_c = template_size.copy()
            template_number = img_template_c[0:, left_m:right_m]
            # cv.imshow("img_number_1", img_number_1)
            # cv.imshow("template_number", template_number)
            # cv.waitKey(0)
            # 模板匹配
            res = cv.matchTemplate(img_number_1, template_number, cv.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # print(min_val, max_val, min_loc, max_loc)
            res_list.append(max_val)
        # print(res_list.index(max(res_list)))
        number_list.append(res_list.index(max(res_list)))
print(number_list)
cv.waitKey(0)
cv.destroyAllWindows()