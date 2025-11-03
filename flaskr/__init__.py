import flask
import flask_socketio
import relays

socketio = flask_socketio.SocketIO()

templateData = {
    'switchPump': False,
    'switchStarter': False,
    'switchACInterupt': False
}

def create_app(test_config=None):
    app = flask.Flask(__name__, instance_relative_config=True)   

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    socketio.init_app(app, async_mode='gevent')

    @app.route('/')
    def index():
        return flask.render_template('index.html', **templateData)

    @socketio.event
    def pumpUpdate(data):
        state = bool(data['switchPump'])

        if state:
            templateData['switchPump'] = True
            relays.pump_on()
        else:
            templateData['switchPump'] = False
            relays.pump_off()

        flask_socketio.emit('pumpUpdate', templateData)

    @socketio.event
    def starterUpdate(data):
        state = bool(data['switchStarter'])

        if state:
            templateData['switchStarter'] = True
            relays.starter_on()
        else:
            templateData['switchStarter'] = False
            relays.starter_off()

        flask_socketio.emit('starterUpdate', templateData)

    @socketio.event
    def aconinteruptUpdate(data):
        state = bool(data['switchACOnInterupt'])

        if state:
            templateData['switchACOnInterupt'] = True
            relays.ac_on_interupt_enable()
        else:
            templateData['switchACOnInterupt'] = False
            relays.ac_on_interupt_disable()

        flask_socketio.emit('aconinteruptUpdate', templateData)

    @socketio.event
    def acoffinteruptUpdate(data):
        state = bool(data['switchACOffInterupt'])

        if state:
            templateData['switchACOffInterupt'] = True
            relays.ac_off_interupt_enable()
        else:
            templateData['switchACOffInterupt'] = False
            relays.ac_off_interupt_disable()

        flask_socketio.emit('acoffinteruptUpdate', templateData)
    
    return app