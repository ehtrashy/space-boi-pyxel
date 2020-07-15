#### made by ehtrashypanda with pyxel
#### currently suffering from two issues / missing features
##1. collsion detection
##2. out of bounds
## feel free to use this as a refrence for any projects!
import pyxel
import random
GRAV = 100  



class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 80
        self.y = 60
        pyxel.playm(0, loop=True)
        self.boosty = 1.2343
        self.side_scroll_y = 30
        self.score = 0
        self.mus = 1
        self.fuel = 100
        self.minusfuel = 1
        self.gravity = 0.5120
        self.fuelx = 40
        self.fuely = 40
        pyxel.load('2ndboi.pyxres')
        pyxel.playm(0,loop=True)
        pyxel.run(self.update, self.draw)
        self.make_fuel = False

    def update(self):
        self.check_fuel()
        gravity_on = True
## player movement
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + 2    
        if pyxel.btn(pyxel.KEY_A):
            self.x = self.x - 2
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - self.boosty
            self.fuel = self.fuel - self.minusfuel
        if pyxel.btn(pyxel.KEY_E):
            self.y = self.y - self.boosty
            self.x = self.x + 2
            self.fuel = self.fuel - self.minusfuel
        if pyxel.btn(pyxel.KEY_Q):
            self.x = self.x - 2
            self.y = self.y - self.boosty
            self.fuel = self.fuel - self.minusfuel
## this was used to test boost
##        if pyxel.btn(pyxel.KEY_SPACE):
##            self.fuel += 10
##            self.score += 10
## stops boosting when fuel equals zero, and gravity
        if self.fuel == 0:
            self.boosty = 0
        elif self.fuel > 0:
            self.boosty = 1.2343
        else:
            self.boosty = 0
        if gravity_on == True:
            self.y += self.gravity
        if self.fuel == 0:
            self.minusfuel = 0
            self.boosty
        elif self.fuel > 0:
            self.minusfuel = 1
        else:
            self.minusfuel = 0
##        while str(self.x) in str(self.fuelx):
##            self.score += 100
##            self.fuel += 30
##            self.fuelx = random.randrange(0,160)
##            self.fuely = random.randrange(10,120)
    def check_fuel(self):
         if str(self.x) == str(self.fuelx) or str(self.y) == str(self.fuely):
            self.score += 100
            self.fuel += 30
            self.fuelx = random.randrange(10,150)
            self.fuely = random.randrange(10,110)
            
####          Checks if spaceman is on fuel

    def show_fuel(self):
        if self.make_fuel == True:
           fuel = pyxel.blt(self.fuelx,self.fuely,0,8,80,8,8,pyxel.COLOR_WHITE)
           make_fuel = False
        if self.x == self.fuelx and self.y == self.fuely:
            self.fuel += 10
        
    def draw(self):
        self.check_fuel()
        self.make_fuel = True
        pyxel.cls(0)
        pyxel.bltm(0,10,0,0,0,30,self.side_scroll_y,True)
        player = pyxel.blt(self.x,self.y,0,32,0,16,16,pyxel.COLOR_WHITE)
##      player movements  
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_E):
            player = pyxel.blt(self.x,self.y,0,0,0,16,16,pyxel.COLOR_WHITE)
            self.score += 10
        elif  pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            player = pyxel.blt(self.x - 1,self.y,0,16,0,16,16,pyxel.COLOR_WHITE)
            self.score += 10
##      print the score, position, and fuel, clearing the screen stops overwriting
        s = "SCORE:{:04}".format(self.score)
        pyxel.text(0, 0, s, 6)
        f = "FUEL:{:02}".format(self.fuel)
        pyxel.text(120,0,f,6)
        self.show_fuel()
        self.check_fuel()
       
      
        
        


        
       
        
     
    
      
        

        

            
        
            
    
            
            
        

       
            
                
            
            
        
App()
