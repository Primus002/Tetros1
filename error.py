from pygame import *
window = display.set_mode((1000, 700))
display.set_caption('Danger space')
clock = time.Clock()
fon = transform.scale(image.load('green.jpg'),(1000,700))
font.init()
font = font.SysFont('Arial',35)
class igroki(sprite.Sprite):
    def __init__(self,igrok_image,igrok_x,igrok_y,size_x,size_y,igrok_step):
        super().__init__()
        self.image = transform.scale(image.load(igrok_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = igrok_x
        self.rect.y = igrok_y
        self.step = igrok_step
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class player(igroki):
    def control_1(self):
        buttons = key.get_pressed()
        if buttons[K_w] and self.rect.y>0:
            self.rect.y-= self.step
        if buttons[K_s] and self.rect.y<920:
            self.rect.y+= self.step
    def control_2(self):
        buttons = key.get_pressed()
        if buttons[K_UP] and self.rect.y>0:
            self.rect.y-= self.step
        if buttons[K_DOWN] and self.rect.y<920:
            self.rect.y+= self.step
game = True
finish = False
clock = time.Clock()
igr_1 = player('racetca.png',20,300,20,100,19)
igr_2 = player('racetca.png',900,300,80,200,19)
boll = player('ball.png',500,300,40,50,0)
lose_1 = font.render('Проиграл 1-ый игрок',True,(255,255,255))
lose_2 = font.render('Проиграл 2-ой игрок',True,(255,255,255))
boll_speed_x = 12
boll_speed_y = 12
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(fon,(0,0))
        igr_1.reset()
        igr_2.reset()
        boll.reset()
        igr_1.control_1()
        igr_2.control_2()
        boll.rect.x -= boll_speed_x
        boll.rect.y += boll_speed_y
        if boll.rect.y <0 or boll.rect.y >650:
            boll_speed_y *= -1
        if boll.rect.x < 0:
            finish = True
            window.blit(lose_1,(400,300))
        if boll.rect.x > 1000:
            finish = True
            window.blit(lose_2,(400,300))
        if sprite.collide_rect(igr_1,boll) or sprite.collide_rect(igr_2,boll):
            boll_speed_y *= 1
            boll_speed_x *= -1
    display.update()
    clock.tick(60)