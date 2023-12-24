from pgsimple import *

# constantes

TILESIZE = 30
WGRID, HGRID = 10, 20
SCREENSIZE = WIDTH, HEIGHT = WGRID * TILESIZE, HGRID * TILESIZE
TITLE = "Titre de la fenêtre"
FPS = 60
BGCOLOR = 'black'
PLAYER_VEL = 5
MAP = [
    [0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

# main
game = Game(SCREENSIZE, TITLE, FPS, BGCOLOR)
player = Player(50, 50, game, TILESIZE, 'orange')
game.all_sprites.add(player)

game.draw_walls(MAP, TILESIZE, 'gray')

while game.running:
    # events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.move("R", PLAYER_VEL)
    elif keys[pygame.K_LEFT]:
        player.move("L", PLAYER_VEL)
    elif keys[pygame.K_DOWN]:
        player.move("D", PLAYER_VEL)
    elif keys[pygame.K_UP]:
        player.move("U", PLAYER_VEL)

    game.draw()
    game.update()
    game.clock.tick(FPS)

pygame.quit()