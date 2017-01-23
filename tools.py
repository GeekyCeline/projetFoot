# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:57:26 2017

@author: 3407073
"""
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

class MyState(object): 
    def __init__(self,state,idteam_idplayer): 
        self.state = state
        self.key = (idteam,idplayer)
    def my_position(self): 
        return self.state.player_state(self.key[0],self.key[1]).position
    def ball_position(self): 
        return self.state.ball.position
    def aller(self,p): 
        return SoccerAction(p-self.my_position(),Vector2D())
    def shoot(self,p): 
        return SoccerAction(Vector2D(),p-self.position(),Vector2D())
    def compute_strategy(self): 
        return self.aller(p)=self.shoot(p)