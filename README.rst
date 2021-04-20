==================
pyramid-elasticapm
==================

elastic-apm integration for the Pyramid framework

This package is inspired by https://www.elastic.co/de/blog/creating-custom-framework-integrations-with-the-elastic-apm-python-agent.


Installation
============

Install with pip::

    $ pip install pyramid_elasticapm


Then include it in your pyramid application via config::

    [app:main]
    ...
    pyramid.includes = pyramid_elasticapm

or programmatically in your application::

    config.include('pyramid_elasticapm')


Settings
========


Settings for the elasticapm client can be specified via the `elasticapm`
namespace:

* `elasticapm.server_url`: Specify the apm server url.
* `elasticapm.secret_token`: Your secret authentication token for the server.
* `elasticapm.service_name`: The service name
* `elasticapm.environment`: The environment (e.g. testing, production, …)
* `elasticapm.service_distribution`: The name of the package your are
  deploying. `pyramid_elasticapm` will retrieve the version number of this
  package and put it into the metadata of every transaction.
* `elasticapm.transactions_ignore_patterns`: Whitespace separated list of
  ignore patterns.
