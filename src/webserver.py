import flaskr
import logging
import logging.config
import os
import sys

def setup_logging(config_path):
    """Setup logging from a fileConfig INI file."""
    if not os.path.isfile(config_path):
        print(f"Error: Logging configuration file not found: {config_path}")
        sys.exit(1)  # Exit or raise an exception

    try:
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        logging.info("Logging configured successfully.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        sys.exit(1)

if __name__ == '__main__':
    config_file = os.path.abspath("/home/asulwer/generator/src/logging.conf")
    setup_logging(config_file)

    logger = logging.getLogger(__name__)
    logging.info("starting webserver")

    app = flaskr.create_app()
    flaskr.socketio.run(app, host='0.0.0.0', port=5000, debug=True)