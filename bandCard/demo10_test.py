import cv2 as cv
import numpy as np


img = cv.imread("image/images/card10.png")
# print(img.shape)
gauss = cv.GaussianBlur(img, (3, 3), 1)
gray = cv.cvtColor(gauss, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY)
# thresh = 255 - thresh
kernel = np.ones((10, 10), np.uint8)
erosion1 = cv.erode(thresh, kernel, iterations=1)
thresh_1 = 255 - erosion1
kernel = np.ones((5, 2), np.uint8)
close = cv.morphologyEx(thresh_1, cv.MORPH_CLOSE, kernel, 1)
kernel = np.ones((10, 2), np.uint8)
# iterations 次数
dilate = cv.dilate(close, kernel, iterations=1)

# cv.imshow("dilate", dilate)
# cv.waitKey(0)
# cv.destroyAllWindows()

binary, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(contours)  # 轮廓点
cnts = sorted(contours, key=cv.contourArea, reverse=True)
# res_img = img.copy()
# res = cv.drawContours(res_img, contours, -1, (0, 0, 255), 2)

template_number = [11, 10, 9, 8, 7]
# res1_img = img.copy()
# res1 = cv.drawContours(res1_img, contours[11], -1, (0, 0, 255), 2)

x, y, w, h = cv.boundingRect(contours[7])
# one_number = cv.rectangle(dilate, (x, y), (x+w, y+h), (0, 255, 0), 2)
# img_c = img.copy()
# img_number = img_c[y: y+h, x:x+w]

gray_c = img.copy()
one_number = gray_c[y: y+h, x:x+w]
one_number = cv.cvtColor(one_number, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(one_number, 120, 255, cv.THRESH_BINARY)
# cv.imshow("one_number", thresh)
# cv.waitKey(0)
# cv.destroyAllWindows()
'''
    [:, 0:21] [:, 21:41] [:, 41:61] [:, 61:81]
    [:, 0:20] [:, 20:40] [:, 40:60] [:, 60:80]
    [:, 0:20] [:, 19:39] [:, 39:59] [:, 58:78]
    [:, 0:20] [:, 20:40] [:, 40:60] [:, 58:78]
    [:, 0:20] [:, 20:40] [:, 40:60]
'''

first_number = thresh[:, 40:60]
cv.imshow("gray", first_number)
cv.waitKey(0)
cv.destroyAllWindows()
# print(first_number.shape)
img_template = cv.imread("./image/images/template_2.png", 0)
# print(template_size.shape)
# cv.imshow("img", template_size)
img_template = img_template[45:-45, 14:-14]
# cv.imshow("img", template_size)

res_list = []
for j in range(10):
    left_m = 100 * j + 8
    right_m = 100 * (j + 1) + 8
    img_template_c = img_template.copy()
    template_number = img_template_c[:, left_m:right_m]
    template_size = cv.resize(template_number, None, fx=0.2, fy=0.2)
    print(first_number.shape)
    print(template_number.shape)
    # cv.imshow("img_number_1", img_number_1)
    # cv.imshow("template_number", template_number)
    # cv.waitKey(0)
    # 模板匹配
    res = cv.matchTemplate(first_number, template_size, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # print(min_val, max_val, min_loc, max_loc)
    res_list.append(max_val)
print(res_list.index(max(res_list)))
cv.waitKey(0)
cv.destroyAllWindows()