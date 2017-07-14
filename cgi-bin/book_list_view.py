'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()


import template.yate as yate
import service.book_service as book_service


print('<html>')
print('<head>')
print('<title>Book List</title>')
print('</head>')
print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
print('<body>')
print('<h2>Book List:</h2>')
print(yate.start_form('book_detail_view.py'))
book_dict=book_service.get_book_dict()
for book_name in book_dict:
    print(yate.radio_button('bookname',book_dict[book_name].name))
print(yate.end_form('detail'))
print(yate.link("/index.html",'Home'))
print('</body>')
print('</html>')