import requests
# from IPython import embed


class LocalCallback:
    def call(self, method, url, data={}, headers={}):
        handlers = {
            'post': self.post,
            'get': self.get,
            'put': self.put,
            'delete': self.delete,
            'patch': self.patch,
        }

        resp = handlers[method.lower()](url, data, headers)

        return self.build_result(resp.ok, url=url, method=method)

    def post(self, url, data={}, headers={}):
        return requests.post(url, data=data, headers=headers)

    def get(self, url, data={}, headers={}):
        # isso daqui vai dar problema
        return requests.get(url, data=data, headers=headers)

    def put(self, url, data={}, headers={}):
        return requests.put(url, data=data, headers=headers)

    def delete(self, url, data={}, headers={}):
        return requests.delete(url, data=data, headers=headers)

    def patch(self, url, data={}, headers={}):
        return requests.patch(url, data=data, headers=headers)

    def build_result(self, status, method='DEFAULT', url='DEFAULT'):
        data = {}

        data['ok'] = status
        data['url'] = url
        data['method'] = method
        return data