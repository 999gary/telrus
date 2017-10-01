import sys
import pygame
import math
true = True;

class Telrus:
    def __init__(self):
        print( '[Telrus] Initalizing Main Class' );
        pygame.init();
        pygame.font.init();
        self.width = 600;
        self.height = 800;
        self.screen = pygame.display.set_mode((self.width, self.height))

    def run(self):
        print( 'lmao this is so not finished' );
        while( true ):
            'lmaos'



class TelrusGameInstance:
    #You thought you would get good, quality code from this project.
    #But instead you got me,
    #Dio
    def __init__(self, player):
        print( '[Telrus] New Game Board Instance Thing' );
        self.player = player;

    def newboard(self, rows, lanes):
        self.rows = rows;
        self.lanes = lanes;

class Player:
    def __init__(self, name, id):
        self.name = name;
        self.id = id;



main = Telrus();
main.run();
