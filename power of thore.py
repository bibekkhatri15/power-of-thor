import sys
import math

lx, ly, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    if lx==tx:
        if ly> ty:
            print("S")
        else:
            print("N")

    if lx < tx:
        if ly> ty:
            print("SW")
            tx-=1
            ty+=1
        if ly<ty:
            print('NW')
            tx-=1
            ty-=1
        if ly==ty:
            print("W")
           

    if lx > tx:
        if ly==ty:
            print("E")
        if ly> ty:
            print("SE")
            tx+=1
            ty+=1
        if ly<ty:
            print("NE")
            tx+=1
            ty-=1
        
            
    
