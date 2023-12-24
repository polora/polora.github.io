import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade test"

class Fenetre(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CADET_BLUE)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

### main
window = Fenetre()
window.setup()
arcade.run()

