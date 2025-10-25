from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING' : True}).testing

#def test_index(client):
#    response = client.get('/')
#    assert response.data == b'Index'

#def test_led_on(client):
#    response = client.get('/led/1')
#    assert response.data == b'ON'

#def test_led_off(client):
#    response = client.get('/led/0')
#    assert response.data == b'OFF'

#def test_flashing(client):
#    response = client.get('/flash/5')
#    assert response.data == b'Flashed'