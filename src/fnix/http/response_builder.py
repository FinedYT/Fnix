class ResponseBuilder:
    def build(self, response):
        status_line = (
            f"HTTP/1.1 {response.status_code} {response.status_text}\n"
        )

        headers = ""

        for content_type, server in response.headers.items():
            headers += f"{content_type}: {server}\r\n"

        full_response = (
            status_line +
            headers +
            "\r\n" +
            response.body
        )

        return full_response