import scrapy
import psycopg2
import csv
from scrapy.crawler import CrawlerProcess


class crawl_data_from_web(scrapy.Spider):
    name = 'diemchuan'
    def start_requests(self):
        start_urls = 'https://diemthi.tuyensinh247.com/diem-chuan.html'
        yield scrapy.Request(url=start_urls, callback=self.parse_find)
    def parse_find(self, response):
        # cnt = psycopg2.connect(
        #     database='""',
        #     user='',
        #     password='',
        #     host='localhost',
        #     port='5432'
        #     )
        # cursor = cnt.cursor()
        # sql = '''CREATE TABLE university(
        #     id BIGSERIAL NOT NULL,
        #     name VARCHAR(100),
        #     code VARCHAR(20),
        #     url VARCHAR(150)
        # )'''
        # cursor.execute(sql)
        ind = 0
        for uni_info in response.xpath('//*[@id="benchmarking"]/li'):
            ind += 1
            url ='https://diemthi.tuyensinh247.com' + uni_info.xpath('a/@href').get()
            university_name = uni_info.xpath('a/@title').get()
            university_code = uni_info.xpath('a/strong/text()').get() if uni_info.xpath('a/strong/text()').get() != None else ''
            # cursor.execute("INSERT INTO university(id, name, code, url) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;", (ind,university_name,university_code,url))
            yield scrapy.Request(url=url, callback=self.parse_follow)
        # cnt.commit()
        # cnt.close()
        
    def parse_follow(self, response):
        data = response.css('tr.bg_white')
        for uni in data:
            major_code = uni.xpath('td[2]/text()').get()
            major_name = uni.xpath('td[3]/text()').get()
            subject_groups = list(uni.xpath('td[4]/text()').get().replace(";","").split(" "))
            point = uni.xpath('td[5]/text()').get()
            note = uni.xpath('td[6]/text()').get().replace(";",".")
            diemchuan_obj = [major_code, major_name, subject_groups,point,note]
            for subject_group in subject_groups:
                diemchuan_obj = [major_code, major_name, subject_group,point,note]
                with open('/output/diemchuan.csv', 'a') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(diemchuan_obj)
 
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(crawl_data_from_web)
    process.start()
