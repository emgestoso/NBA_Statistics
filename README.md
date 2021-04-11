# NBA_Statistics

## Autores:
Enrique Martínez Gestoso y Antonio de la Rubia Salvador

## Contenido:
README.md: Contiene información sobre los autores, ficheros y contenido del dataset.

nba_stats.py: Contiene el código en Python para la ejecución del programa de web scrapping sobre la página web https://basketball.realgm.com/nba/team-stats.

nbateams_stats_20-21.csv: Dataset en formato CSV proveniente de la extracción mediante técnicas de web scrapping sobre la página web https://basketball.realgm.com/nba/team-stats.

PRA1_ARS_EMG.pdf: Documento PDF con las respuestas a las preguntas y nombres de los componentes del grupo así como la tabla de contribuciones al trabajo.

## Español 
Obtiene las principales estadísticas de juego de los equipos de la NBA para la temporada 2020/2021 del proveedor de servicios [RealGM.com](https://basketball.realgm.com/nba/team-stats).

Las bibliotecas necesarias para ejecutar el script son:

```
pip install pandas
pip install requests
pip install beautifulsoup4
pip install os
```

Las estadísticas se almacenan en un dataset de tipo CSV.

Se incluyen las siguientes estadísticas para cada equipo de la NBA (**media por partido**):

- GP: Games Played - *Partidos Jugados*
- MPG: Minutes Per Game - *Minutos por Partido*
- FGM: Field Goals Made - *Tiros de Campo Encestados*
- FGA: Field Goals Attempts - *Tiros de Campo Intentados*
- FG%: Field Goals Percentage - *Porcentaje de Tiros de Campo Encestados*
- 3PM: Three-Points Field Goals Made - *Triples Encestados*
- 3PA: Three-Points Field Goals Attempts - *Triples Intentados*
- 3P%: Three-Points Field Goals Percentage - *Porcentaje de Triples Encestados*
- FTM: Free Throws Made - *Tiros Libres Encestados*
- FTA: Free Throws Attempts - *Tiros Libres Intentados*
- FT%: Free Throws Percentage - *Porcentaje de Tiros Libres Encestados*
- TOV: TurnOvers - *Pérdidas de Balón*
- PF: Personal Faults - *Faltas Personales*
- ORB: Offensive Rebounds - *Rebotes en Ataque*
- DRB: Defensive Rebounds - *Rebotes en Defensa*
- RPG: Total Rebounds Per Game - *Rebotes Totales*
- APG: Assist Per Game - *Asistencias*
- SPG: Steal Per Game - *Robos*
- BPG: Block Per Game - *Bloqueos*
- PPG: Points Per Game - *Puntos*
