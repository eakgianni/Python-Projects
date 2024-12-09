import os
import msvcrt

m = 0    

b = ([[' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']])
i = 1
while 1==1:
        
        os.system('cls')
        
        if i % 2 == 0:
            turn = 'O'
        else:
            turn = 'X'
        
               
        
        print(' ', b[0][0], '|', b[0][1], '|', b[0][2])
        print(' ', b[1][0], '|', b[1][1], '|', b[1][2])
        print(' ', b[2][0], '|', b[2][1], '|', b[2][2])
        print(' ')
        print (turn, 'turn')
        m = msvcrt.getch()      
        m = int(m)

        if not b[int((-m/3)+(9/3))][int((m+2)%3)] == 'X':
            
            if not b[int((-m/3)+(9/3))][int((m+2)%3)] == 'O':

                b[int((-m/3)+(9/3))][int((m+2)%3)] = turn
        
                i = i + 1
           
                
        
        
       
        
        
        
        
        
        
       
 