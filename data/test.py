import csv
import math
import json
import requests


def request_url_get(url):
    """ 请求url方法get方法 """
    try:
        r = requests.get(url=url, timeout=30)
        if r.status_code == 200:
            return r.text
        return None
    except requests.RequestException:
        print('请求url返回错误异常')
        return None


def parse_json(content_json):
    """  解析json函数 """
    result_json = json.loads(content_json)
    return result_json


def request_api(url):
    """ 请求高德api 解析json """
    result = request_url_get(url)
    result_json = parse_json(result)
    return result_json


def run():
    """ 运行函数 """
    keywords = '消防水池'
    city = 'hangzhou'
    key = 'f502d894f55351ea72790cfc88cbf6c8'
    offset = 20

    index_url = f'https://restapi.amap.com/v3/place/text?keywords={keywords}&city={city}&' \
                f'offset={offset}&page=1&key={key}&extensions=base'
    index_result = request_api(index_url)
    pages = math.ceil(int(index_result['count']) / offset)  # 算出一共需要的总页数

    headers = ['address', 'pname', 'cityname', 'type', 'typecode', 'adname', 'name', 'location', 'tel', 'id']
    rows = []

    for page in range(1, pages + 1):
        url = f'https://restapi.amap.com/v3/place/text?keywords={keywords}&city={city}&' \
              f'offset={offset}&page={page}&key={key}&extensions=base'
        result = request_api(url)
        for res in result['pois']:
            row = []
            for dict_key in headers:
                if dict_key in res:
                    row.append(res[dict_key])
                else:
                    row.append('')
            rows.append(row)
    with open('pool.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    run()
