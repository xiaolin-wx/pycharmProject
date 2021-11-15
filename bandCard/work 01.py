import cv2 as cv
import numpy as np
from imutils import contours
import imutils
import skimage
from skimage import io,data,color,filters
import matplotlib.pyplot as plt



#卡号提取
#01
def getmodel():
    # 处理模板图片
    img = cv.imread("./picture/alltemplate.png")
    # img = cv.imread("./image/workimg/ocr_a_reference.png")
    # img = cv.imread("./image/workimg/model3-2-1.png")

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ref = cv.threshold(img_gray, 10, 255, cv.THRESH_BINARY_INV)[1]
    #查找轮廓，从左往右
    refCnts = cv.findContours(ref.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # 画出找到的轮廓
    #cv.drawContours(img.copy(), refCnts, -1, (0, 0, 255), 3)
    refCnts = imutils.grab_contours(refCnts)
    refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]
    digits = {}
    #遍历每一个轮廓  i为数字  c是轮廓
    for (i, c) in enumerate(refCnts):
        # 计算外接矩形并且resize成合适大小
        (x, y, w, h) = cv.boundingRect(c)  # x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
        roi = ref[y:y + h, x:x + w]
        roi = cv.resize(roi, (57, 88))
        digits[i] = roi  #更新字典  每一个数字对应每一个模板
        cv.imshow('roi',digits[i])
    #内核
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 3))
    kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

    #加载银行卡
    # img1 = cv.imread("./image/image/card2.png")


    # img1 = cv.imread("./image/workimg/credit_card_01.png")
    img1 = cv.imread("./picture/credit_card_02.png")
    # img1 = cv.imread("./image/workimg/credit_card_03.png")
    # img1 = cv.imread("./image/workimg/credit_card_05.png")
    # img1 = cv.imread("./image/workimg/card7.png")
    # img1 = cv.imread("./image/workimg/card8.png")
    # img1 = cv.imread("./image/workimg/credit_card_04_bling.png")
    # img1 = cv.imread("./image/workimg/card_rotate.jpg")
    # img1 = cv.imread("./image/workimg/card6-compliex.png")




    img = imutils.resize(img1, width=300)
    # 高斯降噪
    # img_gauss = cv.GaussianBlur(img, (1, 1), 0)
    # 转灰度(计算速度)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 顶帽 (突出亮的区域)
    # kernel2 = cv.getStructuringElement(cv.MORPH_RECT,(26,7))
    tophat = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    # cv.imshow('gray',gray)
    cv.imshow('tophat',tophat)
    # 3、Scharr梯度
    # img_scharrx = cv.Scharr(tophat, cv.CV_64F, 1, 0)
    # img_scharrx = cv.convertScaleAbs(img_scharrx)
    # img_scharry = cv.Scharr(tophat, cv.CV_64F, 0, 1)
    # img_scharry = cv.convertScaleAbs(img_scharry)
    # scharrxy = cv.addWeighted(img_scharrx, 0.5, img_scharry, 0.5, 0)
    # cv.imshow('round',scharrxy)

    scharrxy = cv.Sobel(tophat, cv.CV_32F, 1, 0, ksize=-1)
    scharrxy = np.absolute(scharrxy)
    (minval, maxval) = (np.min(scharrxy), np.max(scharrxy))
    scharrxy = (255*((scharrxy-minval)/(maxval-minval)))
    scharrxy = scharrxy.astype("uint8")

    #闭操作 (将数字分段融合)
    gradx = cv.morphologyEx(scharrxy, cv.MORPH_CLOSE, kernel)
    thresh = cv.threshold(gradx, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    #再次闭操作
    thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel1)
    # cv.imshow('gray1', thresh)
    # 计算轮廓9
    threshCnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    threshCnts = imutils.grab_contours(threshCnts)

    # img2 = img.copy()
    # threshCnts = cv.drawContours(img2, threshCnts, -1, (0, 0, 255), 3)
    # cv.imshow('img2', threshCnts)

    #切割字符  遍历轮廓
    locs = []
    for (i, c) in enumerate(threshCnts):
        # 计算矩形
        (x, y, w, h) = cv.boundingRect(c)
        ar = w / float(h)
        # print(i, ":","rect->",(x, y, w, h), ar)
        #选择合适的区域
        if 2.5 < ar < 4.0:
            if (40 < w < 55) and (10 < h < 20):
                locs.append((x, y, w, h)) #符合的留下来

    print(locs)
    #将符合的轮廓从左到右排序
    locs = sorted(locs, key=lambda x:x[0])
    output = []
    result = img.copy()
    #遍历每一个轮廓中的数字
    for(i, (gX, gY, gW, gH)) in enumerate(locs):
        groupOutput = []
        #根据坐标提取每一个组
        group = gray[gY-5:gY+gH+5, gX-5:gX+gW+5]
        # cv.imshow("group", group)
        #预处理
        group = cv.threshold(group, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)[1]#二值化
        #把每个轮廓分为小轮廓
        digitCnts = cv.findContours(group.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        #排序
        digitCnts=imutils.grab_contours(digitCnts)
        digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]

        #计算每一组中的每一个数字
        for c in digitCnts:
            #找到当前数值的轮廓，resize成合适的大小
            (x, y, w, h) = cv.boundingRect(c)
            roi = group[y:y+h, x:x+w]  #取出小轮廓覆盖区域
            roi = cv.resize(roi, (57, 88))

            #计算匹配得分
            scores = []

            #digits是每个数字的模板
            #遍历模板匹配  计算每一个得分
            for(digit, digitROI) in digits.items():
                # 在所有的数字模板中进行匹配 TM_CCORR：计算相关性, 计算出来的值越大,越相关
                res = cv.matchTemplate(roi, digitROI, cv.TM_CCOEFF) #roi是X digitROI是0  依次是1,2...匹配10次
                (_, score, _, _) = cv.minMaxLoc(res)
                scores.append(score)

            groupOutput.append(str(np.argmax(scores))) #得到最合适的数字
        #画出来 (靠确定对角线来画矩形)
        cv.rectangle(result, (gX-5, gY-5), (gX+gW+5, gY+gH+5), (0, 0, 255), 2)
        cv.putText(result, "".join(groupOutput), (gX-4, gY-9), cv.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
        #结果
        output.extend(groupOutput)

    print("Credit Card:{}".format("".join(output)))
    # cv.imshow("result",result)
    res1=np.hstack((img,result))
    cv.imshow('res',res1)





if __name__ == "__main__":
    # open_xibao()
    # card()
    getmodel()
    # cv_show()
    # newcard()
    # mb()
    # qp()
    cv.waitKey(0)
    cv.destroyAllWindows()




