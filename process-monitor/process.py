#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cgi
import time
import requests



form = cgi.FieldStorage()
hostname = form.getvalue('hostname')
events = form.getvalue('process')
time_str = form.getvalue('time')

def index():
    print """Content-type: text/html


    <html>"""
    f = open('monitor.txt' , 'w').write(hostname + ":" + events +":"+time_str)


if __name__ == '__main__':
    index()