#implimentation of a shitty ui system I made 2 years ago in lua
#should be fine
import pygame
true = True;
class Redam:
    def __init__(self, telrus):
        #create local instance of telrus
        self.telrus = telrus;
        #self.uielements = {};
        self.pygame = telrus.pygame;

    def createObject( self, types, h, w, x, y ):

        if(types=='gbox'):
            return gbox( h, w, x, y );

    def requestObject(self, id):

        return self.uielements[id]

    def drawHook(self, thing):

            thing.draw(self.telrus.surface);

    def updateHook():

        print('nah')

class UI:
    def __init__( self, h, w, x, y ):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.ShouldD = true;
    def setX(self, s):
        self.x = s;
    def setY(self, s):
        self.y = s;
    def setH(self, s):
        self.h = s;
    def setW(self, s):
        self.w = s;

class gbox(UI):
    def draw(self, hook):
        pygame.draw.rect(hook, (255, 255, 255), (self.x, self.y, self.h, self.w))
