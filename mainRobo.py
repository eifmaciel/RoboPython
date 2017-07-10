# coding: utf-8

import sys, pygame, os
import random
import sys, traceback

pygame.init()

score = [0,0]
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
black = 0,0,0
WHITE = 255, 255, 255
DEVICE_NAME = "/dev/robo"
MAX_MOV = 10

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
        if self.rect.centery > 20:
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

def draw_robo(robo, bomba):
    if bomba.rect.colliderect(robo.rect):
        bomba.kill_bomba()
    screen.blit(robo.image, robo.rect)
    pygame.display.flip()

def readDriver():
    try:
        file = open(DEVICE_NAME, 'r')

        if file > 0:
            word = file.read()
            file.close()
        return word
    except:
        print "Problemas no acesso ao Driver."
        print traceback.print_exc(file=sys.stdout)

def main():

    robo = Robo([width/2,height/2])
    pygame.display.set_caption("Robo")
    clock = pygame.time.Clock()
    bomba = Bomba([100,100])
    up = 0
    down = 0
    left = 0
    right = 0

    screen.fill(black)
    done = True
    draw_robo(robo, bomba)
    draw_bomba(bomba)
    # import ipdb; ipdb.set_trace();
    while done==True:
        for event in pygame.event.get():
            pass
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break

        key_pressed = readDriver()
        #key_pressed = pygame.key.get_pressed()
        if key_pressed == 'u':
            if up < MAX_MOV:
                robo.mov_up()
                up += 1
        elif key_pressed == 'd':
            if down < MAX_MOV:
                robo.mov_down()
                down += 1
        elif key_pressed == 'l':
            if left < MAX_MOV:
                robo.mov_left()
                left += 1
        elif key_pressed == 'r':
            if right < MAX_MOV:
                robo.mov_right()
                right += 1
        screen.fill(black)
        draw_robo(robo, bomba)
        draw_bomba(bomba)
        clock.tick(60)
        # cc =raw_input()
        # done = False

if __name__ == "__main__":
    main()
