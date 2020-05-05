
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
# -*- coding: UTF-8 -*-
import os
import psycopg2

#SQL DUMP IS IN FOODIE.sql
#CHANGE TO LOCAL DB WHEN DEPLOYING
conn = sql.connect(user='user', password='100acef123',
                               host='127.0.0.1',
                               database='FOODIE',
                               auth_plugin='mysql_native_password')

curr_user = "user"
user_pref = '{}'

class resHomeScreen(RequestHandler):
    def get(self):
        global curr_user

        if curr_user != "user":
            disable_button_soup = bs4.BeautifulSoup(open('views/homePage.html'), 'html.parser')
            sign_up_modal = disable_button_soup.find('div',{'id' : 'divSignUP'})
            login_modal = disable_button_soup.find('div',{'id':'divLogin'})
            sign_up_modal.attrs['style'] = 'display: none;'
            login_modal.attrs['style'] = 'display: none;'
            with open('views/homePagedisabled.html', 'w') as nb:
                nb.write(str(disable_button_soup.prettify(formatter='html')).rstrip())
            self.render('views/homePagedisabled.html')
        else:
            self.render('views/homePage.html')
        print('connected!')
    def post(self):
        search_page = open('views/homePage.html')
        soup = bs4.BeautifulSoup(open('views/homePage.html'), 'html.parser')
        search_page.close()
        global curr_user

        if curr_user != "":
            disable_button_soup = bs4.BeautifulSoup(open('views/homePage.html'), 'html.parser')
            sign_up_modal = disable_button_soup.find('div', {'id': 'signUP'})
            login_modal = disable_button_soup.find('a', {'id': 'logIN'})
            print(sign_up_modal)
            login_modal.append('disabled')
            with open('views/homePagedisabled.html', 'w') as nb:
                nb.write(str(disable_button_soup.prettify(formatter='html')).rstrip())

        dataBase = conn
        #dataBase = sql.connect(user='user', password='100acef123',
                              # host='127.0.0.1',
                            #  database='FOODIE',
                             #  auth_plugin='mysql_native_password')

        input_search = self.get_body_argument("searchBar_input")

        food_allergies_all = ['Dairy', 'Peanuts', 'Soy']
        on_input = []
        dairy_allergy = ['','']
        peanut_allergy = ''
        soy_allergy = ''
        type_of_food = []
        max_price = '$100'
        for x in self.request.arguments:
            if x == 'Dairy':
                dairy_allergy = ['cheese', 'milk']
            elif x == 'Peanuts':
                peanut_allergy = 'peanuts'
            elif x == 'Soy':
                soy_allergy = 'soy'
            elif x == 'maxPrice':
                max_price = self.get_argument(x)
            elif x != 'searchBar_input':
                type_of_food.append(x)
        foodie_cursor = dataBase.cursor()
        string_execute = """
        SELECT * FROM Restaurant WHERE restaurant.restaurant like '%{0}%' OR dish like '%{0}%' or description_ing like 
        '%{0}%' AND description_ing NOT LIKE '%{1}%' AND description_ing NOT LIKE '%{2}%' AND description_ing NOT LIKE '%{3}%'
        AND description_ing NOT LIKE '%{4}%' AND price <= '{5}'
        """.format(input_search, dairy_allergy[0], dairy_allergy[1], peanut_allergy, soy_allergy, max_price)
        if len(type_of_food) != 0:
            for index, c in enumerate(type_of_food):
                if index != len(type_of_food) - 1:
                    add_string = "OR type_food = '%{0}%'".format(c)
                else:
                    add_string = "AND type_food = '%{0}%' LIMIT 40;".format(c)
                string_execute += add_string
        else:
            string_execute += 'LIMIT 40;'
        print(string_execute)
        results_search = foodie_cursor.execute(string_execute)
        div_tag = soup.find('div', {'id': 'cardResult'})

        for index, x in enumerate(foodie_cursor.fetchall()):
            if index == 0 and (index % 5) == 0:
                card_row = soup.new_tag('div', attrs={'class' : 'row'})

            col_tag = soup.new_tag('div', attrs={'class': 'column'})
            dish_string = x[2].rstrip('\n')
            card_tag = soup.new_tag('div', attrs={'class' : 'card'})
            heading_tag = soup.new_tag('h3')
            heading_tag.string = dish_string
            p_tag = soup.new_tag('p')
            p_tag.string = 'Restaurant: {0}'.format(x[1].strip())
            p_tag2 = soup.new_tag('p')
            p_tag2.string = 'Description: {0}'.format(x[3].strip())
            p_tag3 = soup.new_tag('p')
            p_tag3.string = 'Price: {0}'.format(x[4].strip())
            card_tag.append(heading_tag)
            card_tag.append(p_tag)
            card_tag.append(p_tag2)
            card_tag.append(p_tag3)
            card_tag['style'] = "margin: 20px;background-color: lightblue;width: 300px;border: 15px;padding: 50px;"
            col_tag.append(card_tag)
            card_row.append(col_tag)
            if (index % 4) == 0:
                div_tag.append(card_row)


        with open('views/test_search_page2.html', 'w') as test_html:
            test_html.write(str(soup.prettify(formatter='html')).rstrip())
        try:
            self.render('views/test_search_page2.html')
        except UnicodeDecodeError:
            print('error at render')
        #card_result.p = 'test'
        #self.write(foodie_cursor.fetchall())
