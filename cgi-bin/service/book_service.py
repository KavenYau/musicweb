'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
from model.Book import Book


def get_book_dict():
    book_dict={}
    try:
        with open('book.txt','r') as book_file:
            for each_line in book_file:
                book=parse(each_line)
                book_dict[book.name]=book
    except IOError as ioerr:
        print("IOErr:",ioerr)
    return(book_dict)
    

def parse(book_info):
    (name,author,price)=book_info.split(';')
    book=Book(name,author,price)
    return(book)