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
f = open('processlist.txt' ,'r').readlines()
processL = ''
for p in f:
  processL += p

def index():
    print """Content-type: text/html

<html>
<head>
  <meta charset="UTF-8">
  <title>Process Monitor</title>


  <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'>
  <link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.min.css">
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">


      <link rel="stylesheet" href="css/style.css">


</head>

  <div class="header">

  <div class="logo"> &#160; Process Monitor</div>
</div>
<div class="sidebar">
  <ul>
    <li><a href="index.py"><i class="fa fa-server"></i><span>Process Monitor</span></a></li>
</div>




<!-- Content -->
<div class="main">
  <div class="hipsum">
    <div class="jumbotron">

      <h1 id="hello,-world!">Process Monitor</h1>
      <p>Here you can specifie wich running process' will be monitored of the clients in your network</p>
    </div>

                  <div class="jumbotron">
                        <center>
                        <form action="change.py" method=POST>
                         <textarea rows="4" cols="50" name="processlist">"""+str(processL)+"""
                          </textarea> <br><br>
                            <button type="submit" class="btn btn-primary">Submit</button>
                            <br>
                        </form>
                        </center>

    
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>
    <script src="js/reloader.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>


</body>
</html>

    <html>"""
 
if __name__ == '__main__':
    index()