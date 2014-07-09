#!/usr/bin/python

import cgi, cgitb
from jinja2 import Environment, Template, FileSystemLoader

env = Environment(loader=FileSystemLoader('./testapp/templates/'))
template = env.get_template('dashboard.jinja')
print template.render()