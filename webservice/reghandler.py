#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

username = form.getvalue("username")
email = form.getvalue("email")
password = form.getvalue("password")

result = "ok"

###### add user to database

link = "reg.py?result=" + result
print "Location: " + link
print
print "<a href=\""+link+"\">If not redirecting click here</a>"