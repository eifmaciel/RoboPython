# coding: utf-8

import sys, pygame, os
import random

pygame.init()

score = [0,0]
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
black = 0,0,0
WHITE = 255, 255, 255

class Bomba(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("images/bomba.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def kill_bomba(self):
        posx = random.randint(10,550)
        posy = random.randint(10,350)
        self.rect.centerx = posx
        self.rect.centery = posy

class Robo(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.init_pos = startpos
        self.image, self.rect = load_image("images/robo.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def mov_right(self):
        if self.rect.centerx < 570:
            self.rect.centerx += 10

    def mov_left(self):
        if self.rect.centerx > 30:
            self.rect.centerx -= 10

    def mov_down(self):
        if self.rect.centery < 350:
            self.rect.centery += 10
        
    def mov_up(self):
        if self.rect.centery > 0:
            self.rect.centery -= 10

def load_image(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image: ", fullname
        raise SystemExit, message
    return image, image.get_rect()

def draw_bomba(bomba):
    screen.blit(bomba.image, bomba.rect)
    pygame.display.flip()

def draw_robo(robo):
    if bomba.rect.colliderect(robo.rect):
        bomba.kill_bomba()
    screen.blit(robo.image, robo.rect)
    pygame.display.flip()

def main():
   
    robo = Robo([width/2,height/2])
    pygame.display.set_caption("Robo")
    clock = pygame.time.Clock()
    bomba = Bomba([100,100])

    screen.fill(black)
    done = True
    draw_robo(robo)
    draw_bomba(bomba)
    # import ipdb; ipdb.set_trace();
    while done==True:
        for event in pygame.event.get():
            pass
        
        # key_pressed = pygame.key.get_pressed()
        # if key_pressed[pygame.K_UP]:
        #     robo.mov_up()
        # elif key_pressed[pygame.K_DOWN]:
        #     robo.mov_down()        
        # elif key_pressed[pygame.K_a]:
        #     robo.mov_left()
        # elif key_pressed[pygame.K_z]:
        #     robo.mov_right()     
       
        screen.fill(black)
        draw_robo(robo)
        draw_bomba(bomba)
        clock.tick(20)
        # cc =raw_input()
        # done = False

if __name__ == "__main__":
    main()
