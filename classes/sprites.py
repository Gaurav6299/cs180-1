import pygame
from pygame.locals import *
from base import Board

class BoardSprite(Board, pygame.sprite.Sprite):
	
	def __init__(self, w, h):
		Board.__init__(self, w, h)
		pygame.sprite.Sprite.__init__(self)
		self.cw = 30	#Cell width
		self.ch = 30	#Cell height
