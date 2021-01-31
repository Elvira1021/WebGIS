# -*- coding:utf-8 -*-
import pandas as pd
import requests
from requests.exceptions import ReadTimeout, ConnectTimeout
import csv
from selenium import webdriver
import time


def transform(geo):
    parameters = {'address': geo, 'key': '你的官网申请的KEY'}
    base = 'https://restapi.amap.com/v3/geocode/geo?'
    try:
        response = requests.get(base, parameters, timeout=2)
        if response.status_code == 200:
            answer = response.json()
            # print(answer)
            if answer['geocodes']:
                loc = answer['geocodes'][0]
                loc1 = loc['location']
            else:
                loc1 = 0
        else:
            pass
    except (ReadTimeout, ConnectTimeout):
        pass
    return loc1


def hotspot():
    file = pd.read_csv("D:\\DATA\\heatmapData.csv", encoding='gbk')
    new_data = file.dropna(axis=0, how='any')
    with open("D:\\DATA\\heatmapData.js", "a") as f:
        f.write('var heatmapData = [' + '\n')
        for ite in range(len(new_data)):
            location = transform(new_data.iloc[ite][0])
            lng = float(location.split(',')[0])     # latitude
            lat = float(location.split(',')[1])     # longitude
            count = new_data.iloc[ite][1]           # instead of ix.values
            dic = {"lng": lng,
                   "lat": lat,
                    "count": count}
            f.write('{}'.format(dic) + ',\n')
        f.write('];')
        f.close()

def browse():
    driver = webdriver.Chrome()
    driver.get("D:\\DATA\\heatmap.html")
    driver.maximize_window()
    time.sleep(60)


if __name__ == "__main__":
    hotspot()
    # browse()