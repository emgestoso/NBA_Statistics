# Importamos las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Declaramos la variable URL como string del link donde descargaremos la informacion
url = 'https://basketball.realgm.com/nba/team-stats'

# Opción para que el usuario introduzca la temporada que quiere consultar
# season = input("Introduce la temporada que quieres consultar:\n")

# Tipo de estadisticas a consultar, en este caso siempre serán estadisticas medias
# datatype = 'Averages'

# url2 = 'https://basketball.realgm.com/nba/team_stats/'+ season +'/' + datatype +'/Team_Totals/Regular_Season/gp/desc'


# Haciendo uso del metodo get de la clase requests, descargamos la pagina web y la almacenamos en la variable page
page = requests.get(url)

# Instanciamos el objeto beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

# Declaramos las columnas de nuestro dataframe
columns = ['#', 'Team', 'GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB',
           'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']

# Indicamos que las columnas del dataframe corresponden a las almacenadas en la lista "columns"
df = pd.DataFrame(columns= columns)

# Hacemos uso del metodo find de la clase beautiful soup sobre nuestro objeto "soup"
# para identificar el elemento html table
table = soup.find('table', attrs={'class': 'tablesaw', 'data-tablesaw-mode': 'swipe'}).tbody

# Dentro de la tabla almacenada en el objeto "table", encontramos los elementos html tr
# que identifican las filas de la tabla
trs = table.find_all('tr')

# Recorremos cada una de las filas de la tabla, iterando sobre los elementos que contienen y que se corresponden con las
# columnas de la tabla
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '')for td in tds]
    df = df.append(pd.Series(row, index= columns), ignore_index=True)

# Mostramos por pantalla el dataframe obtenido de la iteracion sobre la tabla html
print(df)

# Hacemos uso de la libreria os para identificar el path del codigo
directory_of_python_script = os.path.dirname(os.path.abspath(__file__))

# Transformamos el dataframe a formato CSV y lo guardamos en la ubicación del código
df.to_csv(os.path.join(directory_of_python_script, "nbateams_stats_20-21.csv"))


