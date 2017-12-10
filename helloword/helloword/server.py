import sys
import os
from tornado.options import options, define, parse_command_line
from multiprocessing import Pool
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from django.core.wsgi import get_wsgi_application
define('port', type=int, default=8000)
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado:%s'%os.getpid())
def run(port):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    parse_command_line()
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)

    tornado_app = tornado.web.Application(
        [
            ('/', HelloHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ])

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(run,[8000,8001,8002,8003])