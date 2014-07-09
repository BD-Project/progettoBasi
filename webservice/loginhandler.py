#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

result = "ok"

###### search database and set cookie

if result=="ok":
	link = "dashboard.py"
else:
	link = "login.py?result="+result
print "Location: " + link
print
print "<a href=\""+link+"\">If not redirecting click here</a>"