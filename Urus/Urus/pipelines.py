import os
from urllib import request

class UrusPipeline(object):

    def __init__(self):
        #os.path.dirname()获取当前文件的路径,os.path.join()获取当前目录并拼接成新目录
        self.path = os.path.join(os.path.dirname(__file__), 'images')

        # 判断路径是否存在
        if not os.path.exists(self.path):  
            os.mkdir(self.path)

    def process_item(self, item, spider):

        #分类存储
        catagory = item['catagory']
        urls = item['image_urls']

        catagory_path = os.path.join(self.path, catagory)

        #如果没有该路径即创建一个
        if not os.path.exists(catagory_path): 
            os.mkdir(catagory_path)

        for url in urls:
            #以_进行切割并取最后一个单元
            image_name = url.split('_')[-1] 
            request.urlretrieve(url,os.path.join(catagory_path,image_name))

        return item