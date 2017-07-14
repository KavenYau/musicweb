'''
Created on 2017-6-12

@author: Kaven
'''
# -*- coding: utf-8 -*-
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')
def para(para_text):
    return('<p>' + para_text + '</p>') 

def link(the_link,value):
    link_string = '<a href="' + the_link + '">' + value + '</a>'
    return(link_string)

def table_start(border, cellpadding, cellspacing):
    table_string = '<table border="%d" cellpadding="%d" cellspacing="%d" >' % (border,cellpadding,cellspacing)
    return(table_string)
    
def table_end():
    table_string = '</table>'
    return(table_string)
    
def table_tr_start():
    table_tr = '<tr>'
    return(table_tr)
    
def table_tr_end():
    table_tr = '</tr>'
    return(table_tr)
  
def table_th(str):    
    table_th_string = '<th>' + str + '</th>'
    return(table_th_string)

def table_td(str):    
    table_td_string = '<td>' + str + '</td>'
    return(table_td_string)
    