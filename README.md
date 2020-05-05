# CSCI-3308_Crazy_Idea_Sofware_Development
All the Python libraries required to run our program

  import bs4
  import tornado
  import mysql.connector as sql
  import json
  import pandas as pd
  from tornado.web import Application, RequestHandler
  from tornado.ioloop import IOLoop
  import datetime
  import tornado.escape
  import tornado.httpserver
  import decimal



Heroku wasn't reactive with us so there's a sql dump file called 'foodie.sql' that contains all the data. Create a local instance and adjust the connection setting in the top of tornado_res.py.
To run the program, use python tornado_res.py in command line and the home page runs on localhost:8000/homepage
