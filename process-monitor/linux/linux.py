#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cgi
import time
import requests



form = cgi.FieldStorage()


def index():
    print """Content-type: text/html

<html>
<head>
  <meta charset="UTF-8">
  <title>Process Monitor</title>


  <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'>
  <link rel="stylesheet" href="../font-awesome-4.7.0/css/font-awesome.min.css">
  <link href="/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">


      <link rel="stylesheet" href="../css/style.css">


</head>

  <div class="header">

  <div class="logo"> &#160; Process Monitor</div>
</div>
<div class="sidebar">
  <ul>
    <li><a href="../index.py"><i class="fa fa-desktop"></i><span>Process Monitor</span></a></li>
    <li><a href="../windows/windows.py"><i class="fa fa-windows"></i><span>Windows process list</span></a></li>
    <li><a href="linux.py"><i class="fa fa-linux"></i><span>Linux process list</span></a></li>
</div>



<!-- Content -->
<div class="main">
  <div class="hipsum">
    <div class="jumbotron">

      <h1 id="hello,-world!">Process Monitor</h1>
      <p>Here you can see some examples of the process' in Linux</p>


    </div>

    <table class="table" style="border-collapse:separate">
      <thead>
        <tr>
          <th>Name</th>
          <th>Process name</th>
        </tr>
          <tr><td>Python</td>
          <td>python</td></tr>

          <tr><td>Apache2</td>
          <td>apache2</td></tr>

          <tr><td>Skype</td>
          <td>skype</td></tr>

          <tr><td>FireFox</td>
          <td>firefox</td><tr>

          <tr><td>Google Chrome</td>
          <td>Chrome</td><tr>

          <tr><td>Gnome terrminal</td>
          <td>gnome-terrminal</td></tr>

          <tr><td>Gedit</td>
          <td>gedit</td></tr>

          <tr><td>Teamviewer</td>
          <td>teamviewerd</td></tr>  

      </thead>

      

    
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="../js/index.js"></script>
    <script src="../js/reloader.js"></script>
    <script src="../vendor/bootstrap/js/bootstrap.min.js"></script>
    

</body>
</html>

    <html>"""



if __name__ == '__main__':
    index()
