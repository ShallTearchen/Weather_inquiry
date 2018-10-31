#coding:utf-8
import requests
import datetime
import time
import threading

class url_request():
    times = []
    error = []
    def req(self, city):
        myreq=url_request()
        headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
        payload = {'city' : city}
        r = requests.post("http://wthrcdn.etouch.cn/weather_mini",  headers=headers, data=payload)
        ResponseTime = float(r.elapsed.microseconds) / 1000 
        myreq.times.append(ResponseTime) 
        if r.status_code !=200 :
            myreq.error.append("0")
if __name__=='__main__':
    myreq = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "开始时间 %s" %starttime
    nub = 50
    ThinkTime = 0.5
    for i in range(0, nub): 
        t = threading.Thread(target=myreq.req, args=("北京", ))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime) 
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "结束时间： %s" %endtime  
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times))) 
    print "平均响应时间 %s ms" %AverageTime 
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) 
    print "进程并发数： %s" %nub 
    print "共耗时 %s s" %(totaltime-float(nub*ThinkTime)) 
    print "请求错误数量为 %s" %myreq.error.count("0") 
