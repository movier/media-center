#!/opt/bin/python3
from flup.server.fcgi import WSGIServer
from hello import app

if __name__ == '__main__':
    WSGIServer(app, bindAddress='/tmp/my-video-app-api-fcgi.sock').run()