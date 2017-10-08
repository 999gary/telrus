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

    def createObject( self, types ):
        if(types=='gbox'):

            #HACK please for the love of god make me change this next part very quickly
            return gbox( 10, 10, 100, 100, self.pygame)

    def requestobject(self, id):
        return self.uielements[id]
    def drawhook(self, thing):

            thing.draw(self.telrus.surface)

    def updatehook():
        print('nah')

class UI:
    def __init__( self, h, w, x, y, pygamec ):
        self.pygamei = pygamec
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

class gbox:
    def __init__( self, h, w, x, y, pygamec ):
        self.pygamei = pygamec
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
    def draw(self, hook):
        self.pygamei.draw.rect(hook, (255, 255, 255), (self.x, self.y, self.h, self.w))
