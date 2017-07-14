'''
Created on 2017-6-12

@author: Kaven
'''

# -*- coding: utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8088

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()