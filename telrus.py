import sys
import pygame
import math
import os
import ConfigParser as cp
true = True;
false = False; #xd


class Telrus:
    def __init__(self):
        print( '[Telrus] Initalizing Main Class' );
        pygame.init();
        pygame.font.init();
        self.width = config.config.getint('Window', 'width');
        self.height = config.config.getint('Window', 'height');
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.maintimer = pygame.time.Clock()


    def run(self):
        print( 'lmao this is so not finished' );
        while( true ):
            self.maintimer.tick(config.config.getint('Window', 'fps'))



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

class TelrusConfig:

    def __init__(self):
        print( '[Telrus] Config Loaded.');
        if ~os.path.isfile('config.cfg'):
            self.firstopen = true;

        #TODO Make this process more streamlined
        with open( 'config.cfg', 'wb+' ) as cfg:
            self.configfile = cfg;
        self.config = cp.RawConfigParser();
        if self.firstopen:
            self.config.add_section('Window');
            self.config.set('Window', 'fps', '60');
            self.config.set('Window', 'width', '1000');
            self.config.set('Window', 'height', '800');
            self.config.write(open( 'config.cfg', 'wb+' ));
        else:
            self.config.read(open( 'config.cfg', 'r'));




config = TelrusConfig();
main = Telrus();
main.run();
