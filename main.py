import os, sys
import pygame
from pygame.locals import *
from classes.base import Board
#import classes

grid = Board(24,16)
pygame.font.init()
#myfont = pygame.font.Font("loma", 15)
#print pygame.font.get_fonts()

class Game:

	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.bg = pygame.Surface((800, 600)) #temporary BG
		self.bg = self.bg.convert()
		self.bg.fill((255, 255, 255))
		
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False

			if event.type == MOUSEMOTION:
				print event.pos
				# render text
				#label = myfont.render(str(event.pos), 1, (255,255,0))
				#self.screen.blit(label, (100, 100))
  
	def start(self):
		while(self.running):
			self.clock.tick(60)
			self.checkEvents()
			
			self.screen.blit(self.bg, (0, 0))
			grid.draw(10,10,30,self.screen)
			pygame.display.update()
  
  
if __name__ == '__main__':	

	pygame.init()
	pygame.display.set_caption("Game Title")
	SCREEN = pygame.display.set_mode((1024, 768))
	#pygame.display.toggle_fullscreen()
	
	game = Game(SCREEN)
	game.start()





















