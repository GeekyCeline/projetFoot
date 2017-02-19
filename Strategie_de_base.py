# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 18:09:32 2017

@author: eleve
"""


class Action(object): 
    def __init__(self,state,id_team,id_player): 
        self.state = state
        self.idt= id_team
        self.idp = id_player
        
       
    def aller_vers_balle(self):
        return SoccerAction(MyState.ball_position(self) -( self.my_position(),Vector2D(angle=3.14,norm=55)))
       # return SoccerAction(ball_position(self) -(position_player(self,state,id_team,id_player),Vector2D(angle=3.14,norm=55))
        #
    def aller_vers_balle_condition(self):
        if( MyState.est_team1(self)):
            liste_players = self.idt.nb_players #team1.nb_players
        else: 
            liste_players = team2.nb_players
        distance_self =MyState.distance_ball_player()
        for player in liste_players: 
            distance = MyState.ball_position(self) -  MyState.my_position(liste_players[player])
            if distance_self< distance : 
                continue
        #return SoccerAction(MyState.ball_position(self) -(self.my_position(),Vector2D(angle=3.14,norm=55)))
        return SoccerAction(distance_self,Vector2D(angle=3.14,norm=55))
        
        
    def aller_vers_but(self):
        essai=MyState(self.state,self.idt,self.idp)
        if essai.est_team1():
            return SoccerAction(POS_DEFAUT-essai.my_position(),Vector2D(3.14,20))
        return SoccerAction(POS_DEFAUT2-essai.my_position(),Vector2D(6.18,20))
         #   return SoccerAction(POS_DEFAUT-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
       #return  SoccerAction(POS_DEFAUT2-(state.player_state(id_team,id_player).position),Vector2D(3.14,20))
          
          
    def shoot_goal(self,state,id_team,id_player): 
        distance =MyState.distance_ball_player(self,state,id_team,id_player)
        if distance < PLAYER_RADIUS + BALL_RADIUS:
            return shoot()


#    def passe(self,state,id_team,id_player): 
#        distance = MyState.distance_ball_player(self,state,id_team,id_player)
#        if distance < PLAYER_RADIUS + BALL_RADIUS:
#            if Position.joueur_le_plus_proche(self) != False: 
#               #return shoot(self,Position.joueur_le_plus_proche(self,state,id_team_id_player))
#                return SoccerAction(Position.joueur_le_plus_proche(self,state,id_team_id_player)-MyState.myposition(),shoot(self))
#            
    def shoot(self,state,id_team,id_player):
        sh = Vector2D(0,0)
        if MyState.distance_ball_player() < PLAYER_RADIUS + BALL_RADIUS:
            if MyState.distance_but_ball() < 40: 
                sh = Vector2D(10,10)
            if MyState.distance_but_ball() > 40:# and personne(): 
                sh = Vector2D(20)
        return sh
    #eviter 

    def tirer_vers(qqun_qqchse): 
        

#    def bouger(self): 
#        return SoccerAction(acceleration,Vector2D(0,0))