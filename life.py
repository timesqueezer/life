import pygame

pygame.inti()

RES = (800, 600)

screen = pygame.display.set_mode(RES)

class Cell:
	def __init__(posx, posy):
		self.alive = False
		self.posx = posx
		self.posy = posy
		self.next_status = False

	def check_neighbors():
		

	def get_position():
		return (self.posx, self.posy)

	
