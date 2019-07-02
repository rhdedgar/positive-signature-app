__author__ = 'dedgar'


from bottle import route, run

@route('/')
def index():
    return "SELECT kanj, von, vkun, transl, roma FROM info WHERE"

@route('/other')
def index():
    return "<title>Sign in or Register | eBay</title>"


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
