from pygame import *

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс главного игрока
class Player(GameSprite):

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (win_height - 80):
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (win_height - 80):
            self.rect.y += self.speed

back_color = (200, 255, 255) # цвет фона
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back_color)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)

ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 0)
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
win1 = font.render('PLAYER 1 WIN!', True, (180, 0, 0))
win2 = font.render('PLAYER 2 WIN!', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back_color)
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if (ball.rect.y < 0) or (ball.rect.y > win_height - 50):
            speed_y *= -1

        if (sprite.collide_rect(racket1, ball)) or (sprite.collide_rect(racket2, ball)):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True


        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)
