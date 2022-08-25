import pandas as pd
import scrapy
import json
import csv
from get_std_code import get_min_max_by_code
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from get_mark import get_student_mark


class crawl_data_from_web_1(scrapy.Spider):
    name = 'spider1'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(1, 9)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)        
class crawl_data_from_web_2(scrapy.Spider):
    name = 'spider2'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(9, 17)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi) 
  
class crawl_data_from_web_3(scrapy.Spider):
    name = 'spider3'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(17, 25)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)

class crawl_data_from_web_5(scrapy.Spider):
    name = 'spider5'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(25, 33)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi) 
  
class crawl_data_from_web_6(scrapy.Spider):
    name = 'spider6'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(33, 41)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)
 
class crawl_data_from_web_7(scrapy.Spider):
    name = 'spider7'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(41, 49)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)

class crawl_data_from_web_4(scrapy.Spider):
    name = 'spider4'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(49, 57)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)

class crawl_data_from_web_8(scrapy.Spider):
    name = 'spider8'
    def start_requests(self):
        list_provide = ['{0:02}'.format(num) for num in range(57, 65)]
        for provide_id in list_provide:
            max_sbd = get_min_max_by_code(provide_id)
            for last_sbd in range(1, max_sbd):
                prefix = ''.join(['0' for i in range(6 - len(str(last_sbd)))])
                sbd = f'{provide_id}{prefix}{last_sbd}'
                start_urls = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}.json'.format(sbd)
                yield scrapy.Request(url=start_urls, callback=self.send_status)
    
    def send_status(self, response):
        infor = response.text
        data_obj = json.loads(infor)
        infor = response.text
        data_obj = json.loads(infor)
        diemthi = get_student_mark(data_obj)
        diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
        with open('/output/diemthi.csv', 'a') as f:
            file_writer = csv.DictWriter(f, fieldnames=diem_dict)
            file_writer.writerows(diemthi)
  
if __name__ == '__main__':
    diem_dict = ['So bao danh', 'Tinh', 'Toan', 'Van', 'Ngoai ngu', 'Ma ngoai ngu', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'GDCD']
    with open('/output/diemthi.csv', 'a') as f:
        file_writer = csv.DictWriter(f, fieldnames=diem_dict)
        file_writer.writeheader()    
    settings = get_project_settings()
    process = CrawlerRunner(settings)
    process.crawl(crawl_data_from_web_1)
    process.crawl(crawl_data_from_web_2)
    process.crawl(crawl_data_from_web_3)
    process.crawl(crawl_data_from_web_4)
    process.crawl(crawl_data_from_web_5)
    process.crawl(crawl_data_from_web_6)
    process.crawl(crawl_data_from_web_7)
    process.crawl(crawl_data_from_web_8)
    d = process.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

