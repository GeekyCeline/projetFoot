from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
#from tools import *

PLAYER_RADIUS= 1.
BALL_RADIUS= 0.65
GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 #

## Strategie aleatoire
class RandomStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player): 
		return SoccerAction(Vector2D.create_random(-10,10),Vector2D.create_random())
		
class StrikerStrategy(Strategy): #attaquant 
	def __init__(self): 
		Strategy.__init__(self,"Striker")
	def compute_strategy(self,state,id_team,id_player):
         return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=35)) 
          #return SoccerAction((state.ball.position)-Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))

                 
class DefenderStrategy(Strategy): #defenseur        
    def __init__(self):
		Strategy.__init__(self,"Defender")
    def compute_strategy(self,state,id_team,id_player):
       # state.player_state(id_team,id_player).positon 
        distance = state.ball.position.distance(state.player_state(id_team,id_player).position) #distance avec la balle
        distance_but = state.ball.position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        if distance <40 and distance_but<20:
            position_defaut = Vector2D(6,45) #dans le tools 
            if distance < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55))
            if id_team == 1: 
                return SoccerAction(position_defaut-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))+SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=55)) 
            
#	    return SoccerAction((state.player_state(id_team,id_player).position)-(state.player_state(self.id_team,self.id_player).position),Vector2D.create_random())
         #return SoccerAction(position_defaut2-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
    #       
class GoalKeeperStrategy(Strategy): 
    def __init__(self): 
        Strategy.__init__(self,"GoalKeeper")
    def compute_strategy(self,state,id_team,id_player):
       # state.player_state(id_team,id_player).positon 
    
        distance = state.ball.position.distance(state.player_state(id_team,id_player).position) #distance avec la balle
        distance_but = state.ball.position.distance(Vector2D(0,GAME_HEIGHT/2-(GAME_GOAL_HEIGHT/2)))
        if distance <40 and distance_but<20:
            position_defaut = Vector2D(6,45) #dans le tools 
            position_defaut2 = Vector2D(145,45) #dans le tools
            if distance < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(angle=3.14,norm=35))
            if id_team == 1: 
                return SoccerAction(position_defaut-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
            return SoccerAction(position_defaut2-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
          
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

team2.add("John",StrikerStrategy()) #Strategie qui defend
#team2.add("Paul",StrikerStrategy())   #Strategie attaque
team1.add("polo",DefenderStrategy())
team1.add("B",GoalKeeperStrategy())
#team2.add("A",GoalKeeperStrategy())
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
