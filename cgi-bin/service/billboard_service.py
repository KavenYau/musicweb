'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
from model.Billboard import Billboard
from model.Song_Info import Song_Info
from template.httputils import http_get
import json

music_url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
billboard_url_values = "size=%d&type=%d&callback=cb_list&_t=1468380543284&format=json&method=baidu.ting.billboard.billList"

GET_SONG_URL_VALUES= "http://music.baidu.com/data/music/fmlink?rate=320&songIds=%d&type=&callback=cb_download&_t=1468380564513&format=json"

BILLBOARD_SIZE = 10
'''type: //1、新歌榜，2、热歌榜，
11、摇滚榜，12、爵士，16、流行
21、欧美金曲榜，22、经典老歌榜，23、情歌对唱榜，24、影视金曲榜，25、网络歌曲榜'''
BILLBOARD_NEW = 1
BILLBOARD_HOT = 2
BILLBOARD_ROCK = 11
BILLBOARD_JAZZ = 12
BILLBOARD_POP = 16
BILLBOARD_EA = 21
BILLBOARD_OLD = 22
BILLBOARD_LOVER = 23
BILLBOARD_FILM = 24
BILLBOARD_INTERNET = 25

def get_billboard_dict(billboard_type):
    #billboard_dict={}
    try:
        billboard_str = get_billboard(BILLBOARD_SIZE,billboard_type)
        #print(billboard_str[12:-2])
        #billboard_dict = json.loads(billboard_str[12:-2])
        #print(billboard_dict.keys())
        billboard = billboard_parse(billboard_str[12:-2],BILLBOARD_SIZE)
        #i = 0
        #while i < 2:
            #print("rank:" + billboard[i].rank)
            #print("language:" + billboard[i].language)
            #print("title:" + billboard[i].title)
            #print("author:" + billboard[i].author)
            #print("album_title:" + billboard[i].album_title)
            #print("artist_name:" + billboard[i].artist_name)
            #i+=1
    except IOError as ioerr:
        print("IOErr:",ioerr)
    return(billboard)
    
def get_billboard(size,type):
    billboard_url = music_url + billboard_url_values %(size, type)
    billboard_res = http_get(billboard_url)
    return billboard_res

def billboard_parse(billboard_str,len):
    #i = 0
    billboard_dict = json.loads(billboard_str)
    billboard_list = []
 
    #try:
        #print(billboard_dict['song_list'][2])
    #except IndexError as indexerr:
        #print("IndexError:",indexerr)
    #print(billboard_dict['song_list'][0])
    try:
        for i in range(len):
            billboard = Billboard()
            billboard.artist_id = billboard_dict['song_list'][i]['artist_id']
            billboard.language = billboard_dict['song_list'][i]['language']
            billboard.pic_big=billboard_dict['song_list'][i]['pic_big']
            billboard.pic_small=billboard_dict['song_list'][i]['pic_small']
            billboard.country=billboard_dict['song_list'][i]['country']
            billboard.publishtime=billboard_dict['song_list'][i]['publishtime']
            billboard.album_no=billboard_dict['song_list'][i]['album_no']
            billboard.lrclink=billboard_dict['song_list'][i]['lrclink']
            billboard.hot=billboard_dict['song_list'][i]['hot']
            billboard.rank_change=billboard_dict['song_list'][i]['rank_change']
            billboard.rank=billboard_dict['song_list'][i]['rank']
            billboard.all_artist_id=billboard_dict['song_list'][i]['all_artist_id']
            billboard.biaoshi=billboard_dict['song_list'][i]['biaoshi']
            billboard.song_id=billboard_dict['song_list'][i]['song_id']
            billboard.title=billboard_dict['song_list'][i]['title']
            billboard.author=billboard_dict['song_list'][i]['author']
            billboard.album_id=billboard_dict['song_list'][i]['album_id']
            billboard.album_title=billboard_dict['song_list'][i]['album_title']
            billboard.artist_name=billboard_dict['song_list'][i]['artist_name']
            billboard_list.append(billboard)
            #i = i + 1
    except IndexError as indexerr:
        print("IndexError:",indexerr)
    #print(billboard_dict['song_list'][0])     
    return (billboard_list)

    
def get_song_info(song_id):
    song_url = GET_SONG_URL_VALUES %(song_id)
    song_info_str = http_get(song_url)
    song_info = song_info_parse(song_info_str[12:-1])
    return song_info

def song_info_parse(song_info_str):
    #print(song_info_str)
    song_dict = json.loads(song_info_str)
    #print(song_dict['data']['songList'][0].keys())
    # try:
    # print(billboard_dict['song_list'][2])
    # except IndexError as indexerr:
    # print("IndexError:",indexerr)
    # print(billboard_dict['song_list'][0])
    try:
        song_info = Song_Info()
        song_info.queryId = song_dict['data']['songList'][0]['queryId']
        song_info.songId = song_dict['data']['songList'][0]['songId']
        song_info.songName = song_dict['data']['songList'][0]['songName']
        song_info.artistId = song_dict['data']['songList'][0]['artistId']
        song_info.artistName = song_dict['data']['songList'][0]['artistName']
        song_info.albumId = song_dict['data']['songList'][0]['albumId']
        song_info.albumName = song_dict['data']['songList'][0]['albumName']
        song_info.songPicSmall = song_dict['data']['songList'][0]['songPicSmall']
        song_info.songPicBig = song_dict['data']['songList'][0]['songPicBig']
        song_info.songPicRadio = song_dict['data']['songList'][0]['songPicRadio']
        song_info.lrcLink = song_dict['data']['songList'][0]['lrcLink']
        song_info.version = song_dict['data']['songList'][0]['version']
        song_info.copyType = song_dict['data']['songList'][0]['copyType']
        song_info.time = song_dict['data']['songList'][0]['time']
        song_info.songLink = song_dict['data']['songList'][0]['songLink']
        song_info.showLink = song_dict['data']['songList'][0]['showLink']
        song_info.rate = song_dict['data']['songList'][0]['rate']
        song_info.size = song_dict['data']['songList'][0]['size']
    except IndexError as indexerr:
        print("IndexError:", indexerr)
    # print(billboard_dict['song_list'][0])
    return (song_info)