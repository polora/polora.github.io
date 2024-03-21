import pygame

pygame.init()

ecran = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test MOUSE")

image_noire = pygame.Surface((50,50))
image_noire.fill((0,0,0))

image_rouge = pygame.Surface((50,50))
image_rouge.fill((255,0,0))

image_rect = image_rouge.get_rect()
image_rect.x = 50
image_rect.y = 50

continuer = True

while continuer:
    ecran.fill((0,150,0))
    ecran.blit(image_rouge,(image_rect.x,image_rect.y))

    if pygame.mouse.get_pos()[0] > image_rect.left and pygame.mouse.get_pos()[0] < image_rect.right and pygame.mouse.get_pos()[1] < image_rect.bottom and pygame.mouse.get_pos()[1] > image_rect.top:
        ecran.blit(image_noire,(image_rect.x,image_rect.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    pygame.display.update()

pygame.quit()