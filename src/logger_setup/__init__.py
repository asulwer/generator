import logging
import logging.config
import os
import sys

def setup(config_path):
    if not os.path.isfile(config_path):
        print(f"Error: Logging configuration file not found: {config_path}")
        sys.exit(1)

    try:
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        logging.info("Logging configured successfully.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        sys.exit(1)