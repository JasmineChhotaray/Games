import pygame
import sys
from pygame.math import Vector2
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # all possible head positions
        self.head_up = pygame.image.load('images/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('images/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('images/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('images/head_left.png').convert_alpha()
		
        # all possible tail positions
        self.tail_up = pygame.image.load('images/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('images/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('images/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('images/tail_left.png').convert_alpha()

        # vertical and horizontal body position
        self.body_vertical = pygame.image.load('images/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('images/body_horizontal.png').convert_alpha()

        # all curved body parts
        self.body_tr = pygame.image.load('images/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('images/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('images/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('images/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('sound/Sound_crunch.wav')

    def draw_snake(self):
        # for block in self.body:
        #     # create a rect
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
        #     block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        #     # draw the rectangle
        #     pygame.draw.rect(screen, (183, 111, 122), block_rect)

        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # 1. We still need a rect for the positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # 2. What direction is the face heading
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:     # last item in self.body
                screen.blit(self.tail, block_rect)
            # Rest of the body
            else:
                # what is my previous block and next_block
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:  # if y parts are same, our block is horizontal
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    # checking our previous block and next block and seeing how they are related to our current block & what corner do we need
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

                # 3. Snake's head direction is not updating
            # else:
            #     pygame.draw.rect(screen, (150, 100, 100), block_rect)

        
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0): 
            self.head = self.head_right
        elif head_relation == Vector2(0, 1): 
            self.head = self.head_up
        elif head_relation == Vector2(0, -1): 
            self.head = self.head_down


    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): 
            self.tail = self.tail_down


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
       
       
class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # draw the rectangle
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # print('Snack')
            # re-position the fruit
            self.fruit.randomize()
            # another block to the snake
            self.snake.add_block()
            self.snake.play_crunch_sound()

        # randomize again if the fruit falls in the body of our snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # pygame.quit()
        # sys.exit()
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 6, apple_rect.height, )

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        # draw a frame around the box
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
# to start pygame
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('images/apple.png').convert_alpha()
game_font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)


# create an object from the class
# fruit = Fruit()
# snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 250)


main_game = Main()

while True:
    # draw all our elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)



    # screen.fill(pygame.Color('gold'))
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)  # 60 is the framerate i.e., how many times this while loop can run per second