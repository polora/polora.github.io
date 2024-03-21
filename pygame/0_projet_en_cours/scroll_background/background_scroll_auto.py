import pygame

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
clock = pygame.time.Clock()

#Creating colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('AnimatedStreet.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.moving_speed = 5
         
      def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))

loop = True

background = Background()

while loop:
    # fermeture fenêtre
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            loop = False


    # Rafraîchissement
    background.update()
    background.render()
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()