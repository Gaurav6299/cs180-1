import pygame

class Board:

	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.board = []
		for i in xrange(self.w):
			arr = []
			for j in xrange(self.h):
				arr.append(0)
			self.board.append(arr)
	
	def get(self, r, c):
		return self.board[r][c]
	
	def set(self, r, c, val):
		self.board[r][c] = val

	def draw(self, x_o=0, y_o=0, size=30, screen=None):
		y = y_o
		for i in range(self.h):
			x = x_o
			for j in range(self.w):
				pygame.draw.rect(screen,(0,0,0),(x, y, size, size), 1)
				x += size
			y += size
		
