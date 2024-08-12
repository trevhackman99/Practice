from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np

def get_bbref_splits(game_data):
    for game in game_data:
        away_pitcher_id = game['away_pitcher_id']
        home_pitcher_id = game['home_pitcher_id']

        away24_url = f'https://www.baseball-reference.com/players/split.fcgi?id={away_pitcher_id}&year=2024&t=p'
        home24_url = f'https://www.baseball-reference.com/players/split.fcgi?id={home_pitcher_id}&year=2024&t=p'

        away_response = requests.get(away24_url)
        home_response = requests.get(home24_url)

        away_data = bs(away_response.text, 'html.parser')
        home_data = bs(home_response.text, 'html.parser')

        # Platoon Splits
        # Find the nested table
        container = away_data.find('div', {'id': 'div_plato'})
        if container:
            away_platoon_splits = container.find('table', {'id': 'plato'})
            if away_platoon_splits:
                rows = away_platoon_splits.find_all('tr')
                for row in rows:
                    columns = row.find_all('td')
                    for column in columns:
                        print(column.text)
            else:
                print("Table with ID 'plato' not found within the container.")
        else:
            print("Container with class 'table_container' not found.")
        

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
                pass
                
    get_bbref_splits(game_data)

get_bbref_previews()

