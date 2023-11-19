# CSF_CAP2_pygame
# Tetris Game Unit Tests

## Game Overview

This document provides an overview of the test cases developed for the Tetris game in the Tetris.py module. The test cases are implemented using the Python unittest framework. Each test case aims to validate specific functionalities of the Tetris game, ensuring correctness and robustness.

## Resources Used

- **Python unittest Framework:**
  - *Justification:* The built-in `unittest` module in Python provides a standardized and convenient framework for organizing and executing tests. It ensures consistency and facilitates test discovery.

- **Pygame Library:**
  - *Justification:* Pygame is chosen for implementing and testing the Tetris game due to its cross-platform game development capabilities, rich feature set, and strong community support.

- **Mocking with `unittest.mock.patch`:**
  - *Justification:* Mocking using the `patch` function isolates the Tetris game code during testing, providing control over external dependencies. This improves test stability and allows for effective testing of various scenarios.

## Test Cases

### 1. Tetramino Rotation

Method: test_tetramino_rotation
Description: Validates the correct rotation behavior of a Tetramino object.

### 2. Creating a New Tetris Figure

Method: test_tetris_new_figure

Description: Ensures the successful creation and assignment of a new Tetris figure in the game.

### 3. Tetris Figure Intersection Check
    
Method: test_tetris_intersects

Description: Checks whether a Tetris figure intersects with existing blocks on the game board.


### 4. Removing a Line in Tetris

Method: test_tetris_remove_line

Description: Validates the removal of a line in the Tetris game and checks if the line is replaced with zeros.

### 5. Freezing a Tetris Figure

Method: test_tetris_freeze

Description: Verifies that a Tetris figure is correctly frozen in place at the bottom of the game board.

### 6. Moving a Tetris Figure Down

Method: test_tetris_go_down

Description: Ensures the proper downward movement of a Tetris figure.

### 7. Moving a Tetris Figure Sideways

Method: test_tetris_go_side

Description: Checks the lateral movement of a Tetris figure, specifically to the right.

### 8. Rotating a Tetris Figure

Method: test_tetris_rotate

Description: Validates the rotation of a Tetris figure.

### 9. Game Over Check

Method: test_tetris_game_over

Description: Confirms that the gameover flag is set when a Tetramino reaches the bottom of the game board.




    
