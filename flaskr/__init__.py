import flask
import flask_socketio
import smbus2

DEVICE_ADDR = 0x01
CHIP_ADDR = 0x10
PUMP_ADDR = 0x01
STARTER_ADDR = 0x02
ACINTERUPT_ON_ADDR = 0x03
ACINTERUPT_OFF_ADDR = 0x04
ON = 0xFF
OFF = 0x00

bus = smbus2.SMBus(DEVICE_ADDR)
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

    bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, OFF)
    bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, OFF)
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, OFF)
    bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, OFF)

    @app.route('/')
    def index():
        return flask.render_template('index.html', **templateData)

    @socketio.event
    def pumpUpdate(data):
        state = bool(data['switchPump'])

        if state:
            templateData['switchPump'] = True
            bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, ON)
        else:
            templateData['switchPump'] = False
            bus.write_byte_data(CHIP_ADDR, PUMP_ADDR, OFF)

        flask_socketio.emit('pumpUpdate', templateData)

    @socketio.event
    def starterUpdate(data):
        state = bool(data['switchStarter'])

        if state:
            templateData['switchStarter'] = True
            bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, ON)
        else:
            templateData['switchStarter'] = False
            bus.write_byte_data(CHIP_ADDR, STARTER_ADDR, OFF)

        flask_socketio.emit('starterUpdate', templateData)

    @socketio.event
    def aconinteruptUpdate(data):
        state = bool(data['switchACOnInterupt'])

        if state:
            templateData['switchACOnInterupt'] = True
            bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, ON)
        else:
            templateData['switchACOnInterupt'] = False
            bus.write_byte_data(CHIP_ADDR, ACINTERUPT_ON_ADDR, OFF)

        flask_socketio.emit('aconinteruptUpdate', templateData)

    @socketio.event
    def acoffinteruptUpdate(data):
        state = bool(data['switchACOffInterupt'])

        if state:
            templateData['switchACOffInterupt'] = True
            bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, ON)
        else:
            templateData['switchACOffInterupt'] = False
            bus.write_byte_data(CHIP_ADDR, ACINTERUPT_OFF_ADDR, OFF)

        flask_socketio.emit('acoffinteruptUpdate', templateData)
    
    return app