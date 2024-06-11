# Tic-Tac-Toe with AI
This project is a simple implementation of the classic Tic-Tac-Toe game using Pygame for the graphical interface and a custom-built AI opponent that uses the minimax algorithm to make optimal moves.
## Explanation
- Using minimax algorithm to implement an opponenet that always choose the optimal decision
- AI Logic:  
The AI uses the minimax algorithm to make optimal moves. The minimax function calls maxValue or minValue depending on the current player to determine the best
possible move. The maxValue and minValue functions recursively evaluate all possible moves and their outcomes to find the optimal move.
## Acknowledgments
- **runner.py** was implemented by COE course instructors at KFUPM
- The minimax algorithm concept from artificial intelligence textbooks and online resources, specially from [CS50.ai](https://cs50.ai/)
# Usage
1. Run **runner.py** to start the game
2. Select whether you want to play as X or O by clicking the corresponding button.
3. Make your moves by clicking on the empty tiles.
4. The AI will make its move after you.
5. The game will display the result (win, lose, or tie) once it ends.
6. Click the "Play Again" button to start a new game.
## Date
This was submitted on March 15th 2022
