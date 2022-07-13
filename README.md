# Montecarlo 
This package will walk through a montecarlo simulation for probability objects that I have labeled as 'die'. Each object can be rolled, played, and analyzed. 

### Metadata: <br>
- Author: Kyler Halat-Shafer 
- Email: utx5qb@virginia.edu
- Package: montecarlo
- Date initially commited: 07/12/2022

### API description: <br> 
- Class Die:
  - init
  - change the weight
  - roll
  - show
- Class DieGame:
  - init
  - play
  - display
- Class Analyzer:
  - init
  - jackpot
  - combo
  - faces count per roll 

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
