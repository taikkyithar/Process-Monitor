import psutil
import requests
import socket
import sys
import time
import datetime


if not (psutil.LINUX or psutil.OSX or psutil.WINDOWS):
    sys.exit("platform not supported")

proc_list = []

r = requests.get("http://YOUR_SERVER_IP/process-monitor/processlist.txt")
for line in r.iter_lines(1024):
    proc_list.append(line)



hostname = socket.gethostname()

def main():
    history = []
    while 1 > 0:
        events = []
        pids = []
        for i in psutil.process_iter():
            for proc in proc_list:
                if proc in i.name():
                    events.append(proc)
                    pids.append(i.pid)

                else:
                    pass


        if len(events) < 1:
            pass
        elif set(history) != set(events):
            now = datetime.datetime.now()
            time_str = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
            events_set = list(set(events))
            payload = {'hostname': hostname, 
                       'process': str(events_set),
                       'time': str(time_str)}

            s = requests.post("http://YOUR_SERVER_IP/process-monitor/process.py", data=payload)
            del history[:]
            history = events
            events = []
            pids = []
            time.sleep(10)
            pass

        else:
            time.sleep(10)
            pass

if __name__ == '__main__':
    main()
