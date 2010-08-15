#!/usr/bin/env python

import pygame

pygame.init()

RES = (800, 600)


class Cell:
	def __init__(posx, posy):
		self.alive = False
		self.posx = posx
		self.posy = posy
		self.next_status = False

	def check_neighbors():
		nb_alive = 0

		# Can be improved easily by solving this by a for loop

		if neighbors[self.posx-1, self.posy-1]:
			nb_alive += 1
		if neighbors[self.posx, self.posy-1]:
			nb_alive += 1
		if neighbors[self.posx+1, self.posy-1]:
			nb_alive += 1
		if neighbors[self.posx-1, self.posy+1]:
			nb_alive += 1
		if neighbors[self.posx, self.posy+1]:
			nb_alive += 1
		if neighbors[self.posx+1, self.posy]:
			nb_alive += 1
		if neighbors[self.posx+1, self.posy+1]:
			nb_alive += 1
		if neighbors[self.posx-1, self.posy]:
			nb_alive += 1


		if nb_alive < 2:
			self.next_status = False
		elif nb_alive >= 2 and nb_alive =< 4:
			self.next_status = True
		elif nb_alive == 3:
			self.next_status = True
		elif nb_alive > 4:
			self.next_status = False


	def get_position():
		return (self.posx, self.posy)

	def aging():
		if self.next_status == False:
			self.alive = False

class Game:
	def __init__(self, res):
		self.screen = pygame.display.set_mode(res)
		self.cells = []


	def add_cell(self, posx, posy):
		self.cells


if __name__ == "__main__":
	game = Game(RES)

