'''
Created on 2017-6-13

@author: Kaven
'''
# -*- coding: utf-8 -*-

from template import yate

class Billboard:
    def __init__(self,artist_id,language,pic_big,pic_small,country,publishtime,album_no,lrclink,hot,rank_change,rank\
                 ,all_artist_id,biaoshi,song_id,title,author,album_id,album_title,artist_name):
        self.artist_id=artist_id
        self.language=language
        self.pic_big=pic_big
        self.pic_small=pic_small
        self.country=country
        self.publishtime=publishtime
        self.album_no=album_no
        self.lrclink=lrclink
        self.hot=hot
        self.rank_change=rank_change
        self.rank=rank
        self.all_artist_id=all_artist_id
        self.biaoshi=biaoshi
        self.song_id=song_id
        self.title=title
        self.author=author
        self.album_id=album_id
        self.album_title=album_title
        self.artist_name=artist_name
        
    def __init__(self):
        self.artist_id=0
        self.language=0
        self.pic_big=0
        self.pic_small=0
        self.country=0
        self.publishtime=0
        self.album_no=0
        self.lrclink=0
        self.hot=0
        self.rank_change=0
        self.rank=0
        self.all_artist_id=0
        self.biaoshi=0
        self.song_id=0
        self.title=0
        self.author=0
        self.album_id=0
        self.album_title=0
        self.artist_name=0
        



