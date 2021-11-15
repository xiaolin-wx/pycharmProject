import cv2 as cv


# 数字模板的拆解
class Template:

    template = cv.imread("images/alltemplate.png", 0)
    template_2 = cv.imread("images/template_2.png", 0)

    # 模板匹配 针对常规数字
    def matching_card(self, arraylist, contours, img, gray, thresh):
        number_list = []
        for l in arraylist:
            x, y, w, h = cv.boundingRect(contours[l])
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
                img_template = cv.imread("images/ocr_a_reference.png", 0)
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
                number = res_list.index(max(res_list))
                number_list.append(res_list.index(max(res_list)))
                cv.putText(img, str(number), (x + left+1, y-2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(number_list)
        return img

        # 模板匹配 针对常规数字

    def matching_card9(self, list, contours, img, gray, thresh):
        number_list = []
        for l in list:
            x, y, w, h = cv.boundingRect(contours[l])
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
                img_template = cv.imread("images/ocr_a_reference.png", 0)
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
                number = res_list.index(max(res_list))
                cv.putText(img, str(number), (x + left + 1, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                number_list.append(res_list.index(max(res_list)))
        print(number_list)
        return img

        # 模板匹配 针对常规数字

    def matching_card2(self, list, contours, img, gray, thresh):
        number_list = []  # 银行卡数字
        for l in list:
            x, y, w, h = cv.boundingRect(contours[l])
            img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # print(x, y, w, h)
            # cv.imshow("img1", img)     # 数字轮廓
            # cv.waitKey(0)
            # cv.destroyAllWindows()

            img_c = gray.copy()
            img_number = img_c[y - 10: y + h + 10, x - 10:x + w + 10]
            # img_number = img_number[0:, 0:136]
            flag = 0
            while flag < 4:
                if flag == 0:
                    left = 5
                    right = 40
                elif flag == 1:
                    left = 35
                    right = 79
                elif flag == 2:
                    left = 75
                    right = 109
                elif flag == 3:
                    left = 105
                    right = 175
                img_number = img_number.copy()
                one_number = img_number[:, left:right]
                flag = flag + 1

                # cv.imshow("one", one_number)
                # cv.waitKey(0)

                img_template = cv.imread("images/ocr_a_reference.png", 0)
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
                number_list.append(res_list.index(max(res_list)))
                print(res_list.index(max(res_list)))
                number = res_list.index(max(res_list))
                cv.putText(img, str(number), (x + left, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(number_list)
        return img

    def matching_card6(self, img, gray, arraylist, contours):
        number_list = []
        img_c = img.copy()
        for al in arraylist:
            label_img = cv.drawContours(img_c, contours[al], -1, (0, 0, 255), 2)
            x, y, w, h = cv.boundingRect(contours[al])
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # gray_c = gray.copy()
            # img_number = gray_c[y: y + h, x:x + w]
            # cv.imshow("img_number_1", img_number)
            # cv.imshow("label_img", label_img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            gray_c = gray.copy()
            array_img = gray_c[y: y + h, x:x + w]
            ret, thresh = cv.threshold(array_img, 70, 255, cv.THRESH_BINARY)
            # cv.imshow("thresh", thresh)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            if al == 5:
                print("进入5")
                for j in range(13):
                    if j == 0:
                        left = 9
                        right = 29
                    elif j < 6:
                        left = 22 * (j-1) + 33
                        right = left + 20
                    elif j == 6:
                        left = 142
                        right = left+20
                    elif j == 7:
                        left = 164
                        right = 184
                    elif j == 10:
                        left = 233
                        right = 253
                    elif 7 < j < 11:
                        left = 187 + 20 * (j-8)
                        right = left + 20
                    else:
                        left = 253 + 20 * (j - 11)
                        right = left + 20
                    one_number = thresh[:, left:right]
                    # cv.imshow("one_number", one_number)
                    # cv.waitKey(0)
                    # cv.destroyAllWindows()
                    template_copy = self.template_2.copy()
                    img_template = template_copy[45:-45, 14:-14]
                    res_list = []
                    for i in range(10):
                        left_m = 100 * i + 8
                        right_m = 100 * (i + 1) + 8
                        template_c = img_template.copy()
                        template_number = template_c[:, left_m:right_m]
                        template_size = cv.resize(template_number, None, fx=0.2, fy=0.2)
                        res = cv.matchTemplate(one_number, template_size, cv.TM_CCOEFF)
                        # print(one_number.shape)
                        # print(template_size.shape)
                        # cv.imshow("img_template", template_size)
                        # cv.imshow("one_number", one_number)
                        # cv.waitKey(0)
                        # cv.destroyAllWindows()
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                        res_list.append(max_val)
                    # print(res_list.index(max(res_list)))
                    number = res_list.index(max(res_list))
                    cv.putText(img, str(number), (x + left + 1, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    number_list.append(res_list.index(max(res_list)))
            else:
                for j in range(6):
                    left = 9 + 22 * j
                    right = left + 23
                    one_number = thresh[:, left:right]
                    # cv.imshow("thresh", thresh)
                    # cv.waitKey(0)
                    # cv.destroyAllWindows()
                    template_copy = self.template_2.copy()
                    img_template = template_copy[45:-45, 14:-14]
                    res_list = []
                    for i in range(10):
                        left_m = 100 * i + 8
                        right_m = 100 * (i + 1) + 8
                        template_c = img_template.copy()
                        template_number = template_c[:, left_m:right_m]
                        template_size = cv.resize(template_number, None, fx=0.2, fy=0.2)
                        res = cv.matchTemplate(one_number, template_size, cv.TM_CCOEFF)
                        # print(one_number.shape)
                        # print(template_size.shape)
                        # cv.imshow("img_template", template_size)
                        # cv.imshow("one_number", one_number)
                        # cv.waitKey(0)
                        # cv.destroyAllWindows()
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                        res_list.append(max_val)
                    # print(res_list.index(max(res_list)))
                    number = res_list.index(max(res_list))
                    cv.putText(img, str(number), (x + left + 1, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    number_list.append(res_list.index(max(res_list)))
        print(number_list)
        return img

    def matching_card10(self, img, arraylist, contours):
        number_list = []
        img_c = img.copy()
        template = self.template_2[45:-45, 14:-14]
        for al in arraylist:
            x, y, w, h = cv.boundingRect(contours[al])
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # print(x, y, w, h)
            array_number = img_c[y: y + h, x:x + w]
            array_number = cv.cvtColor(array_number, cv.COLOR_BGR2GRAY)
            ret, thresh = cv.threshold(array_number, 120, 255, cv.THRESH_BINARY)
            if al > 7:
                for i in range(4):
                    if al == 11:
                        if i == 0:
                            left = 0
                            right = 21
                        else:
                            left = 21 + 20 * (i - 1)
                            right = left+20
                    elif al == 10:
                        left = 20 * i
                        right = left + 20
                    elif al == 9:
                        if i == 0:
                            left = 0
                            right = left + 20
                        elif 0 < i < 3:
                            left = 19 + 20*(i-1)
                            right = left + 20
                        else:
                            left = 58
                            right = left + 20
                    else:
                        if i < 3:
                            left = 20 * i
                            right = left + 20
                        else:
                            left = 58
                            right = left + 20
                    # print(left, right)
                    one_number = thresh[:, left:right]
                    # cv.imshow("one_number", one_number)
                    # cv.waitKey(0)
                    # cv.destroyAllWindows()
                    res_list = []
                    for j in range(10):
                        left_m = 100 * j + 8
                        right_m = 100 * (j + 1) + 8
                        template_c = template.copy()
                        template_number = template_c[:, left_m:right_m]
                        template_size = cv.resize(template_number, None, fx=0.2, fy=0.2)
                        res = cv.matchTemplate(one_number, template_size, cv.TM_CCOEFF)
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                        res_list.append(max_val)
                    # print(res_list.index(max(res_list)))
                    number = res_list.index(max(res_list))
                    cv.putText(img, str(number), (x + left + 1, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    number_list.append(res_list.index(max(res_list)))
            else:
                for i in range(3):
                    left = 20*i
                    right = left+20
                    one_number = thresh[:, left:right]
                    res_list = []
                    for j in range(10):
                        left_m = 100 * j + 8
                        right_m = 100 * (j + 1) + 8
                        template_c = template.copy()
                        template_number = template_c[:, left_m:right_m]
                        template_size = cv.resize(template_number, None, fx=0.2, fy=0.2)
                        res = cv.matchTemplate(one_number, template_size, cv.TM_CCOEFF)
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                        res_list.append(max_val)
                    # print(res_list.index(max(res_list)))
                    number = res_list.index(max(res_list))
                    cv.putText(img, str(number), (x + left + 1, y - 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    number_list.append(res_list.index(max(res_list)))
        print(number_list)
        return img


tmp = Template()

