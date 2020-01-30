# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import json
import os
import pyqrcode

json_file = 'data/linhas2.json'

with open(json_file) as json_data:
    data = json.load(json_data)

    for index, item in enumerate(data):
        #if (index >= 0 and index < 142):
            url = pyqrcode.create('https://onibus.io/' + item['cod'].lower() + '.html')
            url.svg('html/i/linha-qr-'+item['cod'].lower()+'.svg', scale=8)
            url.png('html/i/linha-qr-'+item['cod'].lower()+'.png', scale=8)
            print (str(index) + ' : ' + str(item['cod']) + ' ' + str(item['nome']))