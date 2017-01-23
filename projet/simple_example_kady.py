from soccersimulator.strategies import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation,SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D



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
        
        return SoccerAction(state.ball.position -(state.player_state(id_team,id_player).position),Vector2D(3.14,55))#mettre init au lieu de create random pour la ball

class GoalKeeperStrategy(Strategy): 
    def __init__(self): 
        Strategy.__init__(self,"GoalKeeper")
    def compute_strategy(self,state,id_team,id_player):
        distance = state.ball.position -(state.player_state(id_team,id_player).positon)
        if distance <10: #PLAYER_RADIUS + BALL_RADIUS:
           return SoccerAction((state.player_state(id_team,id_player).position),Vector2D(60,0))#mettre init au lieu de create random pour la ball

## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John", GoalKeeperStrategy()) #Strategie qui ne fait rien
team2.add("Paul",StrikerStrategy())   #Strategie aleatoire
#team1.add("John",GoalKeeperStrategy())

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
