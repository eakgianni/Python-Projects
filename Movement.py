#unfinished dungion crawl system

import sys


##Classes##
class player():
    def __init__ (self):
        self.x = 0 #the players y,x location
        self.y = 1
        
    
    
    def collision_detect(self,direction, current_room):
         
        can_move = getattr(current_room, direction)
        
        
        return can_move
    
    def move(self, ychange, xchange, direction, current_room):   
        
        player.collision_detect(direction, current_room)
        if player.collision_detect(direction, current_room) == True:#when you can go the inputed direction
            player.x = player.x + xchange
            player.y = player.y + ychange
        else:
            print("You can't go this way")#you cant go n the inputed direction and go back to the begining of game loop
        
        
        
        return   
player = player()

class start_room():
    def __init__ (self):
        self.solved = False
        
        self.north = False
        self.south = False
        self.east = True
        self.west = False
        
    def description(self):
        print('ERROR')
    def room_check(self):
        print('ERROR')



class hall_room():
    def __init__ (self):
        self.solved = False
        
        self.north = False
        self.south = False
        self.east = False
        self.west = True
        
    def description(self):
        print('This is a hallway')
    def room_check(self):
        print('there is a chest in the corner')
    

##Map##

Map = [[None, None,], 
       [start_room(), hall_room()]]
       


##Game##        
def gameloop():
    print(player.y, player.x)
    
    
    while 1 == 1:
        
        current_room = Map[player.y][player.x]
        
        current_room.description()
        
        if player.y == 3 and player.x == 1:
            print('you win')
            input()
            sys.exit()
        command = ''
        accepable_commands = ['north', 'south', 'east', 'west', 'check']
        while command not in accepable_commands:
            command = input('>')
        
        ###Direction--------------------------
        if command == 'north':
            player.move(-1, 0, 'north', current_room)
            
        elif command == 'south':
            player.move(1, 0, 'south', current_room)
        elif command == 'east':
            player.move(0, 1, 'east', current_room)
        elif command == 'west':
            player.move(0, -1, 'west', current_room)
        
        elif command == 'check':
            current_room.room_check()
        
        
        
        print(player.y, player.x)
        
        
   
gameloop()

