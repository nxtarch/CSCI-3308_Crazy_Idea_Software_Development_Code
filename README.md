# CSCI-3308_Crazy_Idea_Sofware_Development


Mealbot is a tool for someone looking for a meal. On the homepage it offers a search bar where one can enter in a search for a restaurant or a specific meal and will be matched with corresponding meals or meals of the corresponding restaurant. This is done through our MySQL database and Tornado Server. The meal search also offers a filter option that allows the user to set specific preferences which filters the search results. The user may also see results for a randomized meal if they do not have anything specific in mind. Mealbot also offers a login feature. Where one can sign up, login to an existing account, change their username, change their password, or change the meal preferences. Meal preferences can be set to a specific account in the profile page and the search will automatically apply these. However, the user can also use the filters on the home page for a temporary meal filter. We had also wanted to implement a review page where the user could leave reviews on individual meals they had eaten but were unfortunately unable to implement this in time. 
The difference between our project and existing softwares on the market is we allow more of an ability to customize their eating habits and dietetic contraindications. We also made sure to do this by making it simple and easy for the user to do this through our profile and temporary filter settings.






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
