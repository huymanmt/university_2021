import scrapy
import csv
import json
from get_std_code import get_max_sbd
from get_mark import get_mark_2022
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner

class crawl_mark_from_web_1(scrapy.Spider):
    name = 'diemthi1'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(1, 7)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_2(scrapy.Spider):
    name = 'diemthi2'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(7, 13)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_3(scrapy.Spider):
    name = 'diemthi3'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(13, 19)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_4(scrapy.Spider):
    name = 'diemthi4'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(19, 25)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_5(scrapy.Spider):
    name = 'diemthi5'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(25, 31)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_6(scrapy.Spider):
    name = 'diemthi6'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(31, 37)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_7(scrapy.Spider):
    name = 'diemthi7'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(37, 43)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_8(scrapy.Spider):
    name = 'diemthi8'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(43, 49)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_9(scrapy.Spider):
    name = 'diemthi9'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(49, 55)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj)
class crawl_mark_from_web_10(scrapy.Spider):
    name = 'diemthi10'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(55, 65)]
        for provide_id in list_provide:
            max_sbd = get_max_sbd(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={}'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    def send_status(self, response):
        data = json.loads(response.text)
        for i in data:
            data_obj = get_mark_2022(i)
            diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
            with open('./output/diemthi2022.csv', 'a') as f:
                file_writer = csv.DictWriter(f, fieldnames=diem_dict)
                file_writer.writerows(data_obj) 

if __name__ == '__main__':
    diem_dict = ['Sbd', 'Toan', 'Van', 'Ngoaingu', 'Ma_ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
    with open('./output/diemthi2022.csv', 'a') as f:
        file_writer = csv.DictWriter(f, fieldnames=diem_dict)
        file_writer.writeheader()  
    settings = get_project_settings()
    process = CrawlerRunner(settings)
    process.crawl(crawl_mark_from_web_1)
    process.crawl(crawl_mark_from_web_2)
    process.crawl(crawl_mark_from_web_3)
    process.crawl(crawl_mark_from_web_4)
    process.crawl(crawl_mark_from_web_5)
    process.crawl(crawl_mark_from_web_6)
    process.crawl(crawl_mark_from_web_7)
    process.crawl(crawl_mark_from_web_8)
    process.crawl(crawl_mark_from_web_9)
    process.crawl(crawl_mark_from_web_10)
    d = process.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()