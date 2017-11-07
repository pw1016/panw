# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class QuotesPipeline(object):
    def process_item(self, item, spider):
        print("**************************************")
        print(item['text'])
        print(item['author'])
        print(item['tags'])
        return item


class XiaoHuarPipeline(object):
    def process_item(self, item, spider):
        if item and item['imgurl'] and item['imgurl'] != '':
            name = item['name']
            school = item['school']
            url = item['urlprefix'][0] + item['imgurl'][0]
            file_name = "%s_%s.jpg" % (school, name)
            folder_path = 'D:\\spider\\xiaohuar'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, file_name)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
            req = request.Request(url, headers=headers)
            with request.urlopen(req, timeout=30) as rep:
                if rep.getcode() == 200:
                    with open(file_path, 'wb') as f:
                        f.write(rep.read())
        return item


class SexyBeautyPipeline(object):
    def process_item(self, item, spider):
        if item and item['url'] and item['url'] != '':
            name = item['name'][0]
            url = item['url'][0]
            print(name, url)
            index1 = name.find('(')
            index2 = name.find(')')
            if index1 != -1:
                foldername = name[:index1]
                filename = name[index1 + 1:index2] + '.jpg'
            else:
                foldername = name
                filename = '1.jpg'
            folder = os.path.join("C:\\spider\\sexyBeauty", foldername)
            if not os.path.exists(folder):
                os.makedirs(folder)
            file_path = os.path.join(folder, filename)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
            req = request.Request(url, headers=headers)
            with request.urlopen(req, timeout=30) as rep:
                if rep.getcode() == 200:
                    with open(file_path, 'wb') as f:
                        f.write(rep.read())
        return item


class MmjpgPipeline(object):
    def process_item(self, item, spider):
        if item and item['url'] and item['url'] != '':
            name = item['name'][0]
            url = item['url'][0]
            print(name, url)
            index1 = name.find('(')
            index2 = name.find(')')
            if index1 != -1:
                foldername = name[:index1]
                filename = name[index1 + 1:index2] + '.jpg'
            else:
                foldername = name
                filename = '1.jpg'
            folder = os.path.join("C:\\spider\\mmjpg", foldername)
            if not os.path.exists(folder):
                os.makedirs(folder)
            file_path = os.path.join(folder, filename)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
            req = request.Request(url, headers=headers)
            with request.urlopen(req, timeout=30) as rep:
                if rep.getcode() == 200:
                    with open(file_path, 'wb') as f:
                        f.write(rep.read())
        return item
