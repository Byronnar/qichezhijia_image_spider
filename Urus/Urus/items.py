import scrapy

class UrusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 存储图片分类
    catagory = scrapy.Field()

    # 存储图片地址
    image_urls = scrapy.Field()

    # ImagesPipeline 
    images = scrapy.Field()