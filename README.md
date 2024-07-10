# SnakesAndLadder
 
The objective is to find the expected number of moves required to beat the children's game of Snakes And Ladders.

We will calculate this using Monte Carlo Simulation.

Rules: 

- Roll a dice from 1-6
- Require a 6 to get out of the starting spot AND move 6 spaces
- If you land at the base of a ladder you love to the top of the ladder.
- -If you land on the head of the snake you move to the bottom of the snake
- -to win you must land exactly on the 100 spot if you over roll you move backwards. (I.e if you need 4 to finish and you roll 6. You bounce back to spot 98 and go down the ladder).

![image](https://github.com/Chengalex96/SnakesAndLadder/assets/81919159/f8a6d08a-201e-4423-b7a5-887c79422394)

From a simulation of 100,000 Runs:
- 1 Player is expected to take 83.39 turn to complete a game
- 2 players is expected to have a winner bt 46.5 turns
- 4 players are expected to have a winner by the 27.98 turn.
