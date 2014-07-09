#!/usr/bin/python

from jinja2 import Environment, Template, FileSystemLoader

env = Environment(loader=FileSystemLoader('./testapp/templates/'))
template = env.get_template('home.jinja')
print template.render()