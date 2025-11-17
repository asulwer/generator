import flaskr
import logging
import logger_setup

if __name__ == '__main__':
    logger_setup.setup("/home/asulwer/generator/src/webserver.conf")
    logging.info("starting webserver")

    app = flaskr.create_app()
    flaskr.socketio.run(app, host='0.0.0.0', port=5000, debug=True)