# coding:utf-8

import os
import json

from apistar import App, Route, http
from get_weather import get_weather


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

def index(app: App, request: http.Request) -> dict:
    return app.render_template("tmp1.html")


def Post(request: http.Request) -> dict:
    print(type(request.body))
    print(request.body)
    query = json.loads(request.body.decode("utf-8"))


    city_name = str(query["city_name"])
    date = str(query["date"])
    
    print(city_name)
    print(date)

    reply = get_weather(city_name, date)
    print(reply)

    return {'result': json.dumps(reply, ensure_ascii=False)}


routes = [
    Route('/', method='POST', handler=Post),
    Route("/index", method="GET", handler=index),
]


app = App(routes=routes, template_dir=TEMPLATE_DIR)


if __name__ == '__main__':
    app.main()
    #app.serve("127.0.0.1", 8000, use_debugger=True)








