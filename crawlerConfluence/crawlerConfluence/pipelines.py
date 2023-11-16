# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class CrawlerconfluencePipeline:
    def process_item(self, item, spider):
        print('################ 获取Content ################')
        title = item['title']
        url = item['url']
        # html = html_template.format(content=content)
        file_name = title
        print(file_name)
        file_name = os.path.join(os.path.abspath('.'), 'urls', file_name)
        print(file_name)
        with open(file_name, 'a+', encoding='utf-8') as f:
            f.write(url)
