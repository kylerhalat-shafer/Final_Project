import pandas as pd
import numpy as np
import math
import os
import random

class Die:
    
    '''
    The Die Class: is creating a 'die' meaning any probability object, whether it is for a coin flip or rolling a six-sided die.
    Params: It will have faces, weights for each of those faces, be able to activate or 'roll' the 'die' 
    Return: A dataframe with the faces and weights 
    '''
    
    def __init__(self, faces):
        ''' 
        description: Here we are initializing the Die class 
        param: 1.) Faces, which is an array to create any die object. 2.) Weights are just a number e.g. 5 versus 1, rather than a normalized probability distribution 
        type: 1.) Faces are strings or numbers 2.) Weights are integers or floats
        return: The faces and the weights, originally set to a value of 1, will then be cataloged in a dataframe
        '''
        self.faces = faces #defining faces and so it can be called inside the class
        self.weights = np.ones(len(faces)) #defining the weights as an array of 1 to match the length of faces
        self.__df = pd.DataFrame({'faces': self.faces, 'weights':self.weights}) # dataframe with both faces and weights included, private
        
    def change_the_weight(self,new_face, new_weight):
        ''' 
        description: This gives the user the ability to change the weight by first giving the argument of the face
        param: 1.) New_face, for example we have a six sided die, the user will pick the side '4' and be able to adjust the weight as 2.) new_weight
        type: 1.) New_face are strings or numbers 2.) New_weight are integers or floats
        return: changing the dataframe from above to incorporate the new weight given
        '''
        if new_face not in list(self.__df['faces']): # testing to see if the new_face is in the dataframe initialized
            print('Value did not pass')
        else:
            if (type(new_weight)) not in [int,float]:# testing to see if the new_weight 
                print('Change to integer or float to continue')
            else:
                self.__df.loc[self.__df.faces == new_face, 'weights'] = new_weight #if both tests are passed then changing the dataframe to include the new_weight
        
    def roll(self, num_rolls = 1): #this is taking the argument of the number of rolls, defaulting to 1
        ''' 
        description: This is a random sample from the faces according to weights i.e. the rolling of a die 
        param: the number of rolls, initially set to 1
        type: integer or float
        return: the list of results, which is the faces after rolling the die a specified number of times
        '''
        results = [] 
        #my_probs = [i/sum(self.weights) for i in self.weights] 
        for i in range(num_rolls): 
            result = self.__df.faces.sample(weights = self.__df['weights']).values[0] 
            results.append(result)
        return results # where i is a single roll, the result is the face, and appending that result to the list
    
    def show(self):
        ''' 
        description: showing the current faces and weights as a dataframe
        '''
        print('The current state faces and weights:') 
        return self.__df

class DieGame:
    
    '''
    The DieGame Class: a game consists of rolling one or more 'die' 
    Params: Inputting each die, that have faces and weights already defined 
    Return: A dataframe of the number of die, the rolls, and the faces
    '''
    
    def __init__(self,dice): #input the dice that have been created using the first class, Die
        ''' 
        description: Each game is initialized by having one or more similarly defined dice e.g. d and d2 were created and can be used in this game
        param: each die has the same amount of faces, but the weights can differ
        type: the faces are either string or numeric,but not intermixed
        '''
        self.dice = dice #this will allow the dice to be called on
        
    def play2(self,n_rolls = 1):
        ''' 
        description: This method will roll the dice the specified number of times the user inputs
        param: N_rolls is the number of rolls that should occur
        type: integer
        return: a dataframe that the rows are the roll number, the columns are the die, and the face rolled as the element 
        '''
        self.__roll_results = pd.DataFrame(index=range(1,n_rolls + 1)) #setting the row to offset and start with 1
        self.__roll_results.index.rename('Roll_Number' ,inplace = True) # renaming the row to be 'Roll_Number'
        n = 0
        for die in self.dice: #for each die in dice
            roll = die.roll(n_rolls) #iterating over the multiple dies in dice, for the amount of rolls 
            self.__roll_results[n] = roll #starting as a blank dataframe then adding the roll 
            n = n + 1 #need to define a column with each new die, since there can be more than 1
            
    
    def display(self, wide = True):
        ''' 
        description: Producing a wide dataframe by default and creating the option for a narrow dataframe to be given
        param: True as the input for a wide dataframe and False for a narrow dataframe
        return: Either a wide or narrow data frame of the roll number, dies, and faces rolled
        '''
        d1 = self.__roll_results.copy() #needed to make a copy, originally by altering the actual dataframe infringed on code written later
        d1['id'] = d1.index
        narrowdf = pd.melt(d1, id_vars = ["id"]) #using the copied dataframe to make the adjustment to narrow, which needs an id parameter
        narrowdf.columns = ['Roll_Number','Die','Face_Value'] #name the columns
        narrowdf.set_index(['Roll_Number','Die'],inplace = True) #allowing Roll Number and Die to be stacked
        
        if wide == True:
            return self.__roll_results
        if wide == False:
            return narrowdf
        else:
            return 'Please enter True to return a wide dataframe and False for a narrow dataframe.'

class Analyzer: 
    
    '''
    The Analyzer Class: Giving outputs to help understand what happened in a given game
    Params: A game that has one or more die in it 
    Returns: Different views of when all faces are equal, the unique instances, and overall face counts 
    '''
    
    def __init__(self,game): 
        ''' 
        description: Takesthe results of a single game and analyzes that game
        param: the game that was ran off of the previous class 
        return: displays the type in the game 
        '''
        self.game = game
        game.display().dtypes
    
    def jackpot(self):
        ''' 
        description: How many times a roll, with one or multiple dies, resulted in all faces being the same 
        param: inputting a game through this method
        type:Intger
        return: a dataframe of just the roll numbers that have all faces equal
        '''
        ww = [] #creating an empty list to append to 
        for r in range(len(self.game.display())): #game.display() is the dataframe from the class DieGame, we want the length of that to iterate through 
            if len(set(list(self.game.display().loc[r+1,:]))) == 1: #then looking at each row,using loc, by creating this into a set, if all faces are the same it will output an integer
                ww.append(True) 
            else:
                ww.append(False) # we want both True and False results in this list 
        self.jack = self.game.display()[ww] # we can then take that list against the new dataframe for jackpot that is created to display the roll number and faces
        return len(self.jack)
    
    def combo(self):
        ''' 
        description: How many combination types of faces were rolled 
        param: inputting a game through this method
        type:
        return:
        '''
        self.comb = pd.DataFrame(self.game.display().groupby(list(self.game.display().columns)).size()) #creating a dataframe based on the data frame from the DieGame class, grouping by the columns
        # transforming those columns into a list, and takes the number of rows using size 
        self.comb.columns = ['Number of Instances'] #naming the columns
        return self.comb.sort_values(by=['Number of Instances'])
    
    def face_counts(self):
        ''' 
        description: the number of times a given face appeared in each roll 
        return: a cross tab of faces by roll 
        '''
        self.gamecross = pd.crosstab(index = list(self.game.display(False).reset_index()['Roll_Number']), columns = list(self.game.display(False)['Face_Value']))
        #the row is the narrow df, after reseting the index so that only Roll Number can be used, the columns are the Face Values in the narrow dataframe, which needs to be a list in a df
        return self.gamecross
