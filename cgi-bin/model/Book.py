'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
from template import yate

class Book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    
    @property
    def get_html(self):
        html_str=''
        html_str+=yate.header('BookName:',4)+yate.para(self.name)
        html_str+=yate.header('Author:',4)+yate.para(self.author)
        html_str+=yate.header('Price:',4)+yate.para(self.price)
        return(html_str)