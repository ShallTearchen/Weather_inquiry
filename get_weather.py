#!/usr/bin/env python
# coding=utf-8


import requests
import json
import datetime
import re

def get_weather(city_name, time):
    url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city_name

    response = requests.get(url)

    json_obj = response.content.decode()

    #print(json_obj)

    info = json.loads(json_obj, strict=False)

    #print(info)

    data = info["data"]
    #print(data)

    '''
    for (k, v) in data.items():
        print("%s : %s\n" % (k, v))
    '''

    time_dict = {"昨天" : -1, "今天" : 0, "明天" : 1, "后天" : 2, "大后天" : 3, "大大后天" : 4}

    now_time = datetime.datetime.now()

    timedelta = now_time + datetime.timedelta(days=time_dict[time])

    specified_date = timedelta.strftime("%Y-%m-%d")

    #print(specified_date)   #打印要查询的日期

    #print(city_name)    #打印要查询的地点

    if time == "昨天":
        weather_data = data["yesterday"]
        wind_power = weather_data["fl"]         #风向
        wind_direction = weather_data["fx"]     #风力
    else:
        weather_data = data['forecast'][time_dict[time]]
        wind_power = weather_data['fengli']
        wind_direction = weather_data['fengxiang']
    
    lowest_t = weather_data['low']              #最低温度
    highest_t = weather_data['high']            #最高温度
    weather = weather_data['type']              #天气情况
    
    match_obj = re.search("[\d-]+级", wind_power)
    wind_power = match_obj.group()

    reply = {'city_name' : city_name, 'specified_date' : specified_date, 'lowest_t' : lowest_t, 'highest_t' : highest_t, 'weather' : weather, 'wind_power' : wind_power, 'wind_direction' : wind_direction}
    #print(reply)

    return reply

if __name__ == "__main__":
    get_weather("北京","今天")





