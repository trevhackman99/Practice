from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import pandas as pd
import numpy as np
import time

MAX_RETRIES = 10
RETRY_DELAY = 10  # seconds

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

        for attempt in range(MAX_RETRIES):
            try:

                html_page.html.render(sleep=4, timeout=30)
                html_page2.html.render(sleep=4, timeout=30)



                soup = bs(html_page.html.html, 'html.parser')
                soup2 = bs(html_page2.html.html, 'html.parser')

                a_platoon_table = soup.find('table', {'id': 'plato'})
                a_hmvis_table = soup.find('table', {'id': 'hmvis'})
                a_times_table = soup.find('table', {'id': 'times'})
                a_dr_table = soup.find('table', {'id': 'dr'})
                a_stad_table = soup.find('table', {'id': 'stad'})
                a_catch_table = soup.find('table', {'id': 'catch'})

                # Extract HTML content of the tables
                away_tables_html = [str(table) for table in [a_platoon_table, a_hmvis_table, a_times_table, a_dr_table, a_stad_table, a_catch_table]]

                

                

                h_platoon_table = soup2.find('table', {'id': 'plato'})
                h_hmvis_table = soup2.find('table', {'id': 'hmvis'})
                h_times_table = soup2.find('table', {'id': 'times'})
                h_dr_table = soup2.find('table', {'id': 'dr'})
                h_stad_table = soup2.find('table', {'id': 'stad'})
                h_catch_table = soup2.find('table', {'id': 'catch'})

                # Extract HTML content of the tables
                home_tables_html = [str(table) for table in [h_platoon_table, h_hmvis_table, h_times_table, h_dr_table, h_stad_table, h_catch_table]]

                # Create and write to an HTML file
                with open(f'tables{game_name}.html', 'w') as file:
                    file.write(f'''<html><head><title>Baseball Tables</title><link rel="stylesheet" href="tables.css"></head>
                               <body>
                               

                               <h1>{game['home_team']}</h1>
                                <div class='home_div'></div>  
                               
                               ''')
                    for table_html in away_tables_html:
                        file.write(f'''<h1>{game['away_team']}</h1>
                               <div class='away_div'>{table_html}</div>''')

                    for table_html in home_tables_html:
                        file.write(f'''<h1>{game['home_team']}</h1>
                                   <div class='home_div'>{table_html}</div>''')
                    file.write('</body></html>')
                    print(f'HTML {game_name} file created with tables.')
                break  # Exit the retry loop if successful



            except Exception as e:
                print(f'TimeoutError on attempt {attempt + 1}: e')
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY)
                else:
                    print('Max retries reached for this game. Moving to the next game.')
                    break

            

                
            
            

def get_bbref_previews():
    url = 'https://www.baseball-reference.com/previews/'
    response = requests.get(url)
    data = bs(response.text, 'html.parser')
    
    games = data.find_all('div', {'class': 'game_summary nohover'})

    game_data = []

    if games:
        for game in games:
            for attempt in range(MAX_RETRIES):
                try:
                    table = game.find_all('table')[1]
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
                    break  # Exit the retry loop if successful

                except IndexError:
                    print('IndexError')
                    break  # Exit the retry loop if an IndexError occurs

                except TimeoutError:
                    print(f'TimeoutError on attempt {attempt + 1}')
                    if attempt < MAX_RETRIES - 1:
                        time.sleep(RETRY_DELAY)  # Wait before retrying
                    else:
                        print('Max retries reached for this game. Moving to the next game.')
                        break   
    get_bbref_splits(game_data)

get_bbref_previews()

