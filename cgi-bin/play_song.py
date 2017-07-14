'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
from template.httputils import setParaAndContext
import cgitb
cgitb.enable()

import cgi
import template.yate as yate
import service.billboard_service as billboard_service


def show_song_info(song_info):
    print(yate.table_start(1, 10, 10))
    print(yate.table_tr_start())
    print(yate.table_th('songName'))
    print(yate.table_th('artistName'))
    print(yate.table_th('albumName'))
    print(yate.table_th('lrcLink'))
    print(yate.table_th('songLink'))
    print(yate.table_th('showLink'))
    print(yate.table_th('rate'))
    print(yate.table_th('size'))
    print(yate.table_tr_end())

    try:
        print(yate.table_tr_start())
        print(yate.table_td(song_info.songName))
        print(yate.table_td(song_info.artistName))
        print(yate.table_td(song_info.albumName))
        #print(yate.table_td(song_info.lrcLink))
        print(yate.table_td(yate.link(song_info.lrcLink, 'lrcLink')))
        print(yate.table_td(yate.link(song_info.songLink, 'songLink')))
        print(yate.table_td(yate.link(song_info.showLink, 'showLink')))
        #print(yate.table_td(song_info.songLink))
        #print(yate.table_td(song_info.showLink))
        print(yate.table_td(str(song_info.rate)))
        print(yate.table_td(str(song_info.size)))
        print(yate.table_tr_end())
    except IndexError as indexerr:
        print("IndexError:", indexerr)
    print(yate.table_end())


form_data = cgi.FieldStorage()




#print(setParaAndContext("Content-Type"))
print("Content-type:text/html\n")
print('<html>')
print('<head>')
print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
print('<title>Billboard List</title>')
print('</head>')
print('<body>')
print('<h2>Billboard List:</h2>')
try:
   song_id = form_data['song_id'].value
except KeyError as kerr:
    print(yate.para('err billboard type...'))

song_info = billboard_service.get_song_info(int(song_id))
show_song_info(song_info)

print(yate.link("/index.html",'Home'))
print('</body>')
print('</html>')


