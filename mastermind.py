import itertools
import numpy as np
from random import randint
from random import choices
#make the game
class Mastermind():
#initialize the variables
    def __init__(self):
        self.colors=[1,2,3,4,5,6]
        self.set=itertools.permutations(self.colors, 4)
        self.goal=choices(self.colors, k=4)
        self.turnCounter=0
        self.win=0
# calculate the black/white pegs for a guess
    def guess(self,combination,goal):
        tempGoal=goal[:]
        black=0
        for i in range(len(tempGoal)):
            if combination[i]==tempGoal[i]:
                black+=1
        correctColors=0
        for item in combination:
            if(item in tempGoal):
                correctColors+=1
#black pegs count into the correct colors calculation
#so we just subtract the 2 to find white
        white=correctColors-black
        answer=[]
        answer += list(itertools.repeat("B", black))
        answer += list(itertools.repeat("W", white))
        answer += list(itertools.repeat("nope", 4-len(answer)))
        self.turnCounter+=1
#check for a win after each guess
        if(answer==["B","B","B","B"]):
            self.win=1
        return answer

#initialize the game
game=Mastermind()
#start the turn clock, check for a win after each round
while(game.turnCounter<=12 and game.win==0):
#requires a string of ex. "1 1 1 1" to parse correctly. 
    print("Give me a combination of the elements 1,2,3,4,5,6. Ya fucking idiot.")
    combo=input("1 line, 4 numbers, 3 spaces. It'll break if you don't do that exactly.").split()
    combo=list(map(int,combo))
#check if the guess is the valid format
#don't uptick the turn counter for an invalid format
#i'm not that big of an asshole
    if len(combo)!=4 or set(combo).issubset(game.colors)!=True:
        print("Invalid guess, moron. Make sure you're guessing four items from the list (e.g. '5 5 4 3')")
        continue
    print(game.guess(combo,game.goal))
    print("goal is "+str(game.goal))
#if we leave that game loop, print the win/loss statement
if(game.win==0):
    print("Haha, loser.")
else:
    print("I guess that was a pretty good game. I guess.")



class tree():
    def __init__(self):
        




