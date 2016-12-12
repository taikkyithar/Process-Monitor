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

<html>
<head>
  <meta charset="UTF-8">
  <title>Admin Menu</title>


  <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'>
  <link rel="stylesheet" href="font-awesome-4.7.0/css/font-awesome.min.css">


      <link rel="stylesheet" href="css/style.css">


</head>

  <div class="header">
  <a href="#" id="menu-action">
    <i class="fa fa-bars"></i>
    <span>Close</span>
  </a>
  <div class="logo">
    Process Monitor
  </div>
</div>
<div class="sidebar">
  <ul>
    <li><a class="sidebar_cur" href="index.html"><i class="fa fa-desktop"></i><span>Dashboard</span></a></li>
    <li><a href="process.py"><i class="fa fa-server"></i><span>Process Monitor</span></a></li>
    <li><a href="index.html"><i class="fa fa-sign-out"></i><span>logout</span></a></li>
</div>

<!-- Content -->
<div class="main">
  <div class="hipsum">
    <div class="jumbotron">
      <h1 id="hello,-world!">Process Monitor</h1>
      <p>Here you can monitor, analyse and specifie the current running process' of the clients in your network</p>
    </div>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Host</th>
          <th>Process'</th>
          <th>Last update</th>
        </tr>
      </thead>
      

    
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>
    <script src="js/reloader.js"></script>
<meta http-equiv="refresh" content="5" />
</body>
</html>

    <html>"""
    READ = open('monitor.txt' , 'r').readlines()
    for i in READ:
      print """<body>"""
      print "<tr><td><b>"+i.split(":")[0]+"</b></td>"
      print "<td>"+i.split(":")[1].strip('[]').replace("'", '')+"</td>"
      print "<td>"+i.split(":")[2].strip(",()")+"</td><tr></table>"


if __name__ == '__main__':
    index()