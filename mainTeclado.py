# coding: utf-8

import sys, pygame, os
pygame.init()
import driver

score = [0,0]
size = width, height = 250, 250
screen = pygame.display.set_mode(size)
black = 0,0,0
WHITE = 255, 255, 255

class ArowUP(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3,3]
        self.image, self.rect = load_image("images/up.png")
        self.rect.centerx = (width/2)
        self.rect.centery = 50

class ArowDown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3,3]
        self.image, self.rect = load_image("images/down.jpeg")
        self.rect.centerx = (width/2)
        self.rect.centery = height - 50

class Arowleft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3,3]
        self.image, self.rect = load_image("images/left.jpeg")
        self.rect.centerx = 50
        self.rect.centery = (height/2) - 10

class ArowRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3,3]
        self.image, self.rect = load_image("images/right.jpeg")
        self.rect.centerx = width - 50
        self.rect.centery = (height/2) - 10

def load_image(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image: ", fullname
        raise SystemExit, message
    return image, image.get_rect()

def main():
   
    left = Arowleft()
    right = ArowRight()
    down = ArowDown()
    up = ArowUP()
    pygame.display.set_caption("Teclado")
    clock = pygame.time.Clock()

    screen.fill(WHITE)
    screen.blit(left.image, left.rect)
    screen.blit(right.image, right.rect)
    screen.blit(down.image, down.rect)
    screen.blit(up.image, up.rect)
    pygame.display.flip()
    done = True

    while done==True:
        for event in pygame.event.get():
            pass
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            Driver.writeDriver('u')
        elif key_pressed[pygame.K_DOWN]:
            Driver.writeDriver('d')        
        elif key_pressed[pygame.K_LEFT]:
            Driver.writeDriver('l')
        elif key_pressed[pygame.K_RIGHT]:
            Driver.writeDriver('r')    
             
       
        clock.tick(20)
        # cc =raw_input()
        # done = False

if __name__ == "__main__":
    main()
