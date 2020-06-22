import pygame
import os
import random
pygame.font.init()  # init font

GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
CYAN = (0, 240, 240)
RED = (200, 0, 5)
PURPLE = (155, 2, 238)
ORANGE = (240, 160, 7)
YELLOW = (245, 245, 0)
BLACK = (0, 0, 0)

cubeSize = 40
STAT_FONT = pygame.font.SysFont("comicsans", 50)

class NextShape:
	def __init__(self, game):
		game.nextShapeNum = random.randint(1,7)
		self.initShape(game.nextShapeNum, game)

	def initShape(self, num, game):
		if (len(game.nextShape) != 0):
			del game.nextShape[:]
		if (num == 1):
			game.nextShapeColor = CYAN
			game.nextShape.extend(([3, 0], [4, 0], [5, 0], [6, 0]))
		elif (num == 2):
			game.nextShapeColor = YELLOW
			game.nextShape.extend(([4, 0], [5, 0], [4, 1], [5, 1]))
		elif (num == 3):
			game.nextShapeColor = ORANGE
			game.nextShape.extend(([4, 0], [5, 0], [6, 0], [4, 1]))
		elif (num == 4):
			game.nextShapeColor = BLUE
			game.nextShape.extend(([4, 0], [5, 0], [6, 0], [6, 1]))
		elif (num == 5):
			game.nextShapeColor = PURPLE
			game.nextShape.extend(([4, 1], [5, 1], [6, 1], [5, 0]))
		elif (num == 6):
			game.nextShapeColor = RED
			game.nextShape.extend(([4, 0], [5, 0], [5, 1], [6, 1]))
		else:
			game.nextShapeColor = GREEN
			game.nextShape.extend(([6, 0], [5, 0], [5, 1], [4, 1]))
		for elem in game.nextShape:
			if elem in game.grid:
				game.gameOver = True

class Shape:
	def __init__(self, game, num):
		self.num = num
		self.color = (0, 0, 0)
		self.initShape(self.num, game)

	def initShape(self, num, game):
		if (len(game.newShape) != 0):
			del game.newShape[:]
		if (num == 1):
			game.newShapeColor = CYAN
			game.newShape.extend(([3, 0], [4, 0], [5, 0], [6, 0]))
		elif (num == 2):
			game.newShapeColor = YELLOW
			game.newShape.extend(([4, 0], [5, 0], [4, 1], [5, 1]))
		elif (num == 3):
			game.newShapeColor = ORANGE
			game.newShape.extend(([4, 0], [5, 0], [6, 0], [4, 1]))
		elif (num == 4):
			game.newShapeColor = BLUE
			game.newShape.extend(([4, 0], [5, 0], [6, 0], [6, 1]))
		elif (num == 5):
			game.newShapeColor = PURPLE
			game.newShape.extend(([4, 1], [5, 1], [6, 1], [5, 0]))
		elif (num == 6):
			game.newShapeColor = RED
			game.newShape.extend(([4, 0], [5, 0], [5, 1], [6, 1]))
		else:
			game.newShapeColor = GREEN
			game.newShape.extend(([6, 0], [5, 0], [5, 1], [4, 1]))
		for elem in game.newShape:
			if elem in game.grid:
				game.gameOver = True

	def rotatePiece(self, game, moves):
		touched = False
		moved = []
		moved.append([game.newShape[0][0] + moves[0], game.newShape[0][1] + moves[1]])
		moved.append([game.newShape[2][0] + moves[2], game.newShape[2][1] + moves[3]])
		moved.append([game.newShape[3][0] + moves[4], game.newShape[3][1] + moves[5]])
	
		for newPos in moved:
			if (newPos in game.grid or newPos[0] > 9 or newPos[0] < 0 or newPos[1] > 20 or newPos[1] < 0):
				touched = True
		if (not touched):
			game.newShape[0][0] = game.newShape[0][0] + moves[0]
			game.newShape[0][1] = game.newShape[0][1] + moves[1]
			game.newShape[2][0] = game.newShape[2][0] + moves[2]
			game.newShape[2][1] = game.newShape[2][1] + moves[3]
			game.newShape[3][0] = game.newShape[3][0] + moves[4]
			game.newShape[3][1] = game.newShape[3][1] + moves[5]

	def rotate(self, game):
		if (game.newShapeColor == CYAN):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, 1, 1, 2, 2])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, -1, 1, -2, 2])
				else:
					self.rotatePiece(game, [-1, 1, 1, -1, 2, -2])
			else:
				self.rotatePiece(game, [1, 1, -1, -1, -2, -2])

		elif (game.newShapeColor == ORANGE):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, 1, 1, -2, 0])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, -1, 1, 0, -2])
				else:
					self.rotatePiece(game, [-1, 1, 1, -1, 0, 2])
			else:
				self.rotatePiece(game, [1, 1, -1, -1, 2, 0])

		elif (game.newShapeColor == BLUE):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, 1, 1, 0, 2])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, -1, 1, -2, 0])
				else:
					self.rotatePiece(game, [-1, 1, 1, -1, 2, 0])
			else:
				self.rotatePiece(game, [1, 1, -1, -1, 0, -2])
		elif (game.newShapeColor == PURPLE):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, 1, 1, 1, -1])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, -1, 1, 1, 1])
				else:
					self.rotatePiece(game, [-1, 1, 1, -1, -1, -1])
			else:
				self.rotatePiece(game, [1, 1, -1, -1, -1, 1])
		elif (game.newShapeColor == RED):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, -1, 1, 0, 2])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, -1, -1, -2, 0])
				else:
					self.rotatePiece(game, [-1, 1, 1, 1, 2, 0])
			else:
				self.rotatePiece(game, [1, 1, 1, -1, 0, -2])
		elif (game.newShapeColor == GREEN):
			if (game.newShape[0][1] > game.newShape[1][1]):
				self.rotatePiece(game, [-1, -1, 1, -1, 2, 0])
			elif (game.newShape[0][1] == game.newShape[1][1]):
				if (game.newShape[0][0] < game.newShape[1][0]):
					self.rotatePiece(game, [1, -1, 1, 1, 0, 2])
				else:
					self.rotatePiece(game, [-1, 1, -1, -1, 0, -2])
			else:
				self.rotatePiece(game, [1, 1, -1, 1, -2, 0])
			

