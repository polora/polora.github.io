# coding:utf-8

### déplacement d'un objet avec commandes clavier


""" 
Améliorations à apporter :
    - vitesse de la balle  à incrémenter
    - passer à groupe de sprites
    - mode simple ou double player
    - coder le fonctionnement des josyticks
"""    

import pygame
from constantes import *
from class_raquette import *
from class_balle import *
from random import randrange

class Game(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
        pygame.display.set_caption("Pong perso")

        # chargement du fichier de bande son
        pygame.mixer.music.load('./music/jumpshot.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        # son rebond
        self.son = pygame.mixer.Sound("./music/beep8.wav")

        # variables utiles dans le jeu
        self.score_ordinateur = 0
        self.score_joueur = 0
        self.police = pygame.font.Font("./font/imagine_font.ttf", 60)
        self.continuer = True

        # permet le déplacement continu de la barre (sinon besoin de rappuyer plusieurs fois sur la touche
        pygame.key.set_repeat(1,20)
            
        # raquettes en position initiale
        self.raquette1 = Raquette(x1)
        # raquette2=Raquette(x2)

        # balle en position initiale
        self.balle=Balle()

        # boucle de jeu
        while self.continuer:

            # décor
            self.screen.fill(NOIR)
            pygame.draw.line(self.screen,BLANC,(400,0),(400,600))
            
            for event in pygame.event.get():    
                # sortie du programme
                if event.type==pygame.QUIT:
                    self.continuer=False
                # pour gagner du temps en phase de développpement
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        self.continuer=False
                
            # déplacement des objets
            self.raquette1.deplacement()
            self.balle.deplacement()
            
            # quand la balle touche la raquette
            if self.raquette1.touche_raquette(self.balle.position,self.balle.taille):
                self.son.play()
                self.balle.speed[0] =- self.balle.speed[0]

            # si la balle ne touche pas la raquette
            if self.balle.position.left < 0:
                self.balle.position = self.balle.position.move(60,0)
                self.score_ordinateur += 1        
            
            if self.raquette1.touche_raquette(self.balle.position,self.balle.taille):
                self.score_joueur += 1
            
            # blittage
            self.screen.blit(self.balle.image,self.balle.position)
            self.screen.blit(self.raquette1.image,self.raquette1.position)
            self.affichage_score_ordinateur = self.police.render(str(self.score_ordinateur), True, BLANC)
            self.screen.blit(self.affichage_score_ordinateur,(500,40))
            self.affichage_score_joueur = self.police.render(str(self.score_joueur), True, BLANC)
            self.screen.blit(self.affichage_score_joueur,(300,40))
            pygame.display.flip()    
            
            if self.score_joueur <= 3:
                pygame.time.wait(6)
            elif self.score_joueur <= 6 and self.score_joueur >3:
                pygame.time.wait(5)
            elif self.score_joueur > 6 and self.score_joueur<=10:
                pygame.time.wait(4)
            
            # sortie du jeu
            if self.score_ordinateur>=2:
                pygame.mixer.music.stop()        
                self.screen.fill(0)
                pygame.time.wait(500)
                self.perdu = police.render("GAME OVER", True, BLANC)
                self.screen.blit(self.perdu,((800 - self.perdu.get_width())/2,(600 - self.perdu.get_height())/2))
                pygame.display.flip()
                pygame.time.wait(5000)
                self.continuer = False

game = Game()
pygame.quit()

