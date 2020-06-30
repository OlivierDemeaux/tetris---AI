# Tetris Game and AI Neural Network that  plays the game and learns throught genetic algorithm

This is a tetris game made with pygame and a neural network AI that learns to play the game throught a genetic algorith, getting better at the game generations after generations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame, deepcopy and numpy.

ex:
```bash
pip install pygame
```

## Usage

To start the game and play Tetris, do 
```
python main.py
```
 in the 'tetris---AI' folder.

To start the Neural Network and look at the AI learning process, do 
```
python main.py
```
in the 'tetris---AI/ai' folder.

## Notes

I did this project after seeing a video about it on youtube.

I feel pretty good about this AI. It could use more work to clean the code, and the AI doesn't see a certain move as valid even if it is and therefore the results I get from the AI are sub-optimal, but I coded it within a few day and didn't use anyone else code or help to do it. All the code is mine and mine alone, which makes me feel a bit of pride and accomplishment.

Possible improvement: Make the AI understand that it can slide a new piece under a piece already on the board if there is some room. Right now, the AI test the availability of a new piece by dropping it from the top of the board to the bottom of it. Therefor, the mosst optimal move is not always being seen by the AI which decrease it performance.

Overall: Really fun project. Was a lot more algo and probleme solving than AI oriented project that i was expecting but had a lot of fun  none the less