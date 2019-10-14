class DkubeAPIException(Exception):
    def __init__(self, method, url, code):
        msg = "API {} -> {} failed with code {}".format(method, url, code)
        Exception.__init__(self, msg)