class Game:
	def __init__(self):
		self.width = 800
		self.height = 1400
		self.innerRect = (40, 40, 400, 800)
		self.innerRectNextPiece = (500, 40, 200, 150)
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.gameOver = False
		self.score = 0
		self.newShape = []
		self.newShapeColor = (0, 0, 0)
		self.nextShape = []
		self.nextShapeNum = 0
		self.nextShapeColor = (0, 0, 0)
		self.grid = []
		self.colors = [['' for i in range(10)] for j in range(20)]
		self.level = 1
		self.lines = 0
		self.fps = 2

	def draw(self):
		self.screen.fill((0, 0, 0))
		score_label = STAT_FONT.render("Score: " + str(self.score),1,(255,255,255))
		self.screen.blit(score_label, (520, 350))
		level_label = STAT_FONT.render("Level: " + str(self.level),1,(255,255,255))
		self.screen.blit(level_label, (520, 250))
		lines_label = STAT_FONT.render("Lines: " + str(self.lines),1,(255,255,255))
		self.screen.blit(lines_label, (520, 450))
		for item in self.newShape:
			pygame.draw.rect(self.screen, self.newShapeColor, (int(item[0] * 40 + 40), int(item[1]) * 40 + 40, 40, 40))
			pygame.draw.rect(self.screen, BLACK, (int(item[0] * 40 + 40), int(item[1]) * 40 + 40, 40, 40), 1)
		for item in self.nextShape:
				pygame.draw.rect(self.screen, self.nextShapeColor, (int(item[0] * 40 + 400), int(item[1]) * 40 + 70, 40, 40))
				pygame.draw.rect(self.screen, BLACK, (int(item[0] * 40 + 400), int(item[1]) * 40 + 70, 40, 40), 1)
		for item in self.grid:
			pygame.draw.rect(self.screen, (self.colors[item[1]][item[0]]), (int(item[0] * 40 + 40), int(item[1]) * 40 + 40, 40, 40))
			pygame.draw.rect(self.screen, BLACK, (int(item[0] * 40 + 40), int(item[1]) * 40 + 40, 40, 40), 1)
		pygame.draw.rect(self.screen, (0, 200, 0), self.innerRect, 3)
		if (not self.gameOver):
			pygame.draw.rect(self.screen, (0, 170, 0), self.innerRectNextPiece, 3)
		if (self.gameOver):
			gameOver_label = STAT_FONT.render("Game Over", 1,(255,0,0))
			self.screen.blit(gameOver_label, (350, 350))
		pygame.display.flip()

def checkCompletedLine(game):
	linesCompleted = 0
	i = 19
	while (i >= 0):
		found = 0
		for j in range(10):
			if ([j, i] in game.grid):
				found += 1
		if (found == 10):
			linesCompleted += 1
			for k in range(10):
				game.grid.remove([k, i])
				game.colors[i][k] = ''
				for l in range(i - 1, -1, -1):
					if ([k, l] in game.grid):
						game.grid.remove([k, l])
						game.grid.append([k, l + 1])
						game.colors[l + 1][k] = game.colors[l][k]

			i = i + 1
		else:
			i -= 1

	game.score += linesCompleted * 50 + 5
	game.lines += linesCompleted
	if (game.score / game.level > 100):
		game.level += 1
		game.fps += 1


def run():


	game = Game()
	NextShape(game)
	shape = Shape(game, random.randint(1,7))
	clock = pygame.time.Clock()
	
	while (not game.gameOver):

		clock.tick(game.fps)

		game.draw()

		reached = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quit()
				break
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					validMove = True
					for elem in game.newShape:
						if (elem[0] + 1 >= 10 or [elem[0] + 1, elem[1]] in game.grid):
							validMove = False
					if (validMove):
						for elem in game.newShape:
							elem[0] += 1
				if event.key == pygame.K_LEFT:
					validMove = True
					for elem in game.newShape:
						if (elem[0] - 1 < 0 or [elem[0] - 1, elem[1]] in game.grid):
							validMove = False
					if (validMove):
						for elem in game.newShape:
							elem[0] -= 1
				if event.key == pygame.K_UP:
					shape.rotate(game)
				if event.key == pygame.K_DOWN:
					forcedReach = False
					for elem in game.newShape:
						if (elem[1] + 1 == 20 or [elem[0], elem[1] + 1] in game.grid):
							forcedReach = True
					if (forcedReach == False):
						for elem in game.newShape:
							elem[1] += 1
				

		# Check if reaching already existing piece or if reaching end of board
		for elem in game.newShape:
			if (elem[1] + 1 == 20 or [elem[0], elem[1] + 1] in game.grid):
				reached = True
		# If haven't reached yet, go down one
		for elem in game.newShape:
			if (reached == False):
				elem[1] += 1
		# If reached, register the new shape as an now elem of the board and create a new shape
		if (reached == True):
			for elem in game.newShape:
				game.grid.append(elem)
				game.colors[elem[1]][elem[0]] = game.newShapeColor
			del game.newShape[:] 
			Shape(game, game.nextShapeNum)
			NextShape(game)
			checkCompletedLine(game)

		
	while (game.gameOver):
		game.draw()

if __name__ == '__main__':
	run()