from random import random
import cherrypy
import datetime
import random
import json

class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        body = cherrypy.request.body.read()
        request_json = json.loads(body)
        if 'delivery_method' in request_json:
          method = cherrypy.request.json['delivery_method']
        else:
          method = "UPS"

        base_order = {
          "order_number": random.randint(1000,9999),
          "status": "CREATED",
          "created_at": self.rel_date(),
          "delivery_method": method
        }
        return base_order

    def rel_date(self, weeks=0, days=0, hours=0):
      now = datetime.datetime.now() 
      return_date = now - datetime.timedelta(weeks=weeks, days=days, hours=hours)
      return return_date.strftime('%Y-%m-%dT%H:%M:%S.%f')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def order(self, number):
        created = self.rel_date(weeks=-1);
        return {
          "order_number": number,
          "status": "SHIPPED",
          "created_at": created,
          "shipped_at": self.rel_date(days=-4),
          "delivery_method":"UPS",
          "tracking_reference":"1Z001985YW90838348"
        }
cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.thread_pool': 100,
    'server.socket_port': 12345
    })
cherrypy.quickstart(HelloWorld())
