'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()

import cgi
import service.book_service as book_service
import template.yate as yate

#使用cig.FieldStorage() 访问web请求发送给web服务器的数据，这些数据为一个Python字典
form_data = cgi.FieldStorage()

print("Content-type:text/html\n")
print('<html>')
print('<head>')
print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
print('<title>Book List</title>')
print('</head>')
print('<body>')
print(yate.header('Book Detail:'))
print(form_data)
try:
   book_name = form_data['bookname'].value
   book_dict=book_service.get_book_dict()
   book=book_dict[book_name]
   print(book.get_html)
except KeyError as kerr:
   print(yate.para('please choose a book...'))
print(yate.link("/index.html",'Home'))
print(yate.link("/cgi-bin/book_list_view.py",'Book List'))
print('</body>')
print('</html>')

