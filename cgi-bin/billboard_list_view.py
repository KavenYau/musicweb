'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
from template.httputils import setParaAndContext
import cgitb
cgitb.enable()


import template.yate as yate
import service.billboard_service as billboard_service

def make_billboard_list(billboard_list):
    print(yate.table_start(billboard_service.BILLBOARD_SIZE,10,10))
    print(yate.table_tr_start())
    print(yate.table_th('rank'))
    print(yate.table_th('language'))
    print(yate.table_th('title'))
    print(yate.table_th('author'))
    print(yate.table_th('album_title'))
    print(yate.table_th('artist_name'))
    print(yate.table_th('listening'))
    print(yate.table_tr_end())
    
    try:
        #i = 0
        for each in billboard_list:
            print(yate.table_tr_start())
            print(yate.table_td(each.rank))
            print(yate.table_td(each.language))
            print(yate.table_td(each.title))
            print(yate.table_td(each.author))
            print(yate.table_td(each.album_title))
            print(yate.table_td(each.artist_name))
            print(yate.table_td(yate.link("play_song.py?song_id=%d" % (int(each.song_id)), 'listen')))
            print(yate.table_tr_end())
            #i+=1
    except IndexError as indexerr:
        print("IndexError:",indexerr)
    print(yate.table_end())

#print(setParaAndContext("Content-Type"))

print('<html>')
print('<head>')
print('<title>Billboard List</title>')
print('</head>')
print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
print('<body>')
print('<h2>Billboard List:</h2>')
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_NEW),'新歌'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_HOT),'热榜'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_ROCK),'摇滚'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_JAZZ),'爵士'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_EA),'欧美金曲榜'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_OLD),'经典老歌榜'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_LOVER),'情歌对唱榜'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_FILM),'影视金曲榜'))
print(yate.link("choose_billboard_list.py?billboard_type=%d" % (billboard_service.BILLBOARD_INTERNET),'网络歌曲榜'))
print(yate.start_form('book_detail_view.py'))
billboard_list=billboard_service.get_billboard_dict(billboard_service.BILLBOARD_NEW)

make_billboard_list(billboard_list)
#print(billboard_list)
#for book_name in book_dict:
    #print(yate.radio_button('bookname',book_dict[book_name].name))

print(yate.end_form('detail'))
print(yate.link("/index.html",'Home'))
print('</body>')
print('</html>')


