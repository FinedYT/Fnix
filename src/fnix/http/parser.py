from .request import Request


class HTTPParser:

    def parse(self, raw_data):
        decoded_data = raw_data.decode("utf-8")
        lines = decoded_data.split("\r\n")
        request_line = lines[0]
        method, path, version = request_line.split(" ")
        headers = {}

        for line in lines[1:]:
            if line == "":
                break

            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

        request = Request(
            method=method,
            path=path,
            version=version
        )
        request.headers = headers

        return request