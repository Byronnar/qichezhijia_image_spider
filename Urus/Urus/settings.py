BOT_NAME = 'Urus'

SPIDER_MODULES = ['Urus.spiders']
NEWSPIDER_MODULE = 'Urus.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'Urus.pipelines.UrusPipeline': 1,
}