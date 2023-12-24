"""
Platformer Game
"""
import arcade

# Constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"


class MyGame(arcade.Window):
    """
    Classe principale qui gère le jeu
    """

    def __init__(self):

        # Appel de la classe parent et initiation de la fenêtre
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Définition de la couleur de fond de la fenêtre
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Configuration/initialisation du jeu ici. Appeler cette fonction pour 
            relancer le jeu."""
        pass

    def on_draw(self):
        """Gère tout ce qui s'affiche à l'écran"""

        self.clear()
        # Le code pour dessiner ce qui apparaît sur l'écran se met ici


def main():
    """Fonctionprincipale"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()