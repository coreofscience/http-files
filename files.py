import falcon


class HealthCheckResource(object):
    def on_get(self, req, res):
        res.body = "pong"


class FilesResource(object):
    def __init__(self, url):
        self.url = url

    def on_get(self, req, res, filename):
        print(filename)
        print("Setting the header on response")
        res.set_header("X-Accel-redirect", "/storage/file.txt")


def app():
    api = falcon.API()
    api.add_route("/ping", HealthCheckResource())
    api.add_route("/file/{filename}", FilesResource("/storage/"))
    return api
