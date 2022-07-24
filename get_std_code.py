import requests
import json


def build_sbd(provide_id, last_sbd):
    prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
    sbd = f'{provide_id}{prefix}{last_sbd}'
    return sbd


def get_min_max_by_code(provide_id):
    session = requests.Session()
    min = 1
    max = 110000
    sbd = max
    should_find = True
    mid = int((max - min) / 2) + min
    while (should_find):
        if ((min - max) ** 2) == 1:
            break
        mid = int((max - min) / 2) + min
        sbd = build_sbd(provide_id=provide_id, last_sbd=mid)
        url = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(
            sbd)
        if session.get(url).status_code != 200:
            max = mid
            continue
        else:
            min = mid
            continue
    return mid


def get_max_sbd(provide_id):
    session = requests.Session()
    min = 1
    max = 100000
    sbd = max
    should_find = True
    mid = int((max - min) / 2) + min
    while (should_find):
        if ((min - max) ** 2) == 1:
            break
        mid = int((max - min) / 2) + min
        sbd = build_sbd(provide_id=provide_id, last_sbd=mid)
        url = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(
            sbd)
        data = json.loads(session.get(url=url).text)
        if data == []:
            max = mid
            continue
        else:
            min = mid
            continue
    return mid
