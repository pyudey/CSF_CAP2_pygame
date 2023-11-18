import pygame
import random
import unittest
from unittest.mock import patch
from tetris import Tetris, Tetramino

# Define a test class that inherits from unittest
class TestTetrisGame(unittest.TestCase):
    
    # Set up method that initializes Pygame
    def setUp(self):
        pygame.init()
    
    # Tear down method that quits Pygame
    def tearDown(self):
        pygame.quit()
    
    # Test rotation of Tetramino
    def test_tetramino_rotation(self):
        # Create a Tetramino at position (0,0)
        tetramino = Tetramino(0, 0)
        # Store the initial rotation
        initial_rotation = tetramino.rotation
        # Rotate the Tetramino
        tetramino.rotate()
        # Assert that the rotation has changed as expected
        self.assertEqual(tetramino.rotation, (initial_rotation + 1) % len(tetramino.shape))
    
    # Test creating a new Tetris figure
    def test_tetris_new_figure(self):
        # Create a Tetris game with a board size of 20*10
        tetris = Tetris(20, 10)
        # Create a new Tetris figure
        tetris.new_figure()
        # Assert that the figure is not None
        self.assertIsNotNone(tetris.figure)
    
    # Test if a Tetris figure intersects with existing blocks on the board
    def test_tetris_intersects(self): 
        tetris = Tetris(20, 10)
         # Set the current figure to a Tetramino at position (0, 0)
        tetris.figure = Tetramino(0, 0)
        # Assert that the figure doesn't intersect with existing blocks
        self.assertFalse(tetris.intersects())

    # Test removing a line in Tetris and checking if it contains all zeros
    def test_tetris_remove_line(self):
        tetris = Tetris(20, 10)
        # Set the board with a full line at the top
        tetris.board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0] * 10 for _ in range(19)]
        # Remove the line
        tetris.remove_line()
        # Check if all rows, except the first one, contain zeros
        self.assertTrue(all(cell == 0 for cell in tetris.board[0]))
    

    # Test freezing a Tetris figure in place
    def test_tetris_freeze(self):
        tetris = Tetris(20, 10)
        tetris.figure = Tetramino(0, 0)
         # Freeze the figure in place
        tetris.freeze()
        # Assert that the figure is not None and has y-coordinate set to 0
        self.assertIsNotNone(tetris.figure)
        self.assertEqual(tetris.figure.y, 0)
    
     # Test moving a Tetris figure down
    def test_tetris_go_down(self):
        tetris = Tetris(20, 10)
        tetris.figure = Tetramino(0, 0)
        # Store the initial y-coordinate
        initial_y = tetris.figure.y
        # Move the figure down
        tetris.go_down()
        # Assert that the y-coordinate has increased by 1
        self.assertEqual(tetris.figure.y, initial_y + 1)

     # Test moving a Tetris figure sideways
    def test_tetris_go_side(self):
        tetris = Tetris(20, 10)
        tetris.figure = Tetramino(0, 0)
        # Store the initial x-coordinate
        initial_x = tetris.figure.x
        # Move the figure to the right (side=1)
        tetris.go_side(1)
         # Assert that the x-coordinate has increased by 1
        self.assertEqual(tetris.figure.x, initial_x + 1)
    
    # Test rotating a Tetris figure
    def test_tetris_rotate(self):
        tetris = Tetris(20, 10)
        tetris.figure = Tetramino(0, 0)
        # Store the initial rotation
        initial_rotation = tetris.figure.rotation
         # Rotate the figure
        tetris.rotate()
         # Assert that the rotation has changed as expected
        self.assertEqual(tetris.figure.rotation, (initial_rotation + 1) % len(tetris.figure.shape))
    
    # Test removing a line in Tetris and checking if it contains all zeros
    def test_tetris_remove_line(self):
        tetris = Tetris(20, 10)
        tetris.board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0] * 10 for _ in range(19)]
        tetris.remove_line()
    
        # Check if all rows, except the first one, contain zeros
        self.assertTrue(all(all(cell == 0 for cell in row) for row in tetris.board[1:]))

    # Test if the gameover flag is set when a Tetramino reaches the bottom
    def test_tetris_game_over(self):
        tetris = Tetris(20, 10)
        tetris.figure = Tetramino(0, 0)

         # Move the Tetramino down until it reaches the bottom
        while not tetris.gameover:
          tetris.go_down()
        # Check if the gameover flag is set
        self.assertTrue(tetris.gameover)
   
# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
