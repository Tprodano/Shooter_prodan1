#Создай собственный Шутер!
from pygame import *
from random import *
font.init()
mixer.init()
#создай окно игры
window = display.set_mode((700,500))
#задай фон сцены
display.set_caption("Пин-понг")
background = transform.scale(image.load("pixil-frame-0 (1).png"),(700,500))
#создай 2 спрайта и размести их на сцене
clock = time.Clock()
FPS = 60
game = True
finish = False
#mixer.music.load('Фоновая музыка')
#mixer.music.play()
#faer = mixer.Sound('Звук отбивания')
#font = font.SysFont('Arial', 35)
#Функции-----------------------------------------------------------------------------
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect() #rect - прямоугольник
        self.rect.x = player_x #Координата х
        self.rect.y = player_y #Координата у
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 455:
            self.rect.y = 0
            self.rect.x = randint(50,650)

enemy = Enemy("pixil-frame-0 (2).png",150,0,4,50,45)
player = Player("pixil-frame-0.png",15,250,7,10,90)
player2 = Player("pixil-frame-0.png",685,250,7,10,90)
#win = font.render('You win!',True,(255,215,0))
#lous = font.render('You lose!',True,(255,215,0))

while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        #window.blit(win,(350,250))
        window.blit(background,(0,0))
        player.reset()
        player.update_1()
        player2.reset()
        player2.update_2()
        enemy.reset()
        enemy.update()
    display.update()