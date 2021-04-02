# NBA_Statistics

## Español 
Obtiene las principales estadísticas de juego de los equipos de la NBA para la temporada 2020/2021 del proveedor de servicios [RealGM.com](https://basketball.realgm.com/nba/team_stats/2021/Averages/Team_Totals/Regular_Season/gp/desc).

Las bibliotecas necesarias para ejecutar el script son:

```
pip install pandas
pip install requests
pip install beautifulsoup4
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
