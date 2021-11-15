#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:
import xlrd
from flask import Flask, render_template
from data import *

app = Flask(__name__)


@app.route('/')
def index():
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/corp')
def corp():
    data = CorpData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/job')
def job():
    data = JobData()
    return render_template('index.html', form=data, title=data.title)


# def get_data(file_path):
#     Excel_data = xlrd.open_workbook(file_path)
#     my_sheet = Excel_data.sheet_by_index(0)
#     row_num = my_sheet.nrows  # 获取行
#     col_num = my_sheet.ncols
#     if len(str(row_num)) < 2:
#         print('Excel表格数据为空！！！')
#     else:
#         l = []
#         for i in range(1, row_num):
#             for j in range(col_num):
#                 title = my_sheet.row_values(0)[j]
#                 data = my_sheet.row_values(i)[j]
#                 sheet_data = {title: data}
#                 l.append(sheet_data)
#         # print(l)
#         return l


if __name__ == "__main__":
    # file_path = 'C:/Users/GJ/Desktop/112.xls'
    # get_data(file_path)
    app.run(host='127.0.0.1', debug=False)
