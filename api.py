import requests

class MicroMock(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def API(api_base):
    def get(route=''):
        return requests.get(api_base + '/' + route)

    def post(route='', body={}):
        return requests.post(api_base + '/' + route, body)

    def delete(route=''):
        return requests.delete(api_base + '/' + route)

    return MicroMock(get=get, post=post, delete=delete)

base_url = 'http://localhost:3000/'

api_members = API(base_url + 'members')
api_books = API(base_url + 'books')
api_borrows = API(base_url + 'borrows')

