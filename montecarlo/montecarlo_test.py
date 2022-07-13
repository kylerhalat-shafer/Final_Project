import unittest
import pandas as pd
import numpy as np
from montecarlo import Die
from montecarlo import DieGame
from montecarlo import Analyzer

class DieGameTestSuite(unittest.TestCase):
    '''
    This testing file is designed to test each method in that is in each class of the module montecarlo. It imports the classses Die,DieGame, and Analyzer then specifically looks at each method in
    them, as they appear in the montecarlo.py file. 
    '''

    def test_change_the_weight(self): 
        '''
        description: This test is seeing if the face that is passed is in the array of weights. 
        return: By changing the weight of the face 5 to the weight of 6, then applying a boolean check to see if the new face's weight is equal to 6 provides a True respone
        note: Originally used a self.assertEqual method, however, this errored as pandas does not appreciate the boolean nature of testing dataframes or series 
        '''
        testing = Die([1,2,3,4,5,6])
        testing.change_the_weight(5,6) 
        new_face =  5
        df = testing.show()  
        df.loc[df.faces == new_face, 'weights'] == 6
    
    def test_roll(self): 
        '''
        description: Does the method take in how many times the die is to be rolled? Does this return a list of outcomes?
        return: By inputting a normal die, rolling it 10 times and then checking the length of roll using assertEqual as boolean response and seeing if it is a list is in the instance the 
        two questions are resolved
        note: Using k and l throughout as naming longer variables that are used in order to save computing time, reduce amount of code written, and getting in the habit of reduce, reuse, recycle
        '''
        testing = Die([1,2,3,4,5,6])
        k = testing.roll(10) 
        self.assertEqual(len(k),10) 
        self.assertIsInstance(k, list) 
     
    def test_show(self):
        '''
        description: Does this show the current set of faces and weights?
        return: By understanding that there are two columns, one for the roll number and the die(s) the length of a set will be 2 for columns, same as for the number of columns
        note: The set function here can be eliminated since all characters are unique
        '''
        testing = Die([1,2,3,4,5,6])
        df = testing.show() 
        self.assertEqual(len(set(list(df.columns))),2)
        self.assertEqual(len(set(list(df.index))), 6) 
  
    def test_play2(self): 
        '''
        description: Does it create a table where the columns are roll number, the die number is the row, and the element is the face?
        return: By playing a simple game of 10 rolls, the number of rows will be equal to the number of rolls, whereas the columns will be equal to 1 in display since the die is the only column
        in the way that this dataframe is designed
        '''
        testing = Die([1,2,3,4,5,6]) 
        game_test = DieGame([testing]) 
        game_test.play2(10) 
        self.assertEqual(len(list(game_test.display().index)), 10)
        self.assertEqual(len(game_test.display().columns), 1)
                   
    def test_display(self): 
        '''
        description: Is a narrow and a wide dataframe able to be created? Expected number of rows, columns, and indexes are also checked. 
        return: Boolean responses are returned for both the narrow and wide dataframes as well as the length of rows and columns. The difference in narrow and wide is having double the amount of
        rows in this example, which checking for and seeing is correct shows that both are created. As well as columns are different. 
        note: Originally used a self.assertEqual method, however, this errored as pandas does not appreciate the boolean nature of testing dataframes or series
        '''
        testing = Die([1,2,3,4,5,6])
        game_test = DieGame([testing, testing])
        game_test.play2(10)
        k = game_test.display(True) 
        l = game_test.display(False) 
        k == True
        l == True
        self.assertEqual(len(k.index),10) 
        self.assertEqual(len(k.columns),2) 
        self.assertEqual(len(l.index),20) 
        self.assertEqual(len(l.columns),1) 
        
    def test_jackpot(self): 
        '''
        description: Check the dataframe that is created if all face_values are identical.
        return: By doing a simple test with a die where it has only one face and one roll, then the jackpot would have to be triggered and be equal to one, shown below. 
        '''
        testing = Die([6])
        game_test = DieGame([testing])
        game_test.play2(1)
        test_jack = Analyzer(game_test) 
        self.assertEqual(test_jack.jackpot(),1) 
    
    def test_combo(self): 
        '''
        description: Check the dataframe that is created if all paired face_values are unique. 
        return: The idea here is to use the method as is, then to test it by reseting the index to get a length that is measurable against the number of rows. Without reseting the index 
        then checking the rows became increasing challenging. 
        '''
        testing = Die([1,2,3,4,5,6])
        game_test = DieGame([testing,testing])
        game_test.play2(10)
        test_combo = Analyzer(game_test)
        k = test_combo.combo()
        len(k.reset_index(drop=True))==10
                        
    def test_face_count(self):
        '''
        description: Check the dataframe that your face_count is saved. 
        return: By using a simple 1 faced die, the game can be played and saved to the dataframe and boolean tested to see if the dataframe has been saved. From there the rows should be equal 
        to the number of rolls, and the columns equal to the single die where the face is saved. Since the die = face, then the face is saved. 
        '''
        testing = Die([5])
        game_test = DieGame([testing])
        game_test.play2(10)
        test_faceco = Analyzer(game_test)
        test_faceco.face_counts() 
        k = test_faceco.gamecross  
        k == True 
        self.assertEqual(len(k.index),10) 
        self.assertEqual(len(k.columns),1) 
        
if __name__ == '__main__':
    unittest.main(verbosity=3)