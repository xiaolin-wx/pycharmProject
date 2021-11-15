import cv2 as cv
import numpy as np


img = cv.imread("./picture/credit_card_01.png")
# 二值化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

# 闭操作 数字涂白
kernel = np.ones((5, 35), np.uint8)
close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, 1)

# 膨胀操作  将中间的白块去掉
kernel = np.ones((15, 27), np.uint8)
dilate = cv.dilate(close, kernel, iterations=1)

# 获取轮廓
binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cnts = sorted(contours, key=cv.contourArea, reverse=True)
# 所有轮廓
# res_img = img.copy()
# res = cv.drawContours(res_img, contours, -1, (0, 0, 255), 2)

# 数字区域 3 4 5 6
res1_img = img.copy()
res1 = cv.drawContours(res1_img, contours[2], -1, (0, 0, 255), 2)

# cv.imshow("", res1)
list = [5, 4, 3, 2]
number_list = []
i = 0
flag = 0
for l in list:
    x, y, w, h = cv.boundingRect(contours[l])
    img2 = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x, y, w, h)
    cv.imshow("img1", img2)     # 数字轮廓

    img_c = thresh.copy()
    img_number = img_c[y: y+h, x+8:x+w-8]
    # cv.imshow("img_number", img_number)  # 银行卡数字截取
    # cv.waitKey(0)

    w_4 = int((w- 16) / 4 )

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
x, y, w, h = cv.boundingRect(contours[list[0]])
for i in number_list:
    cv.putText(img, "".join(str(i)), (x+9, y-5), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    x = x + 24
    flag = flag +1
    if flag ==4 or flag==8 or flag==12 :
        x = x+32
cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()

