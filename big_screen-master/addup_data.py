import re

import xlrd


def get_excel_data(file_name):
    excel_data = xlrd.open_workbook(file_name)
    my_sheet = excel_data.sheet_by_index(0)
    row_num = my_sheet.nrows
    col_num = my_sheet.ncols
    if len(str(row_num)) < 2:
        print('没有数据!!!')
    else:
        d = []
        for i in range(1, row_num):
            d_1 = []
            for j in range(col_num):
                values = my_sheet.row_values(i)[j]
                d_1.append(values)
            d.append(d_1)
        # print(d)
        for i in d:
            sure=[]
            data_time = re.findall("\S'(.*?)月", str(i), re.S)
            print(str(data_time))
            if str(data_time) == "['10']":
                sure.append(i[1])

            else:
                print('null')
                pass


if __name__ == "__main__":
    file_name = '武汉easterpro.xls'
    get_excel_data(file_name)
