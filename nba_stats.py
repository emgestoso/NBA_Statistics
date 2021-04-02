from bs4 import BeautifulSoup
import requests
import pandas as pd

# Declaramos la variable URL como string del link donde descargaremos la informacion
# url = 'https://basketball.realgm.com/nba/team-stats'

season = input("Introduce la temporada que quieres consultar:\n")
datatype = 'Averages'

url2 = 'https://basketball.realgm.com/nba/team_stats/'+ season +'/' + datatype +'/Team_Totals/Regular_Season/gp/desc'


# Haciendo uso del metodo get de la clase requests,
# descargamos la pagina web y la almacenamos en la variable page
page = requests.get(url2)

# Instanciamos
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)

columns = ['#', 'Team', 'GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB',
           'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']

df = pd.DataFrame(columns= columns)

# Equipos
table = soup.find('table', attrs={'class': 'tablesaw', 'data-tablesaw-mode': 'swipe'}).tbody

trs = table.find_all('tr')
