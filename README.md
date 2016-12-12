# Process-Monitor
Monitor all your specified process' on the client PC's in your network

# Windows, Linux and Mac


You can monitor running process' of all your clients in your network with Process-Monitor.<br>
The program will sent a HTTP request to the server when a process is started and prints it in the table

![alt tag](https://github.com/raoulbigg/Porcess-Monitor/blob/master/P-M.png)



# Usage

<b>1.)</b> Download git and move it to /var/www/html<br>
<b>2.)</b> Run: sudo chmod -R 777 process-monitor<br>
<b>3.)</b> Update the procmon.py to your servers IP address<br>
<b>4.)</b> Run the procmon.py on all the clients workstations (You might want to compile it with pyinstaller) <br>
<b>5.)</b> Go to: http://server_ip/process-monitor and change your desired process'



# Requirements

Python 2.7<br>
Apache2<br><br>
Modules: <br>
<b>requests<br>
psutil<br>
cgi</b><br>
