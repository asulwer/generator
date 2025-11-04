import flaskr

if __name__ == '__main__':
    app = flaskr.create_app()
    flaskr.socketio.run(app, host='0.0.0.0', port=5000, debug=True)