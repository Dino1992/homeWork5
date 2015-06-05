from pyramid.response import Response


import sys
reload(sys)
sys.setdefaultencoding('utf8')


from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError


@view_config(route_name='my_index', renderer='templates/index.jinja2')
def my_index(request):
    return {'link': u'<a href="about/aboutme.html">AboutMe</a>'}


@view_config(route_name='my_about', renderer='templates/about/aboutme.jinja2')
def my_about(request):
    return {'link': u'<a href="/">Index</a>'}



