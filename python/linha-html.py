# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import json
import os
import re
import subprocess

def sort_json(json_data):
    horarios = json_data["tabela"]
    return sorted(horarios, key=lambda d: (d["dia"],d["tabela"]))

def sortTable(horarios):
    return sorted(horarios, key=lambda d: (d["ponto"],d["dia"]))

def sortPontos(pontos):
    return sorted(pontos, key=lambda d: (d["itinerary_id"],int(d["seq"])))

def buildHeader():
    lista = '<h1><span class="'+str(data["cor"]).lower()+'">'+str(data["cod"])+'</span> '+str(data["nome"])+'</h1>'
    lista += '<p class="info">'+str(data["categoria_servico"]).capitalize()+' / Cor: '+str(data["cor"])+'</p>'
    lista += '<div class="info-b"><span>https://</span>onibus.io/<b>' + data['cod'].lower() + '</b>/</div>'
    lista += '<div class="qr"><img src="i/linha-qr-'+str(data["cod"]).lower()+'.png" /></div>'
    return lista

def buildPontos(pontos):
    lista = '<div class="ui-pontos-panel ver '+str(data["cor"]).lower()+'">'
    lastItinerario = ''
    for index, item in enumerate(pontos):
        title =  ' title="' + str(pontos[index]['seq'].encode('utf-8')) + ' - ' + str(pontos[index]['itinerary_id'].encode('utf-8')) + ' - sentido:' + str(pontos[index]['sentido'].encode('utf-8')) + '"'
        if (pontos[index]['itinerary_id'] != lastItinerario):
            if (lastItinerario != '') and pontos[index]['itinerary_id'] != lastItinerario:
                lista += '</ul>'
            #lista += '<h3>sentido: '+ str(pontos[index]['sentido'].encode('utf-8')) + '</h3>'
            lista += '<ul data-itinerary-id="'+pontos[index]['itinerary_id'] +'">'
        lista += '<li'+title+' data-seq="' + str(pontos[index]['seq'].encode('utf-8')) + '" data-itinerary-id="' + str(pontos[index]['itinerary_id'].encode('utf-8')) + '" data-sentido="' + str(pontos[index]['sentido'].encode('utf-8')) + '">' + str(pontos[index]['nome'].encode('utf-8')) + '</li>'+'\n'
        
        lastItinerario = pontos[index]['itinerary_id']
    lista += '</ul></div>'
    return lista

def buildTable(horarios):
    lista = '<div class="ui-table-panel">'
    horaAnt = '';
    for index, item in enumerate(horarios):
        hora = re.search('(^[0-9]{2})',str(horarios[index]['hora'])).group(1)
        minuto = re.search('(:[0-9]{2})',horarios[index]['hora']).group(1)
        novaHora = 'h-block'
        if (hora != horaAnt):
            novaHora += ' nl'
        if (int(hora) % 2 == 0):
            novaHora += ' odd'
        if (horarios[index]['ponto'] != horarios[(index-1)]['ponto']):
            if (horaAnt != ''):
                lista += '</ul></div>'
            lista += '<h3>' + str(horarios[index]['ponto']) + '</h3>'
        if (horarios[index]['dia'] == '1' and (horarios[index]['dia'] != horarios[(index-1)]['dia']) or (horarios[index]['ponto'] != horarios[(index-1)]['ponto'])):
            lista += str("<div class=\"dia dia-1\"><h4>DIA ÚTIL</h4>")
            lista += '<ul class="schedule schedule-table schedule-a">'
        if (horarios[index]['dia'] == '2' and horarios[index]['dia'] != horarios[(index-1)]['dia']):
            lista += '</ul></div>' + '\n'
            lista += str("<div class=\"dia dia-2\"><h4>SÁBADO</h4>" + '\n')
            lista += '<ul class="schedule schedule-table schedule-b">'
        if (horarios[index]['dia'] == '3' and horarios[index]['dia'] != horarios[(index-1)]['dia']):
            lista += '</ul></div>' + '\n'
            lista += str("<div class=\"dia dia-3\"><h4>DOMINGOS E FERIADOS</h4>" + '\n')
            lista += '<ul class="schedule schedule-table schedule-c">'
        lista += "<li data-dia=\""+str(horarios[index]['dia'])+"\" class=\"" + str(novaHora) + "\"><b>" + str(hora) + "</b>" + str(minuto) + "</li>"
        horaAnt = hora
        

    lista += '</ul></div></div>'
    return lista
        
def saveHTML():
    template = 'tpl-linha-onibus.html'
    fileName = 'html/'+g[1]+'.html'
    with open(template, 'r') as file :
        filedata = file.read()

        newFiledata = filedata
        newFiledata = newFiledata.replace('--TITLE--', str(data["cod"])+' - '+str(data["nome"]))
        newFiledata = newFiledata.replace('--PONTOS--', str(saidaPontos))
        newFiledata = newFiledata.replace('--HORARIOS--', str(saidaHorarios))
        newFiledata = newFiledata.replace('--HEADER--', str(saidaCabecalho))

    with open(fileName, 'w') as file:
        file.write(newFiledata)

g = sys.argv

json_file = 'data/linha-'+g[1]+'.json'

with open(json_file) as json_data:
    data = json.load(json_data)

horarios = sortTable(data["tabela"])
pontos = sortPontos(data["pontos"])

saidaHorarios = buildTable(horarios)
saidaPontos = buildPontos(pontos)

saidaCabecalho = buildHeader()

saveHTML()