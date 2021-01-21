import logging

import curlify
import requests


def format_console(first, second):
    return "{:>7} : {}".format(first, second)


class APIClient(requests.Session):
    base_url: str = ""

    def __init__(self):
        super(APIClient, self).__init__()
        self.hooks["response"].append(self._logging)

    @staticmethod
    def _logging(response: requests.Response, *args, **kwargs):
        """Function to handle logging in hook['response'] """
        logging.info("----------- Request ----------->")
        logging.info(format_console(response.request.method, response.request.url))
        logging.info(format_console("HEADERS", response.request.headers))
        logging.info(format_console("DEBUG", curlify.to_curl(response.request)))
        # print(format_console("DEBUG", curlify.to_curl(response.request)))
        if response.request.body is not None:
            logging.info(format_console("BODY", response.request.body))

        logging.info("<----------- Response -----------")
        logging.info(
            format_console(
                "STATUS",
                f"{response.status_code}, elapsed: {response.elapsed.total_seconds()}s",
            )
        )
        logging.info(format_console("HEADER", response.headers))
        if response.text != "":
            logging.info(format_console("BODY", response.text))
            # print(format_console("BODY", response.text))
