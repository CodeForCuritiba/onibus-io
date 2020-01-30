# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import json
import os

json_file = 'data/linhas2.json'

with open(json_file) as json_data:
    data = json.load(json_data)

    for index, item in enumerate(data):
        print item['cod'].lower() + ' ' +item['nome']
        fileName = 'data/linha-'+item['cod'].lower()+'.json'
        with open(fileName, 'w') as json_file:
            json.dump(item, json_file)
