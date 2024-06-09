import pygame

pygame.init()

# constantes
WIDTH, HEIGHT = 960, 600

# fenêtre principale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SandBOX")
clock = pygame.time.Clock()
running = True

# spritesheet & animation
IDLE_spritesheet = pygame.image.load("./assets/Idle.png").convert_alpha()
RUN_spritesheet = pygame.image.load("./assets/Run.png").convert_alpha()
ATTACK_spritesheet = pygame.image.load("./assets/Attack1.png")

def get_sprites(feuille_sprite, nombre_sprites, flipped):
    sprites = []
    sprites_flipped = []
    for x in range(nombre_sprites):
        temp_image = feuille_sprite.subsurface(x * 250, 0, 250, 250)
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
pos_x = 100
pos_y = 100
velocity = 8
statut ="IDLE"

# mainloop
while running:

    statut = "IDLE"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and pos_x < WIDTH - 170:
        direction = "RIGHT"
        statut = "RUN"
        pos_x += velocity
    elif keys[pygame.K_LEFT] and pos_x > - 80:
        direction = "LEFT"
        statut = "RUN"
        pos_x -= velocity
    elif keys[pygame.K_SPACE]:
        statut = "ATTACK"

    screen.fill("DARKGREY")

    # animation
    animationIndex += animationSpeed
    if animationIndex >= 8:
        animationIndex = 0

    if direction == "RIGHT":
        if statut == "IDLE":
            image = get_sprites(IDLE_spritesheet, 8, True)[int(animationIndex)]
        elif statut == "RUN":
            image = get_sprites(RUN_spritesheet, 8, True)[int(animationIndex)]
        elif statut == "ATTACK":
            image = get_sprites(ATTACK_spritesheet, 8, True)[int(animationIndex)]
    elif direction == "LEFT":
        if statut == "IDLE":
            image = get_sprites(IDLE_spritesheet, 8, False)[int(animationIndex)]
        elif statut == "RUN":
            image = get_sprites(RUN_spritesheet, 8, False)[int(animationIndex)]
        elif statut == "ATTACK":
            image = get_sprites(ATTACK_spritesheet, 8, False)[int(animationIndex)]

    screen.blit(image, (pos_x, pos_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()