from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from tools import *

GOLF = 0.001
SLALOM = 10.




class GolfeurStrategy(Strategy):
    def __init__(self):
        super(GolfeurStrategy,self).__init__("Golf")

    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        act = Action(state,id_team,id_player)
        zones = state.get_zones(id_team)
        
        if len(zones)==0:
            """ shooter au but """
            ### on va vers la balle puis on tire vers le but ###
            act.aller_vers_balle
            return SoccerAction(act.shoot)

        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la balle est dans une zone a valider """
        ###on se dirige vers la prochaine zone a passer##
        
        if zone.dedans(state.ball.position):
            state.ball.position-zone.position+Vector2D(z.l/2.,z.L/2.)
    
            
            return SoccerAction()
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        return SoccerAction()

