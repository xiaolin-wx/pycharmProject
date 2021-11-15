import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 数字模板的拆解
class Template:

    template = cv.imread("./picture/alltemplate.png")
    template_2 = cv.imread("./picture/template_2.png")
    max_list = []

    # 模板匹配 针对常规数字
    def matching_card(self, list, contours, img, gray, thresh):

        number_list = []
        for l in list:
            x, y, w, h = cv.boundingRect(contours[l])
            img2 = cv.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(x, y, w, h)
            # cv.imshow("img1", img2)     # 数字轮廓

            img_c = thresh.copy()
            img_number = img_c[y: y + h, x + 8:x + w - 8]
            # cv.imshow("img_number", img_number)  # 银行卡数字截取
            # cv.waitKey(0)

            w_4 = int((w - 16) / 4)

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
                self.max_list.append(res_list.index(max(res_list)))
                if len(self.max_list) == 4:
                    for i in self.max_list:
                        cv.putText(img, "".join(str(i)), (x + 9, y - 5), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0),2)
                        x = x+25
                    self.max_list = []
                # print(res_list.index(max(res_list)))
                number_list.append(res_list.index(max(res_list)))
        print(number_list)
        return img

        # 模板匹配 针对常规数字

    def matching_card9(self, list, contours, img, gray, thresh):
        number_list = []
        for l in list:
            x, y, w, h = cv.boundingRect(contours[l])
            img2 = cv.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(x, y, w, h)
            # cv.imshow("img1", img2)     # 数字轮廓

            img_c = thresh.copy()
            img_number = img_c[y: y + h, x + 8:x + w - 6]
            # cv.imshow("img_number", img_number)  # 银行卡数字截取
            # cv.waitKey(0)

            w_4 = int((w - 14) / 4)

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
                self.max_list.append(res_list.index(max(res_list)))
                if len(self.max_list) == 4:
                    for i in self.max_list:
                        cv.putText(img, "".join(str(i)), (x + 9, y - 5), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0,255),
                                   2)
                        x = x + 25
                    self.max_list = []
                # print(res_list.index(max(res_list)))
                number_list.append(res_list.index(max(res_list)))
        print(number_list)
        return img

        # 模板匹配 针对常规数字

    def matching_card2(self, list, contours, img, gray, thresh):
        number = []  # 银行卡数字
        for l in list:
            x, y, w, h = cv.boundingRect(contours[l])

            # img1 = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # print(x, y, w, h)
            # cv.imshow("img1", img1)     # 数字轮廓

            img_c = gray.copy()
            img_number = img_c[y - 10: y + h + 10, x - 10:x + w + 10]
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
                    max_list = []
                self.max_list.append(res_list.index(max(res_list)))
                if len(self.max_list) == 4:
                    for i in self.max_list:
                        cv.putText(img, "".join(str(i)), (x + 9, y - 5), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255),
                                   2)
                        x = x + 25
                    self.max_list = []
                number.append(res_list.index(max(res_list)))
        print(number)
        return img



tmp = Template()

