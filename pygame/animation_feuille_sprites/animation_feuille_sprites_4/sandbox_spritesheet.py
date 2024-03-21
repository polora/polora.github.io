import pygame

pygame.init()

# fenêtre principale
screen = pygame.display.set_mode((960, 600))
pygame.display.set_caption("SandBOX")
clock = pygame.time.Clock()
running = True

# spritesheet & animation
IDLE_spritesheet = pygame.image.load("./assets/Idle.png").convert_alpha()
RUN_spritesheet = pygame.image.load("./assets/Run.png").convert_alpha()
sprites = []
sprites_flipped = []

rect = pygame.Rect(0,0,250,250)

def get_sprites(feuille_sprite, nombre_sprites, flipped):
    for x in range(nombre_sprites):
        temp_image = IDLE_spritesheet.subsurface(x * 250, 0, 250, 250)
        sprites.append(temp_image)
        temp_image_flipped = pygame.transform.flip(temp_image, True, False)
        sprites_flipped.append(temp_image_flipped)
    if flipped:
        return sprites
    elif not flipped:
        return sprites_flipped

# character
animationIndex = 0
animationSpeed = 0.1
direction = "RIGHT"

# mainloop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    elif keys[pygame.K_LEFT]:
        direction = "LEFT"

    screen.fill("DARKGREY")

    # animation 
    animationIndex += animationSpeed
    if animationIndex >= 8:
        animationIndex = 0

    if direction == "RIGHT":
        image = get_sprites(IDLE_spritesheet, 8, True)[int(animationIndex)]

    elif direction == "LEFT":
        image = get_sprites(IDLE_spritesheet, 8, False)[int(animationIndex)]

    screen.blit(image, (100,100))

    pygame.display.update()
    clock.tick(60)

pygame.quit()










"""


while running:

    # animate
    animationIndex += animationSpeed
    if animationIndex >= len(sprites):
        animationIndex = 0
    
    image = sprites[int(animationIndex)]
    screen.blit(image, (100,100))



pygame.quit()

"""