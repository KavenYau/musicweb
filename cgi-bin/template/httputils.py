'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
import urllib  
import urllib.request  

def http_get(url):
    
   
    
    res=urllib.request.urlopen(url).read()  
    res=res.decode('UTF-8')  
    return(res)  

def setParaAndContext(type):
    msgSendtoClient="Content-Type: "+type+";charset=utf-8"
    return msgSendtoClient
