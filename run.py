# from werkzeug.wsgi import DispatcherMiddleware

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from flask_server import server
from test import app as test_app


application = DispatcherMiddleware(server, {
    '/test': test_app.server
})




if __name__ == '__main__':
	run_simple('0.0.0.0', 8050, application, use_reloader=True, use_debugger=True)

