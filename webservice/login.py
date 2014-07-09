#!/usr/bin/python

import cgi, cgitb
from jinja2 import Environment, Template, FileSystemLoader

get = cgi.FieldStorage()

r = get.getvalue("result")

env = Environment(loader=FileSystemLoader('./testapp/templates/'))
template = env.get_template('login.jinja')
print template.render(result=r)