
import bs4
import tornado
import mysql.connector as sql
import json
import pandas as pd
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import datetime
import tornado.escape
import decimal
# -*- coding: UTF-8 -*-
class resHomeScreen(RequestHandler):
    def get(self):
        self.render('views/homePage.html')
        print('connected!')
    def post(self):
        search_page = open('views/homePage.html')
        soup = bs4.BeautifulSoup(open('views/homePage.html'), 'html.parser')
        search_page.close()
        dataBase = sql.connect(user='user', password='100acef123',
                               host='127.0.0.1',
                               database='FOODIE',
                               auth_plugin='mysql_native_password')

        input_search = self.get_body_argument("searchBar_input")
        foodie_cursor = dataBase.cursor()
        results_search = foodie_cursor.execute("""
        SELECT * FROM restaurant WHERE restaurant.restaurant like '%{0}%';
        """.format(input_search))
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
        self.render('views/profilePage.html')
def make_app():
    urls = [(r'/homepage', resHomeScreen),
            (r'/search_page/?', resHomeScreen),
            (r'/profilePage', profileInspector)]

    return Application(urls, debug=True)
def main():
    app = make_app()
    app.listen(8000)
    IOLoop.current().start()
if __name__ == '__main__':
    main()