class profileInspector(RequestHandler):
    def get(self):
        print(self.request.arguments)
        self.render('views/profilePage.html')
    def post(self):
        global curr_user
        global user_pref

        dataBase_db = conn
        user_arguments = self.request.arguments
        first_name = ''
        last_name = ''
        password_1 = ''
        user_login = dataBase_db.cursor()
        if len(user_arguments) > 2:
            for i in user_arguments:
                if i == 'username':
                    temp_string = user_arguments[i]
                    print(str(temp_string[0].decode('utf-8')))
                    curr_user = str(temp_string[0].decode('utf-8'))
                elif i == 'firstName':
                    temp_string1 = user_arguments[i]
                    first_name = str(temp_string1[0].decode('utf-8'))
                elif i == 'lastName':
                    temp_string2 = user_arguments[i]
                    last_name = str(temp_string2[0].decode('utf-8'))
                elif i == 'password':
                    temp_string3 = user_arguments[i]
                    password_1 = str(temp_string3[0].decode('utf-8'))
            insert_string = """
                       INSERT INTO userlogin
                       VALUES
                       ('{0}','{1}','{2}','{3}','{4}')

                       """.format(curr_user, first_name, last_name, password_1, user_pref)
            user_login.execute(insert_string)
            dataBase_db.commit()
        else:
            for c in user_arguments:
                if c == 'userName':
                    temp_string = user_arguments[c]
                    print(str(temp_string[0].decode('utf-8')))
                    temp_user = str(temp_string[0].decode('utf-8'))
                elif c == 'password':
                    temp_string3 = user_arguments[c]
                    password_1 = str(temp_string3[0].decode('utf-8'))

            check_username_string = """
            SELECT * FROM userlogin
            WHERE username like '%{0}%' AND pword = '{1}';
        
            """.format(temp_user, password_1)
            user_login.execute(check_username_string)
            data = user_login.fetchall()
            if len(data) != 0:
                curr_user = temp_user
                user_pref = data[0][-1]
        self.render('views/profilePage.html')
class reviewMeal(RequestHandler):
    def get(self):
        self.render('views/reviewPage_new.html')
    def post(self):
        print('connected!')
        review_page = open('views/reviewPage_new.html')
        new_soup = bs4.BeautifulSoup(review_page, 'html.parser')
        review_page.close()
        dataBase = conn
        input_res = self.get_body_argument('inputRes')
        input_dish = self.get_body_argument('inputDish')

        review_cursor = dataBase.cursor()
        results = review_cursor.execute("""
        SELECT * FROM Restaurant where restaurant like '%{0}%' AND dish like '%{1}%' LIMIT 1;
        """.format(input_res, input_dish))
        data_array = review_cursor.fetchall()
        info_dish_tag = new_soup.find('label', {'id': 'dishName'})
        info_price_tag = new_soup.find('label', {'id':'priceName'})
        info_desc_tag = new_soup.find('label', {'id':'descriptionName'})
        info_price_tag.string = data_array[0][-1]
        info_dish_tag.string = data_array[0][2]
        info_desc_tag.string = data_array[0][3]
        with open('views/reviewPage_new_results.html', 'w') as results_html:
            results_html.write(str(new_soup.prettify(formatter='html')))
        try:
            self.render('views/reviewPage_new_results.html')
        except UnicodeDecodeError:
            print('error at render')
