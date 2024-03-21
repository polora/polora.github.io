import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
FPS = 60

# Définition des couleurs et de la couleur de fond
YELLOW = (255,255,0)
BGCOLOR = YELLOW

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        # Initialiser les joysticks.
        pygame.joystick.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.done = False
        
        if pygame.joystick.get_count() != 0: 
            
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
                
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.done = True
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def events(self):
        # fermeture de la fenêtre à la l'aide de la croix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      
                self.closeWindow()
                

    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.screen.fill(BGCOLOR)
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()

    

# programme principal
game = Game()
game.new()
while not game.done:
    game.run()
print("Nombre de joystick branché : ", pygame.joystick.get_count())
print("Nom du joystick : ", game.joystick.get_name())
print("Nombre de trackballs : ", game.joystick.get_numballs())
print("Nombre de boutons : ", game.joystick.get_numbuttons())
print("Nombre de hats : ", game.joystick.get_numhats())
pygame.quit()
