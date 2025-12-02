import logging
import flask
import flask_socketio
import asyncio
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, Button
import json

import relays
import flaskr.dtos

templateData = flaskr.dtos.TemplateData()
socketio = flask_socketio.SocketIO()

def create_app(test_config=None):
    logging.info("create flaskr app")
    app = flask.Flask(__name__)
    
    if test_config is None:
        app.config.from_object('flask_config.ProdConfig')
    else:
        app.config.from_mapping(test_config)

    logging.info("initialize socketio")
    socketio.init_app(app, async_mode='gevent')

    logging.info("initialize relays")
    relays.initialize()

    @app.route('/')
    def index():
        logging.info("index called")
        return flask.render_template('index.html', **templateData.__dict__)

    @socketio.event
    def pumpUpdate(data: json):
        logging.info("pumpUpdate called")
        state = bool(data['switchPump'])

        if state:
            templateData.switchPump = True
            relays.pump(relays.State.ON)
        else:
            templateData.switchPump = False
            relays.pump(relays.State.OFF)

        flask_socketio.emit('pumpUpdate', templateData.__dict__, broadcast=True)

    @socketio.event
    def starterUpdate(data: json):
        logging.info("starterUpdate called")
        state = bool(data['switchStarter'])

        if state:
            templateData.switchStarter = True
            relays.starter(relays.State.ON)
        else:
            templateData.switchStarter = False
            relays.starter(relays.State.OFF)

        flask_socketio.emit('starterUpdate', templateData.__dict__, broadcast=True)

    @socketio.event
    def aconinteruptUpdate(data: json):
        logging.info("aconinteruptUpdate called")
        state = bool(data['switchACOnInterupt'])

        if state:
            templateData.switchACOnInterupt = True
            relays.ac_on_interupt(relays.State.ON)
        else:
            templateData.switchACOnInterupt = False
            relays.ac_on_interupt(relays.State.OFF)

        flask_socketio.emit('aconinteruptUpdate', templateData.__dict__, broadcast=True)

    @socketio.event
    def acoffinteruptUpdate(data: json):
        logging.info("acoffinteruptUpdate called")
        state = bool(data['switchACOffInterupt'])

        if state:
            templateData.switchACOffInterupt = True
            relays.ac_off_interupt(relays.State.ON)
        else:
            templateData.switchACOffInterupt = False
            relays.ac_off_interupt(relays.State.OFF)

        flask_socketio.emit('acoffinteruptUpdate', templateData.__dict__, broadcast=True)
    
    return app