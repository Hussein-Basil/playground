import pygame
from pygame.locals import *
import time, random

SIZE = 35

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load('Resources/apple.png').convert()
        self.image = pygame.transform.scale(self.image, (SIZE,SIZE))
        self.x = SIZE * random.randint(0,13)
        self.y = SIZE * random.randint(0,13)

    def draw_apple(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.update()

class Snake:
    def __init__(self, game):
        self.game = game
        
        self.length = 6
        self.x = [SIZE] * self.length
        self.y = [SIZE] * self.length

        self.block = pygame.image.load('Resources/ppt.png').convert()
        self.block = pygame.transform.scale(self.block, (SIZE,SIZE))
        self.draw_block()

        self.increasement_x = SIZE
        self.increasement_y = 0


    def draw_block(self):
        for i in range(self.length):
            self.game.surface.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.update()

    def move_up(self):
        self.increasement_y = -SIZE
        self.increasement_x = 0
    
    def move_down(self):
        self.increasement_y = SIZE
        self.increasement_x = 0
    
    def move_left(self):
        self.increasement_x = -SIZE
        self.increasement_y = 0
    
    def move_right(self):
        self.increasement_x = SIZE
        self.increasement_y = 0

    def always_move(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        self.x[0] += self.increasement_x
        self.y[0] += self.increasement_y
        
        self.draw_block()
        
    def add_tail(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Snake Game')

        pygame.mixer.init()
        self.play_background_music()

        self.running = True
        self.w, self.h = 1015, 805
        
        self.surface = pygame.display.set_mode((self.w, self.h))
        self.snake = Snake(self)
        self.apple = Apple(self.surface)

        self.direction = 'right'
        self.gameover = False
    
    def is_collosion(self, x1, y1, x2, y2):
        if x1 == x2:
            if y1 == y2:
                return True
        return False

    def play(self):
        self.render_background()
        self.snake.always_move()
        self.apple.draw_apple()
        self.display_score()

        # snake eats apple senario
        if self.is_collosion(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.add_tail()
            self.apple = Apple(self.surface)
            self.play_sound('eat')

        # snake crashes into itself
        for i in range(1,self.snake.length):
            if self.is_collosion(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                while self.running:
                    pygame.mixer.music.pause()
                    self.game_over()            
                    self.event_loop()
                self.running = False

    def reset(self):
        self.running = False
        self.gameover = False
        g = Game()
        g.run()
        
    # check collosion with borders
    def border(self):
        if self.snake.x[0] in [-35,1015] or self.snake.y[0] in [-35,805]:
            self.play_sound('crash')
            while self.running:
                pygame.mixer.music.pause()
                self.game_over()            
                self.event_loop()
            self.running = False

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE : self.running = False
                elif event.key == K_UP   : self.snake.move_up()   ; self.direction = 'up'
                elif event.key == K_DOWN : self.snake.move_down() ; self.direction = 'down'
                elif event.key == K_LEFT : self.snake.move_left() ; self.direction = 'left'
                elif event.key == K_RIGHT: self.snake.move_right(); self.direction = 'right'
                elif self.gameover and event.key == K_r : self.reset()
            elif event.type == QUIT:
                self.running = False
    
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length - 6}", True, (255,255,255))
        self.surface.blit(score, (self.w/2 - score.get_rect().width/2, 25))
        pygame.display.update()
    
    def game_over(self):
        self.gameover = True
        self.surface.fill((0,0,0))
        font = pygame.font.SysFont('arial', 30)
        text = font.render("Game Over", True, (255,255,255))
        text2 = font.render("Press R to try again", True, (255,255,255))
        self.surface.blit(text, (self.w/2 - text.get_rect().width/2, self.h/2 - text.get_rect().height/2))
        self.surface.blit(text2, (self.w/2 - text2.get_rect().width/2, self.h/2 - text.get_rect().height/2 + 75))
        self.display_score()
        pygame.display.update()

    def play_background_music(self):
        pygame.mixer.music.load('Resources/bg_music.mp3')
        pygame.mixer.music.play()

    def play_sound(self, sound_name):
        sound = pygame.mixer.Sound(f"Resources/{sound_name}.mp3")
        pygame.mixer.Sound.play(sound)
        
    def render_background(self):
        bg = pygame.image.load('Resources/bg.jpg').convert()
        self.surface.blit(bg, (0,0))

    def run(self):
        while self.running:
            self.event_loop()
            self.play()
            self.border()
            time.sleep(0.1)

g = Game()
g.run()