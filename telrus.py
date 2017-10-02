import sys
import pygame
import math
import os
import configparser as cp
true = True;
false = False;  #xd


class Telrus:
    def __init__(self):
        print( '[Telrus] Initalizing Main Class' );
        pygame.init();
        pygame.font.init();
        self.width = config.getint('Window', 'width')
        self.height = config.getint('Window', 'height')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.shouldend = false
        self.maintimer = pygame.time.Clock()

    def exit(self):
        print('[Telrus] Exiting.')
        self.shouldend == true;
        pygame.quit();
        sys.exit();

    def run(self):
        #print( 'lmao this is so not finished' )
        while( not self.shouldend ):


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit();
                    else:
                        return event.key;


            self.maintimer.tick(config.getint('Window', 'fps'))



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
        if not os.path.isfile('config.cfg'):
            self.firstopen = true;
        else:
            self.firstopen = false;

        #TODO Make this process more streamlined
        self.config = cp.ConfigParser();
        if self.firstopen:
            self.config['Window'] = {};
            self.config['Window']['fps'] = '60';
            self.config['Window']['width'] = '1000';
            self.config['Window']['height'] = '800';
            self.config.write(open( 'config.cfg', 'w+' ));
        else:
            self.config.read('config.cfg');

    def getint(self, s, b):
        return self.config.getint( s, b )
    def getbool(self, s, b):
        return self.config.getboolean( s, b )




if __name__ == '__main__':
    config = TelrusConfig();
    main = Telrus();
    main.run();
