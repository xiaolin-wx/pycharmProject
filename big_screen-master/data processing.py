#  -*- coding:utf-8 -*-
import glob
import os

# 打开文件
import re

import xlrd
import xlwt
from xlutils.copy import copy
from numpy import unicode



def walkfile(path):
    file_li = []
    for root, dirs, files in os.walk(path):
        file_li = files
    for file in file_li:
        ab_path = os.path.join('doc', file)
        with open(ab_path, 'r', encoding='utf8') as f:
            results = f.read()
            # print(results)
            raw_data = re.compile('(.*?)，.*?截至.*?确诊病例(.*?)例.*?出院病例(.*?)例.*?死亡病例(.*?)例.*?报告确诊病例(.*?)例.*?006', re.S)
            fine_data = re.findall(raw_data, results)
            print(fine_data)
            data = xlrd.open_workbook('武汉疫情统计.xls')    #打开excel表格
            wb=copy(data)                       #复制excel
            mysheet = wb.get_sheet(0)           #从复制的文件中得到的一个sheet
            i =len(mysheet.rows)            #获取最后一列
            for item in fine_data:
                时间 = item[0]
                新增确证病例 = item[1]
                境外输入病例 = item[2]
                本土病例 = item[3]
                新增治愈出院病例 = item[4]
                密切接触者 = item[5]
                境外输入确诊病例 = item[6]
                累计确诊病例 = item[7]
                累计出院病例 = item[8]

                # print(item[5])
                mysheet.write(i, 0, 时间)
                mysheet.write(i, 1, 新增确证病例)
                mysheet.write(i, 2, 境外输入病例)
                mysheet.write(i, 3, 本土病例)
                mysheet.write(i, 4, 新增治愈出院病例)
                mysheet.write(i, 5, 密切接触者)
                mysheet.write(i, 6, 境外输入确诊病例)
                mysheet.write(i, 7, 累计确诊病例)
                mysheet.write(i, 8, 累计出院病例)
                i += 1
            wb.save('武汉疫情统计.xls')
            print('写入成功')

def main():
    walkfile(r'./doc')


if __name__ == '__main__':
    main()
