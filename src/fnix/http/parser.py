from .request import request


class HTTPParser:

    def parse(self, raw_data):
        text = raw_data.decode("utf-8")

        first_line = text.split("\r\n")[0]

        method, path, version = first_line.split(" ")

        return request(
            method=method,
            path=path,
            version=version
        )