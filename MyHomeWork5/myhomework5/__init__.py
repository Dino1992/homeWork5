from pyramid.config import Configurator
from sqlalchemy import engine_from_config



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('my_index', '/')
    config.add_route('my_about', '/about/aboutme.html')
    config.scan()
    return config.make_wsgi_app()
