import pygame
import random

pygame.init()
SCREEN = WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

CELLSIZE = 20
ROWS = (HEIGHT - 120) // CELLSIZE
COLS = WIDTH // CELLSIZE

clock = pygame.time.Clock()
FPS = 24

BLACK = (21, 24, 29)
BLUE = (31, 25, 76)
RED = (252, 91, 122)
WHITE = (255, 255, 255)

img1 = pygame.image.load('images/photo_6199537352360180034_m.jpg')
img2 = pygame.image.load('images/photo_6199537352360180035_m.jpg')
img3 = pygame.image.load('images/photo_6199537352360180037_m.jpg')
img4 = pygame.image.load('images/photo_6199537352360180038_m.jpg')

Assets = {
    1: img1,
    2: img2,
    3: img3,
    4: img4
}

font = pygame.font.Font('fonts/Alternity-8w7J.ttf', 50)
font2 = pygame.font.SysFont('cursive', 25)

class Tetramino:
    FIGURES = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }

    TYPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(self.TYPES)
        self.shape = self.FIGURES[self.type]
        self.color = random.randint(1, 4)
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

class Tetris:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.score = 0
        self.board = [[0 for j in range(cols)] for i in range(rows)]
        self.next = None
        self.gameover = False
        self.new_figure()

    def new_figure(self):
        if not self.next:
            self.next = Tetramino(18, 0)
        self.figure = self.next
        self.next = Tetramino(18, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.rows - 1 or \
                       j + self.figure.x > self.cols - 1 or \
                       j + self.figure.x < 0 or \
                       self.board[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def remove_line(self):
        rerun = False
        for y in range(self.rows - 1, 0, -1):
            is_full = True
            for x in range(0, self.cols):
                if self.board[y][x] == 0:
                    is_full = False
            if is_full:
                del self.board[y]
                self.board.insert(0, [0 for i in range(self.cols)])
                self.score += 1
                rerun = True

        if rerun:
            self.remove_line()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.board[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.remove_line()
        self.new_figure()
        if self.intersects():
            self.gameover = True

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def go_side(self, dx):
        self.figure.x += dx
        if self.intersects():
            self.figure.x -= dx

    def rotate(self):
        rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = rotation

# Initialize variables
counter = 0
move_down = False
can_move = True

# Initialize the highest score
try:
    with open("highscore.txt", "r") as file:
        highest_score = int(file.read())
except FileNotFoundError:
    highest_score = 0

current_score = 0  # Initialize the current score

# Create a new state variable to manage the game state
game_state = "home"  # Initially, set the game state to the home screen

# Create buttons for the home screen
start_button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
quit_button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 80, WIDTH // 2, 50)

tetris = Tetris(ROWS, COLS)

running = True
while running:
    if game_state == "home":
        # Display the home screen
        win.fill(BLACK)
        # Draw buttons
        pygame.draw.rect(win, BLUE, start_button_rect)
        pygame.draw.rect(win, BLUE, quit_button_rect)
        # Add text for buttons
        start_text = font2.render('Start', True, WHITE)
        quit_text = font2.render('Quit', True, WHITE)
        win.blit(start_text, (start_button_rect.centerx - start_text.get_width() / 2, start_button_rect.centery - start_text.get_height() / 2))
        win.blit(quit_text, (quit_button_rect.centerx - quit_text.get_width() / 2, quit_button_rect.centery - quit_text.get_height() / 2))

        # Display the highest score and current score
        highscore_text = font2.render(f'Highest Score: {highest_score}', True, WHITE)
        win.blit(highscore_text, (WIDTH // 2 - highscore_text.get_width() / 2, HEIGHT // 2 - 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game_state = "playing"
                    tetris = Tetris(ROWS, COLS)  # Start a new game
                    current_score = 0  # Reset the current score
                elif quit_button_rect.collidepoint(event.pos):
                    running = False

        pygame.display.update()
    elif game_state == "playing":
        win.fill(BLACK)

        counter += 1
        if counter >= 10000:
            counter = 0

        if can_move:
            if counter % (FPS // 2) == 0 or move_down:
                if not tetris.gameover:
                    tetris.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if can_move and not tetris.gameover:
                    if event.key == pygame.K_LEFT:
                        tetris.go_side(-1)

                    if event.key == pygame.K_RIGHT:
                        tetris.go_side(1)

                    if event.key == pygame.K_UP:
                        tetris.rotate()

                    if event.key == pygame.K_DOWN:
                        move_down = True

                    if event.key == pygame.K_SPACE:
                        tetris.go_space()

                if event.key == pygame.K_r:
                    tetris = Tetris(ROWS, COLS)
                    current_score = 0  # Reset the current score

                if event.key == pygame.K_p:
                    can_move = not can_move

                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    move_down = False

        for x in range(ROWS):
            for y in range(COLS):
                if tetris.board[x][y] > 0:
                    val = tetris.board[x][y]
                    img = Assets[val]
                    win.blit(img, (y * CELLSIZE, x * CELLSIZE))
                    pygame.draw.rect(win, WHITE, (y * CELLSIZE, x * CELLSIZE, CELLSIZE, CELLSIZE), 1)

        if tetris.figure:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in tetris.figure.image():
                        img = Assets[tetris.figure.color]
                        x = CELLSIZE * (tetris.figure.x + j)
                        y = CELLSIZE * (tetris.figure.y + i)
                        win.blit(img, (x, y))
                        pygame.draw.rect(win, WHITE, (x, y, CELLSIZE, CELLSIZE), 1)

        if tetris.gameover:
            rect = pygame.Rect((50, 140, WIDTH - 100, HEIGHT - 350))
            pygame.draw.rect(win, BLACK, rect)
            pygame.draw.rect(win, RED, rect, 2)

            over = font2.render('Game Over', True, WHITE)
            msg1 = font2.render('Press r to restart', True, RED)
            msg2 = font2.render('Press q to quit', True, RED)

            win.blit(over, (rect.centerx - over.get_width() / 2, rect.y + 20))
            win.blit(msg1, (rect.centerx - msg1.get_width() / 2, rect.y + 80))
            win.blit(msg2, (rect.centerx - msg2.get_width() / 2, rect.y + 110))

            # Update the highest score if needed
            if current_score > highest_score:
                highest_score = current_score
                with open("highscore.txt", "w") as file:
                    file.write(str(highest_score))

        pygame.draw.rect(win, BLUE, (0, HEIGHT - 120, WIDTH, 120))
        if tetris.next:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in tetris.next.image():
                        img = Assets[tetris.next.color]
                        x = CELLSIZE * (tetris.next.x + j - 4)
                        y = HEIGHT - 100 + CELLSIZE * (tetris.next.y + i)
                        win.blit(img, (x, y))

        pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT - 120), 2)

        # Update and display the current score during the game
        current_score_text = font2.render(f'Score: {current_score}', True, WHITE)
        win.blit(current_score_text, (20, HEIGHT - 80))

        clock.tick(FPS)
        pygame.display.update()

pygame.quit()
