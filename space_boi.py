#### made by ehtrashypanda with pyxel
#### currently suffering from two issues / missing features
##1. collsion detection
##2. out of bounds //// DONE
## feel free to use this as a refrence for any projects!
import pyxel
import random
GRAV = 100  
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120



class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
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

##      Out of Bounds collision
        print(self.is_out_of_bounds())
        if self.is_out_of_bounds():
            # Place what you want when it goes out of bounds here
            print('Game Over !')
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

    def is_out_of_bounds(self):
        ## Will check if the player go out of bounds at a certain border and if so it returns true
        # "self.x + 4" is the left side of the player, "self.x + 11" is the right side of the player, "self.y + 4" is the top side of the player, "self.y + 14" is the bottom side of the player
        # TODO:you will need to take into account the correct border of your character in the future
        
        #Left Corner collision
        if self.x + 11 < 0:
            return True
        #Right Corner collision
        elif self.x + 4 > SCREEN_WIDTH:
            return True
        #Top Corner collision
        elif self.y + 14 < 10:
            return True
        #Bottom Corner collision
        elif self.y + 4 > SCREEN_HEIGHT:
            return True
        else:
            return False
            
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
        pyxel.rect(0,0,SCREEN_WIDTH,10, pyxel.COLOR_BLACK)
        s = "SCORE:{:04}".format(self.score)
        pyxel.text(0, 0, s, 6)
        f = "FUEL:{:02}".format(self.fuel)
        pyxel.text(120,0,f,6)
        self.show_fuel()
        self.check_fuel()
       
      
        
        


        
       
        
     
    
      
        

        

            
        
            
    
            
            
        

       
            
                
            
            
        
App()
