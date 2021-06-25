# from werkzeug.wsgi import DispatcherMiddleware

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from flask_server import server
from test import app as test_app

application = DispatcherMiddleware(server, {
    # '/dash1': da_farmer_app.server,
    '/test': testapp
})

