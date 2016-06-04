from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .db import DBSession, Base
from .database.savers import Savers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    savers = Savers.create()

    config = Configurator(settings=settings)
    config.registry.DBSession = DBSession

    config.add_request_method(
        savers.request_property, 'savers', property=True)

    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('auth', '/authorize')

    config.scan()
    return config.make_wsgi_app()
