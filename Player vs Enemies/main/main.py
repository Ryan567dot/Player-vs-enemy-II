import pygame 
  
color = (255,255,255) 
bg_color = (0,0,0) 
w = 300
h = 300

class Sprite(pygame.player.enemy):
    def __init__(self, color, h, w):
        super().__init__() 
  
        self.image = pygame.Surface([w, h]) 
        self.image.fill(bg_color) 
        self.image.set_colorkey(color) 
  
        pygame.draw(self.image,color, pygame.Rect(0, 0, w, h)) 
  
        self.rect = self.image.get_rect() 
        
mixer.intit()
mixer.music.load("lazer.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()