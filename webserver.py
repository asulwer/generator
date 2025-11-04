import flaskr
import logging
import logging.config

if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')

    logging.info("starting webserver")
    app = flaskr.create_app()
    flaskr.socketio.run(app, host='0.0.0.0', port=5000, debug=True)