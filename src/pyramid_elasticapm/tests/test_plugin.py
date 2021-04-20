import time

from pyramid.config import Configurator
from webtest import TestApp


def make_app(server_url):
    settings = {
        'elasticapm.service_name': 'pyramid-test-app',
        'elasticapm.server_url': server_url,
        'elasticapm.secret_token': '<MY_SECRET_TOKEN>',
        'elasticapm.environment': 'testing',
        'elasticapm.service_distribution': 'pytest',
        'elasticapm.transactions_ignore_patterns': 'foo bar baz',
    }
    config = Configurator(settings=settings)
    config.include('pyramid_elasticapm')

    config.add_route('index', '/')
    config.add_view(
        lambda x: {'status': 'ok'}, route_name='index', renderer='json'
    )

    return config.make_wsgi_app()


def test_foo(apmserver):
    assert [] == apmserver.requests

    app = TestApp(make_app(apmserver.url))

    resp = app.get('/')
    resp.mustcontain(b'{"status": "ok"}')

    # Give the apm integration some time to send requests to the apm server
    time.sleep(1)

    requests = apmserver.requests
    assert len(requests) != 0

    assert 'Bearer <MY_SECRET_TOKEN>' == requests[0].headers['Authorization']
