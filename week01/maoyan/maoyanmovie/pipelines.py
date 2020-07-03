# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
 
class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        category = item['category']
        date = item['date']
        movie_info = [[title, category, date]]
        df = pd.DataFrame(movie_info[:10], columns=['title', 'category', 'date'])
        df.to_csv('./maoyanmovies_2.csv',mode='a',encoding='utf-8-sig',index=False,header=True)

        return item
