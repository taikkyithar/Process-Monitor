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
    <li><a href="index.py"><i class="fa fa-desktop"></i><span>Process Monitor</span></a></li>
    <li><a href="windows/windows.py"><i class="fa fa-windows"></i><span>Windows process list</span></a></li>
    <li><a href="linux/linux.py"><i class="fa fa-linux"></i><span>Linux process list</span></a></li>
</div>


<!-- Content -->
<div class="main">
  <div class="hipsum">
    <div class="jumbotron">

      <h1 id="hello,-world!">Process Monitor</h1>
      <p>Here you can monitor and analyse the current running process' of the clients in your network</p>

      <a href="processchange.py"><button class="btn btn-primary">Process list</button></a>


    </div>

            



    <table class="table" style="border-collapse:separate">
      <thead>
        <tr>
          <th>Host</th>
          <th>Running process'</th>
          <th>Last update</th>
        </tr>
      </thead>
      

    
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>
    <script src="js/reloader.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
    
    <meta http-equiv="Refresh" content="10">


</body>
</html>

    <html>"""
    READ = open('monitor.txt' , 'r').readlines()
    for i in READ:
      time_print = i.split(":")[2] +":"+ i.split(":")[3] +":"+ i.split(":")[4]
      print """<body>"""
      print "<tr><td><b>"+i.split(":")[0]+"</b></td>"
      print "<td>"+i.split(":")[1].strip('[]').replace("'", '')+"</td>"
      print "<td>"+time_print+"</td><tr>"


if __name__ == '__main__':
    index()
