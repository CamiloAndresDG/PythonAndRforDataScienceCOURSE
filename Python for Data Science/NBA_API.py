# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:51:36 2021

@author: CamiloDiazG
"""

#CREACION DE API's (API= Aplication Program Interface=Interfaz del programa de aplicación)

#Que es API?
#Permite comunicacion entre dos partes de un software o sistema
#Por ejemplo, tengo mi programa, datos y otro componente software
#Estos se comunican por medio de inputs y outputs
#Pandas es un API, cuando cargamos los datos, el API enviara los datos al otro componente
#De igual manera sucede con los metodos

#Que es REST APIs?
#Son un tipo de API que permiten comunicarce a travez de internet 
#Permitiendo tener ventaja de almaceniamiento, datos, algoritmos de inteligencia artificial, entre otros

#RE=REpresentational
#S=State
#T=Transfer

#En el RestAPI nuestro programa es llamado por el cliente, son usados para interactuar con servicios web
#Tienen reglas 
 #Comunicacion
 #Input o Request
 #Output o Response
 
#EJEMPLO DE API con NBA.com
#!pip install nba_api
import pandas as pd#Se importa la libreria pandas con el as pd se hace un apodo a pandas para el uso posterior
from nba_api.stats.static import teams
from nba_api.stats.static import players
nba_teams=teams.get_teams()
nba_teams[:5] #DEVOLVERA UN JSON DE LOS VALORES

#Esto lo podemos convertir de un diccionario a una tabla
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key,value in dict_.items():
            out_dict[key].append(value)
    return out_dict

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head() #Devolvera los datos de los equipos que hay en la NBA
#Para buscar dentro de la tabla el equipo Warriors
df_warriors=df_teams[df_teams["nickname"]=="Warriors"]
df_warriors()

#Funcion que llamara a un metodo del API
from nba_api.stats.endpoints import leaguegamefinder
id_warriors=df_teams[df_teams["nickname"]=="Warriors"]
gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

games=gamefinder.get_data_frames()[0]
games.head() #Mostrara informacion de todos los juegos de los Warriors

#Podemos ver que juegos jugaron como local y como visitante
#En la tabla Matchup los vs=local y los @=visitante
#En este caso sera en todos los juegos jugados contra TOR (Toronto Raptors)
games_home=games[games["MATCHUP"]=="GSW vs. TOR"]
games_away=games[games["MATCHUP"]=="GSW @ TOR"]

#Con estos resultados podemos hacer una grafica teniendo en cuenta las fechas
#Y los resultados finales (si ganaron o perdieron y por que puntos)
import matplotlib.pyplot as plt
fig,ax= plt.subplots()
games_away.plot(x="GAME_DATE",y="PLUS_MINUS",ax=ax)
games_home.plot(x="GAME_DATE",y="PLUS_MINUS",ax=ax)
ax.legend(["away","home"])
plt.show() #PARA PODER VER EL RESULTADO VER EL VID:https://youtu.be/MlM00ZK27lY

###

player_dict = players.get_players()





# Use ternary operator or write function 
# Names are case sensitive
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# find team Ids
from nba_api.stats.static import teams 
teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

##Getting Game Data
# First we import the endpoint
# We will be using pandas dataframes to manipulate the data
from nba_api.stats.endpoints import playergamelog
import pandas as pd 

#Call the API endpoint passing in lebron's ID & which season 
gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2018')

#Converts gamelog object into a pandas dataframe
#can also convert to JSON or dictionary  
df_bron_games_2018 = gamelog_bron.get_data_frames()

# If you want all seasons, you must import the SeasonAll parameter 
from nba_api.stats.library.parameters import SeasonAll

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()