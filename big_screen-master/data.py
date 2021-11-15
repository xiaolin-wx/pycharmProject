#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

import json
from app import *


class SourceDataDemo:

    def __init__(self):
        self.title = '疫情统计'
        self.counter = {'name': '截止今日出院人数', 'value': 86397}
        self.counter2 = {'name': '截止今日死亡人数', 'value': 4636}
        self.echart1_data = {
            'title': '累计死亡人数',
            'data': [
                {"name": "1月", "value": 4634},
                {"name": "2月", "value": 2870},
                {"name": "3月", "value": 3300},
                {"name": "4月", "value": 4633},
                {"name": "5月", "value": 4634},
                {"name": "6月", "value": 4634},
                {"name": "7月", "value": 4634},
                {"name": "8月", "value": 4634},
                {"name": "9月", "value": 4634},
                {"name": "10月", "value": 4634},
                {"name": "11月", "value": 4634},
                {"name": "12月", "value": 4634},
            ]
        }
        self.echart2_data = {
            'title': '累计出院人数',
            'data': [
                {"name": "1月", "value": 83314},
                {"name": "2月", "value": 41625},
                {"name": "3月", "value": 75448},
                {"name": "4月", "value": 77642},
                {"name": "5月", "value": 78307},
                {"name": "6月", "value": 78479},
                {"name": "7月", "value": 78974},
                {"name": "8月", "value": 80208},
                {"name": "9月", "value": 80594},
                {"name": "10月", "value": 80984},
                {"name": "11月", "value": 81631},
                {"name": "12月", "value": 82050},
            ]
        }
        self.echarts3_1_data = {
            'title': '1月疫情情况',
            'data': [
                {"name": "累计确诊", "value": 1711},
                {"name": "累计出院", "value": 83314},
                {"name": "累计死亡", "value": 4634},
            ]
        }
        self.echarts3_2_data = {
            'title': '2月疫情情况',
            'data': [
                {"name": "累计确诊", "value": 35329},
                {"name": "累计出院", "value": 41625},
                {"name": "累计死亡", "value": 2870},
            ]
        }
        self.echarts3_3_data = {
            'title': '3月疫情情况',
            'data': [
                {"name": "累计确诊", "value": 2691},
                {"name": "累计出院", "value": 75448},
                {"name": "累计死亡", "value": 3300},
            ]
        }
        self.echart4_data = {
            'title': '疫情实况分析',
            'data': [
                {"name": "出院",
                 "value": [83314, 41625, 75448, 77642, 78307, 78479, 78974, 80208, 80594, 80984, 81631, 82050]},
                {"name": "死亡", "value": [4634, 2870, 3300, 4633, 4634, 4634, 4634, 4634, 4634, 4634, 4634, 4634]},
            ],
            'xAxis': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        }
        self.echart5_data = {
            'title': '累计确诊病例',
            'data': [
                {"name": "1月", "value": 1711},
                {"name": "2月", "value": 35329},
                {"name": "3月", "value": 2691},
                {"name": "4月", "value": 599},
                {"name": "5月", "value": 63},
                {"name": "6月", "value": 421},
                {"name": "7月", "value": 684},
                {"name": "8月", "value": 216},
                {"name": "9月", "value": 186},
                {"name": "10月", "value": 355},
                {"name": "11月", "value": 277},
                {"name": "12月", "value": 370},
            ]
        }
        self.echart6_data = {
            'title': '治愈率,死亡率',
            'data': [
                {"name": "出院人数", "value": 86397, "value2": 4636, "color": "01", "radius": ['94%','5%']},
                {"name": "死亡人数", "value": 4636, "value2": 86397, "color": "01", "radius": ['94%','5%']},
                {"name": "未出院人数", "value": 501, "value2": 91534, "color": "01", "radius": ['1%', '94%']},

            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '武汉', 'value': 239},
                {'name': '北京', 'value': 239},
                {'name': '海口', 'value': 239},
            ]
        }

    @property  # 是python的一种修饰器 用来修饰方法，可以使用@property创建只读属性，并转换为名称相同的只读属性可以与所定义的属性配合使用这样可以防止属性被修改
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """

        super().__init__()
        self.title = '疫情统计'
        self.counter = {'name': '累计出院人数', 'value': 86397}
        self.counter2 = {'name': '累计死亡人数', 'value': 4636}
        self.echart1_data = {
            'title': '累计死亡人数',
            'data': [
                {"name": "10月", "value": 4634},
                {"name": "11月", "value": 4634},
                {"name": "12月", "value": 4634},
                {"name": "1月", "value": 4634},
                {"name": "2月", "value": 2870},
                {"name": "3月", "value": 3300},
                {"name": "4月", "value": 4633},
                {"name": "5月", "value": 4634},
                {"name": "6月", "value": 4634},
                {"name": "7月", "value": 4634},
                {"name": "8月", "value": 4634},
                {"name": "9月", "value": 4634},
            ]
        }


class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')


class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')
