from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',        ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                     )
    @app.route('/deploy/',    	['OPTIONS', 'POST'],        lambda x = None: call([deploy])   )
    def base():
        return
