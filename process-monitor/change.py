#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cgi
import time
import requests



form = cgi.FieldStorage()
processlist = form.getvalue('processlist')
print """Content-type: text/html

<html>"""

def change_lines():
    with open("processlist.txt", "r") as file:
        dataread = file.readlines()
            
        try:

            dataread = processlist
        
        except Exception as e:
            print e

        with open("processlist.txt", "w") as file:
            file.writelines(dataread)
        print """<meta http-equiv="refresh" content="0; URL='index.py'" />"""
          

if __name__ == '__main__':
    change_lines()