import socket
import time

import pytest
from pytest_localserver.http import ContentServer


@pytest.fixture()
def apmserver(request):
    config = getattr(request, 'param', {})
    server = ContentServer(**config)
    server.start()
    wait_for_http_server(server)

    yield server

    server.stop()


def wait_for_http_server(httpserver, timeout=30):
    start_time = time.time()
    while True:
        try:
            sock = socket.create_connection(
                httpserver.server_address, timeout=0.1
            )
            sock.close()
            break
        except socket.error:
            if time.time() - start_time > timeout:
                raise TimeoutError()
