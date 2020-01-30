# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import json

g = sys.argv
print g[0]

if (len(g) <= 1):
    json_file = 'data/linhas2.json'
    with open(json_file) as json_data:
        data = json.load(json_data)
        data = sorted(data, key=lambda d: (d["nome"]))
        lista = ''
        for index, item in enumerate(data):
            print (str(index) + ' : ' + str(item['cod']) + ' ' + str(item['nome']))
            lista += '<option value="'+str(item['cod']).lower()+'">'+str(item["cod"])+' - '+str(item["nome"])+'</option>'
            os.system('python linha-html.py '+ str(item['cod']).lower())

    template = 'tpl-index.html'
    fileName = 'html/index.html'
    with open(template, 'r') as file :
        filedata = file.read()
        newFiledata = filedata
        newFiledata = newFiledata.replace('--LINHAS--', lista)
    with open(fileName, 'w') as file:
        file.write(newFiledata)

else:
    os.system('python linha-html.py '+g[1])