class randomMeal(RequestHandler):
    def post(self):
        print('in the random meal website')
        search_page = open('views/homePage.html')
        result_soup = bs4.BeautifulSoup(search_page, 'html.parser')
        dataBase_NEW = conn
        random_cursor = dataBase_NEW.cursor()
        string_execute = "SELECT * FROM Restaurant where rand() <= .3 limit 1;"
        random_cursor.execute(string_execute)
        div_tag = result_soup.find('div', {'id': 'cardResult'})
        for index, x in enumerate(random_cursor.fetchall()):
            if index == 0 and (index % 5) == 0:
                card_row = result_soup.new_tag('div', attrs={'class' : 'row'})

            col_tag = result_soup.new_tag('div', attrs={'class': 'column'})
            dish_string = x[2].rstrip('\n')
            card_tag = result_soup.new_tag('div', attrs={'class' : 'card'})
            heading_tag = result_soup.new_tag('h3')
            heading_tag.string = dish_string
            p_tag = result_soup.new_tag('p')
            p_tag.string = 'Restaurant: {0}'.format(x[1].strip())
            p_tag2 = result_soup.new_tag('p')
            p_tag2.string = 'Description: {0}'.format(x[3].strip())
            p_tag3 = result_soup.new_tag('p')
            p_tag3.string = 'Price: {0}'.format(x[4].strip())
            card_tag.append(heading_tag)
            card_tag.append(p_tag)
            card_tag.append(p_tag2)
            card_tag.append(p_tag3)
            card_tag['style'] = "margin: 20px;background-color: lightblue;width: 300px;border: 15px;padding: 50px;"
            col_tag.append(card_tag)
            card_row.append(col_tag)
            if (index % 4) == 0:
                div_tag.append(card_row)
        with open('views/random_result.html', 'w') as test_html:
            test_html.write(str(result_soup.prettify(formatter='html')).rstrip())
        try:
            self.render('views/random_result.html')
        except UnicodeDecodeError:
            print('error at render')

class profileChanges(RequestHandler):
    def prepare(self):
        print(self.request.arguments)
    def get(self):
        self.render('views/profilePage.html')
    def post(self):
        global curr_user
        global user_pref
        database = conn
        change_arguments = self.request.body_arguments
        change_cursor = database.cursor()
        if 'userName1' in change_arguments:
            current_user = curr_user

            temp_user = str(change_arguments['userName1'][0].decode('utf-8'))
            string_execute = """
            UPDATE userlogin
            SET
                username = '{0}'
            WHERE
                username = '{1}';
            
            """.format(temp_user,current_user)
            change_cursor.execute(string_execute)
            database.commit()
            curr_user = temp_user
        if 'password1' in change_arguments:
            org_pass = str(change_arguments['password'][0].decode('utf-8'))
            new_pass = str(change_arguments['password1'][0].decode('utf-8'))
            string_pass_execute = """
            UPDATE userlogin
            SET
                pword = '{0}'
            WHERE
                pword = '{1}'
                AND
                username = '{2}'
                ;
            
            """.format(new_pass,org_pass,curr_user)
            change_cursor.execute(string_pass_execute)
            database.commit()
        temp_preferences = {"Allergies": [], "Types":[]}
        for x in change_arguments:
            if x == 'dairyBox':
                temp_preferences["Allergies"].append('milk')
                temp_preferences["Allergies"].append('cheese')
            elif x == 'nutsBox':
                temp_preferences["Allergies"].append('peanuts')
            elif x == 'soyBox':
                temp_preferences["Allergies"].append('soy')
            elif x != 'password1' and x != 'userName1' and x != 'password2' and x != 'password':
                temp_preferences["Types"].append(x)
        user_pref = str(temp_preferences)
        change_cursor.execute("""
        UPDATE userlogin
        SET prefs = "{0}"
        WHERE
            username = '{1}'
            ;
        """.format(user_pref,curr_user))
        database.commit()
        self.render('views/profilePage.html')
def make_app():
    urls = [(r'/homepage', resHomeScreen),
            (r'/homepage/randomMeal', randomMeal),
            (r'/profilePage', profileInspector),
            (r'/reviewPage', reviewMeal),
            (r'/reviewPage/results', reviewMeal),
            (r'/profilePagechanges', profileChanges),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': './resources/img/'}),
            (r'/static/stylesheet/(.*)', tornado.web.StaticFileHandler, {'path': './resources/css/'}),
            (r'/js/(.*)',tornado.web.StaticFileHandler, {'path': './resources/js/'}),
            ]

    return Application(urls, debug=True)
def main():
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(8000)
    IOLoop.current().start()
if __name__ == '__main__':
    main()