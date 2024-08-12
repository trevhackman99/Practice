from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import pandas as pd
import numpy as np

def get_bbref_splits(game_data):
    for game in game_data:
        game_name = game['away_team'] + ' at ' + game['home_team']    

        away_pitcher_id = game['away_pitcher_id']
        home_pitcher_id = game['home_pitcher_id']

        away24_url = f'https://www.baseball-reference.com/players/split.fcgi?id={away_pitcher_id}&year=2024&t=p'
        home24_url = f'https://www.baseball-reference.com/players/split.fcgi?id={home_pitcher_id}&year=2024&t=p'

        session = HTMLSession()

        html_page = session.get(away24_url)
        html_page2 = session.get(home24_url)

        html_page.html.render(sleep=4)

        soup = bs(html_page.html.html, 'html.parser')

        a_platoon_table = soup.find('table', {'id': 'plato'})
        a_times_table = soup.find('table', {'id': 'times'})
        a_dr_table = soup.find('table', {'id': 'dr'})
        a_stad_table = soup.find('table', {'id': 'stad'})
        a_catch_table = soup.find('table', {'id': 'catch'})

        # Extract HTML content of the tables
        away_tables_html = [str(table) for table in [a_platoon_table, a_times_table, a_dr_table, a_stad_table, a_catch_table]]

        html_page2.html.render(sleep=4)

        soup2 = bs(html_page2.html.html, 'html.parser')

        h_platoon_table = soup2.find('table', {'id': 'plato'})
        h_times_table = soup2.find('table', {'id': 'times'})
        h_dr_table = soup2.find('table', {'id': 'dr'})
        h_stad_table = soup2.find('table', {'id': 'stad'})
        h_catch_table = soup2.find('table', {'id': 'catch'})

        # Extract HTML content of the tables
        home_tables_html = [str(table) for table in [h_platoon_table, h_times_table, h_dr_table, h_stad_table, h_catch_table]]

        # Create and write to an HTML file
        with open(f'tables{game_name}.html', 'w') as file:
            file.write('<html><head><title>Baseball Tables</title></head><body>')
            for table_html in away_tables_html:
                file.write(table_html)

            for table_html in home_tables_html:
                file.write(table_html)
            file.write('</body></html>')

        print(f'HTML {game_name} file created with tables.')
        

def get_bbref_previews():
    url = 'https://www.baseball-reference.com/previews/'
    response = requests.get(url)
    data = bs(response.text, 'html.parser')
    
    games = data.find_all('div', {'class': 'game_summary nohover'})

    game_data = []

    if games:
        for games in games:
            try:

                table = games.find_all('table')[1]
                rows = table.find_all('tr')
                away_team = rows[0].find_all('td')[0].text
                home_team = rows[1].find_all('td')[0].text
                away_pitcher = rows[0].find_all('td')[1].find('a').text
                home_pitcher = rows[1].find_all('td')[1].find('a').text
                away_pitcher_bbref = rows[0].find_all('td')[1].find('a')['href']
                home_pitcher_bbref = rows[1].find_all('td')[1].find('a')['href']

                away_pitcher_id = away_pitcher_bbref.split('/')[-1].split('.')[0]
                home_pitcher_id = home_pitcher_bbref.split('/')[-1].split('.')[0]

                game_info = {
                    'away_team': away_team,
                    'home_team': home_team,
                    'away_pitcher': away_pitcher,
                    'home_pitcher': home_pitcher,
                    'away_pitcher_id': away_pitcher_id,
                    'home_pitcher_id': home_pitcher_id
                }

                
                game_data.append(game_info)

            except IndexError:
                print('IndexError')
                
    get_bbref_splits(game_data)

get_bbref_previews()

