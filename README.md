# Montecarlo 
This package will walk through a montecarlo simulation for probability objects that I have labeled as 'die'. Each object can be rolled, played, and analyzed. 

### Metadata: <br>
- Author: Kyler Halat-Shafer 
- Email: utx5qb@virginia.edu
- Package: montecarlo
- Date initially commited: 07/12/2022

### Installation: 
- pip install -e .
- import montecarlo.montecarlo import Die
- import montecarlo.montecarlo import DieGame
- import montecarlo.montecarlo import Analyzer

### API description: <br> 
- Class Die:
  - init 
    - params : takes faces as an argument 
    - data types: strings or numbers
    - default : the weights for each face is 1.0 
  - change the weight
    - params : faces and weight 
    - data types: strings or numbers for faces, integers or floats for weights
  - roll
    - params : number of rolls 
    - data types: integers or floats
    - default : 1 roll
  - show
    - params : none
    - data types: dataframe displaying the current set of faces and weights 
- Class DieGame:
  - init
    - params : one or more defined Die objects where each die has the same number of sides and associated faces, each die may have its own weights 
    - data types: composite of faces and weights 
  - play
    - params : how many times a die should be rolled 
    - data types: integer or float
    - default: 1 
  - display
    - params : wide = True
    - data types: passes a dataframe in either wide (True as the input) or narrow (False as the input), boolean type
    - default : True
- Class Analyzer:
  - init
    - params : takes a game object (defined in DieGame) 
    - data types: die faces as either numbers or strings
  - jackpot
    - params : none
    - data types: integer
  - combo
    - params : none
    - data types: dataframe
  - faces count per roll 
    - params : none
    - data types : datframe 

### Synopsis: <br> 
#### Below are utilizing all of the different methods inside each of the classes listed above, please see montecarlo_demo.ipynb for more details: 
- d = Die([1,2,3,4,5,6])
- d.change_the_weight(5,6)
- d.roll(10)
- d.show()
- d2 = Die([1,2,3,4,5,6])
- d2.change_the_weight(3,6)
- game = DieGame([d,d2])
- game.play2(10)
- game.display(False)
- game.display(True)
- analyze1 = Analyzer(game)
- analyze1.jackpot()
- analyze1.combo()
- analyze1.face_counts()

### Manifest: <br>
- montecarlo.py
- montecarlo_test.py
- montecarlo_demo.ipynb
- setup.py
-__init__.py
- test_results.txt
- LICENSE.text
