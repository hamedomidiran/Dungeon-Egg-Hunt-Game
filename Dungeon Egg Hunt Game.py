import random
from IPython.display import clear_output as co

class DungeonGame:
    def __init__(self):
        self.rooms = [
                        (0,0),(1,0),(2,0),(3,0),(4,0),
                        (0,1),(1,1),(2,1),(3,1),(4,1),
                        (0,2),(1,2),(2,2),(3,2),(4,2),
                        (0,3),(1,3),(2,3),(3,3),(4,3),
                        (0,4),(1,4),(2,4),(3,4),(4,4),
                     ]


    def players_start(self):
        P                       = self.rooms[random.choice(range(len(self.rooms)))]
        return P
        
    def monsters_start(self,P):
        while True:
            M                   = self.rooms[random.choice(range(len(self.rooms)))]
            if M != P:
                break  
        return M
        
    def basket_start(self,P,M):
        while True:
            B                     = self.rooms[random.choice(range(len(self.rooms)))]
            if B != P and B != M:
                break       
        return B
    
    def door_start(self,P,M,B):
        while True:
            D                     = self.rooms[random.choice(range(len(self.rooms)))]
            if D != P and D != M and D != B:
                break       
        return D
    
    def eggs_start(self,P,M,B,D):
        while True:
            E1                    = self.rooms[random.choice(range(len(self.rooms)))]
            if E1 != P and E1 != M and E1 != B and E1 != D:
                break
                
        while True:
            E2                    = self.rooms[random.choice(range(len(self.rooms)))]
            if E2 != P and E2 != M and E2 != B and E2 != D  and E2 != E1:
                break
                
        while True:
            E3                    = self.rooms[random.choice(range(len(self.rooms)))]
            if E3 != P and E3 != M and E3 != B and E3 != D  and E3 != E1 and E3 != E2:
                break
                
        return E1,E2,E3
            
        
    def get_basket(self,P,M,B):
        coordinate = P
        while coordinate != M and coordinate != B:
            co()
            print(coordinate)
            if self.rooms.index(coordinate) == 0:
                print('\nYou cannot move Up or Left')
                movement = input('\nYou have two directions to move in: Down/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up' or movement.lower() == 'left':
                    print('\nYou cannot move Up or Left')
                    movement = input('\nYou have two directions to move in: Down/Right'
                                     '\nWhat direction would you like to move in?     ')
         
                   
            elif self.rooms.index(coordinate) == 4:
                print('\nYou cannot move Up or Right')
                movement = input('\nYou have two directions to move in: Down/Left'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up' or movement.lower() == 'right':
                    print('\nYou cannot move Up or Right')
                    movement = input('\nYou have two directions to move in: Down/Left'
                                     '\nWhat direction would you like to move in?     ')
        
            
            elif self.rooms.index(coordinate) == 20:
                print('\nYou cannot move Down or Left')
                movement = input('\nYou have two directions to move in: Up/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down' or movement.lower() == 'left':
                    print('\nYou cannot move Down or Left')
                    movement = input('\nYou have two directions to move in: Up/Right'
                                     '\nWhat direction would you like to move in?     ')
        
                    
            elif self.rooms.index(coordinate) == 24:
                print('\nYou cannot move Down or Right')
                movement = input('\nYou have two directions to move in: Up/Left'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down' or movement.lower() == 'right':
                    print('\nYou cannot move Down or Right')
                    movement = input('\nYou have two directions to move in: Up/Left'
                                     '\nWhat direction would you like to move in?     ')
            
        
            elif self.rooms.index(coordinate) in range(0,5):
                print('\nYou cannot move up')
                movement = input('\nYou have three directions to move in: Down/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up':
                    print('\nYou cannot move up')
                    movement = input('\nYou have three directions to move in: Down/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(20,25):
                print('\nYou cannot move down')
                movement = input('\nYou have three directions to move in: Up/Left/Right'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down':
                    print('\nYou cannot move down')
                    movement = input('\nYou have three directions to move in: Up/Left/Right'
                                 '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(0, 21, 5):
                print('\nYou cannot move left')
                movement = input('\nYou have three directions to move in: Up/Down/Right'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'left':
                    print('\nYou cannot move left')
                    movement = input('\nYou have three directions to move in: Up/Down/Right'
                                 '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(4, 25, 5):
                print('\nYou cannot move right')
                movement = input('\nYou have three directions to move in: Up/Down/Left'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'right':
                    print('\nYou cannot move right')
                    movement = input('\nYou have three directions to move in: Up/Down/Left'
                                 '\nWhat direction would you like to move in?     ')
        
            if self.rooms.index(coordinate) not in range(0,5):
                if self.rooms.index(coordinate) not in range(20,25):
                    if self.rooms.index(coordinate) not in range(0, 21, 5):
                        if self.rooms.index(coordinate) not in range(4, 25, 5):
                            movement = input('\nYou have four directions to move in: Up/Down/Left/Right'
                                             '\nWhat direction would you like to move in?     ')
        
        
            if movement.lower() == 'up':
                x, y         = coordinate
                y           -= 1
                coordinate   = x,y

            elif movement.lower() == 'down':
                x, y          = coordinate
                y            += 1
                coordinate    = x,y
                
            elif movement.lower() == 'left':
                x, y         = coordinate
                x           -= 1
                coordinate   = x,y

            elif movement.lower() == 'right':
                x, y        = coordinate
                x          += 1
                coordinate  = x,y
                
            else:
                print('Sorry, That is not an option')
        
        if coordinate == M:
            co()
            print('\nYou have been caught by the monster. GAME OVER')
            return False
            
        elif coordinate == B:
            co()
            print('\nYou have found the basket, without being caught. Please proceed to finding the eggs.')
            return coordinate
        
    def get_eggs(self,P,M,E1,E2,E3):
        coordinate = P
        counter = 0
        egg_lists = [E1,E2,E3]
        found_eggs = []
        while counter != 3:
            while coordinate != M:
                co()
                print(coordinate)
                if self.rooms.index(coordinate) == 0:
                    print('\nYou cannot move Up or Left')
                    movement = input('\nYou have two directions to move in: Down/Right'
                                         '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'up' or movement.lower() == 'left':
                        print('\nYou cannot move Up or Left')
                        movement = input('\nYou have two directions to move in: Down/Right'
                                         '\nWhat direction would you like to move in?     ')
         
                   
                elif self.rooms.index(coordinate) == 4:
                    print('\nYou cannot move Up or Right')
                    movement = input('\nYou have two directions to move in: Down/Left'
                                         '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'up' or movement.lower() == 'right':
                        print('\nYou cannot move Up or Right')
                        movement = input('\nYou have two directions to move in: Down/Left'
                                         '\nWhat direction would you like to move in?     ')
            
                
                elif self.rooms.index(coordinate) == 20:
                    print('\nYou cannot move Down or Left')
                    movement = input('\nYou have two directions to move in: Up/Right'
                                         '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'down' or movement.lower() == 'left':
                        print('\nYou cannot move Down or Left')
                        movement = input('\nYou have two directions to move in: Up/Right'
                                         '\nWhat direction would you like to move in?     ')
            
                        
                elif self.rooms.index(coordinate) == 24:
                    print('\nYou cannot move Down or Right')
                    movement = input('\nYou have two directions to move in: Up/Left'
                                         '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'down' or movement.lower() == 'right':
                        print('\nYou cannot move Down or Right')
                        movement = input('\nYou have two directions to move in: Up/Left'
                                         '\nWhat direction would you like to move in?     ')
                
            
                elif self.rooms.index(coordinate) in range(0,5):
                    print('\nYou cannot move up')
                    movement = input('\nYou have three directions to move in: Down/Left/Right'
                                         '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'up':
                        print('\nYou cannot move up')
                        movement = input('\nYou have three directions to move in: Down/Left/Right'
                                         '\nWhat direction would you like to move in?     ')
            
                elif self.rooms.index(coordinate) in range(20,25):
                    print('\nYou cannot move down')
                    movement = input('\nYou have three directions to move in: Up/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'down':
                        print('\nYou cannot move down')
                        movement = input('\nYou have three directions to move in: Up/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
            
                elif self.rooms.index(coordinate) in range(0, 21, 5):
                    print('\nYou cannot move left')
                    movement = input('\nYou have three directions to move in: Up/Down/Right'
                                     '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'left':
                        print('\nYou cannot move left')
                        movement = input('\nYou have three directions to move in: Up/Down/Right'
                                     '\nWhat direction would you like to move in?     ')
            
                elif self.rooms.index(coordinate) in range(4, 25, 5):
                    print('\nYou cannot move right')
                    movement = input('\nYou have three directions to move in: Up/Down/Left'
                                     '\nWhat direction would you like to move in?     ')
                    while movement.lower() == 'right':
                        print('\nYou cannot move right')
                        movement = input('\nYou have three directions to move in: Up/Down/Left'
                                     '\nWhat direction would you like to move in?     ')
            
                if self.rooms.index(coordinate) not in range(0,5):
                    if self.rooms.index(coordinate) not in range(20,25):
                        if self.rooms.index(coordinate) not in range(0, 21, 5):
                            if self.rooms.index(coordinate) not in range(4, 25, 5):
                                movement = input('\nYou have four directions to move in: Up/Down/Left/Right'
                                                 '\nWhat direction would you like to move in?     ')
        
        
                if movement.lower() == 'up':
                    x, y         = coordinate
                    y           -= 1
                    coordinate   = x,y
    
                elif movement.lower() == 'down':
                    x, y          = coordinate
                    y            += 1
                    coordinate    = x,y
    
                elif movement.lower() == 'left':
                    x, y         = coordinate
                    x           -= 1
                    coordinate   = x,y
    
                elif movement.lower() == 'right':
                    x, y        = coordinate
                    x          += 1
                    coordinate  = x,y
    
                else:
                    print('Sorry, That is not an option')
                
                egg_lists = [E1,E2,E3]
                
                for i in egg_lists:
                    if i == coordinate and i not in found_eggs:
                        counter += 1
                        found_eggs.append(i)
                        if counter != 3:
                            print(f'\nYou have found {counter} egg(s). Please proceed to finding the other {3 - counter} egg(s).') 
                        elif counter == 3:
                            break

                if counter == 3:
                    co()
                    print('\nCongratulations you have found all three eggs.' 
                          '\nThe final step is to find the escape door without being caught.')
                    return coordinate
                break

            if coordinate == M:
                co()
                print('\nYou have been caught by the monster. GAME OVER')
                return False


    def escape_door(self,P,M,D):
        coordinate = P
        while coordinate != M and coordinate != D:
            co()
            print(coordinate)
            if self.rooms.index(coordinate) == 0:
                print('\nYou cannot move Up or Left')
                movement = input('\nYou have two directions to move in: Down/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up' or movement.lower() == 'left':
                    print('\nYou cannot move Up or Left')
                    movement = input('\nYou have two directions to move in: Down/Right'
                                     '\nWhat direction would you like to move in?     ')
         
                   
            elif self.rooms.index(coordinate) == 4:
                print('\nYou cannot move Up or Right')
                movement = input('\nYou have two directions to move in: Down/Left'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up' or movement.lower() == 'right':
                    print('\nYou cannot move Up or Right')
                    movement = input('\nYou have two directions to move in: Down/Left'
                                     '\nWhat direction would you like to move in?     ')
        
            
            elif self.rooms.index(coordinate) == 20:
                print('\nYou cannot move Down or Left')
                movement = input('\nYou have two directions to move in: Up/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down' or movement.lower() == 'left':
                    print('\nYou cannot move Down or Left')
                    movement = input('\nYou have two directions to move in: Up/Right'
                                     '\nWhat direction would you like to move in?     ')
        
                    
            elif self.rooms.index(coordinate) == 24:
                print('\nYou cannot move Down or Right')
                movement = input('\nYou have two directions to move in: Up/Left'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down' or movement.lower() == 'right':
                    print('\nYou cannot move Down or Right')
                    movement = input('\nYou have two directions to move in: Up/Left'
                                     '\nWhat direction would you like to move in?     ')
            
        
            elif self.rooms.index(coordinate) in range(0,5):
                print('\nYou cannot move up')
                movement = input('\nYou have three directions to move in: Down/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'up':
                    print('\nYou cannot move up')
                    movement = input('\nYou have three directions to move in: Down/Left/Right'
                                     '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(20,25):
                print('\nYou cannot move down')
                movement = input('\nYou have three directions to move in: Up/Left/Right'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'down':
                    print('\nYou cannot move down')
                    movement = input('\nYou have three directions to move in: Up/Left/Right'
                                 '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(0, 21, 5):
                print('\nYou cannot move left')
                movement = input('\nYou have three directions to move in: Up/Down/Right'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'left':
                    print('\nYou cannot move left')
                    movement = input('\nYou have three directions to move in: Up/Down/Right'
                                 '\nWhat direction would you like to move in?     ')
        
            elif self.rooms.index(coordinate) in range(4, 25, 5):
                print('\nYou cannot move right')
                movement = input('\nYou have three directions to move in: Up/Down/Left'
                                 '\nWhat direction would you like to move in?     ')
                while movement.lower() == 'right':
                    print('\nYou cannot move right')
                    movement = input('\nYou have three directions to move in: Up/Down/Left'
                                 '\nWhat direction would you like to move in?     ')
        
            if self.rooms.index(coordinate) not in range(0,5):
                if self.rooms.index(coordinate) not in range(20,25):
                    if self.rooms.index(coordinate) not in range(0, 21, 5):
                        if self.rooms.index(coordinate) not in range(4, 25, 5):
                            movement = input('\nYou have four directions to move in: Up/Down/Left/Right'
                                             '\nWhat direction would you like to move in?     ')
        
        
            if movement.lower() == 'up':
                x, y         = coordinate
                y           -= 1
                coordinate   = x,y

            elif movement.lower() == 'down':
                x, y          = coordinate
                y            += 1
                coordinate    = x,y

            elif movement.lower() == 'left':
                x, y         = coordinate
                x           -= 1
                coordinate   = x,y

            elif movement.lower() == 'right':
                x, y        = coordinate
                x          += 1
                coordinate  = x,y

            else:
                print('Sorry, That is not an option')
        
        if coordinate == M:
            co()
            print('\nYou have been caught by the monster. GAME OVER')
            return True
            
        elif coordinate == D:
            co()
            print('\nYou found the escape door and therefore won the game. Congratulations!!')
            return True
        

def runGame():
    print('\nType 1 to start a new game. Type 2 to stop the game.')
    to_start = int(input('>>>>     '))
    
    while to_start != 1 and to_start != 2:
        co()
        print('\nSorry, That is not an option')
        print('\nType 1 to start a new game. Type 2 to stop the game.')
        to_start = int(input('>>>>     '))
        
    while to_start == 1:    
        game1 = DungeonGame()
        co()
        P   = game1.players_start()
        M   =  game1.monsters_start(P)
        B   =  game1.basket_start(P,M)
        D   =  game1.door_start(P,M,B)
        E1, E2, E3 = game1.eggs_start(P,M,B,D)
        P  =  game1.get_basket(P,M,B)
        if P != False:
            co()
            P  = game1.get_eggs(P,M,E1,E2,E3)
            if P != False:
                co()
                game1.escape_door(P,M,D)
                print('\nType 1 to start a new game. Type 2 to stop the game.')
                to_start = int(input('>>>>     '))

                while to_start != 1 and to_start != 2:
                    co()
                    print('\nSorry, That is not an option')
                    print('\nType 1 to start a new game. Type 2 to stop the game.')
                    to_start = int(input('>>>>     '))
            else:
                print('\nType 1 to start a new game. Type 2 to stop the game.')
                to_start = int(input('>>>>     '))

                while to_start != 1 and to_start != 2:
                    co()
                    print('\nSorry, That is not an option')
                    print('\nType 1 to start a new game. Type 2 to stop the game.')
                    to_start = int(input('>>>>     '))

        else:
            print('\nType 1 to start a new game. Type 2 to stop the game.')
            to_start = int(input('>>>>     '))
            
            
            while to_start != 1 and to_start != 2:
                co()
                print('\nSorry, That is not an option')
                print('\nType 1 to start a new game. Type 2 to stop the game.')
                to_start = int(input('>>>>     '))
                
    
    print('\nThank you for playing. Have a nice day!')
      
runGame()        