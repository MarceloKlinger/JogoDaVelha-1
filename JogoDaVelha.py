''' ===== ===== =====

Jogo da Velha com Inteligencia Artificial.
Tic Tac Toe with Artificial Intelligence.

Inteligencia Artificial - Algoritmo Logico
GitHub - https://github.com/dfop02/JogoDaVelha
By: Dfop02

===== ===== ===== '''

import os
import platform
import time
import random

class Game(object):
	def __init__(self):
		self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.player = 1
		self.gameover = False
		self.endgame = False
		self.move = 0

	def GetMove(self):
		self.move = int(input('\n\nOnde deseja jogar?\n'))

	def MakePlay(self):
		if self.move == 1:
			if self.board[0][0] == 0:
				if self.player == 1:
					self.board[0][0] = 1
				else:
					self.board[0][0] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 2:
			if self.board[0][1] == 0:
				if self.player == 1:
					self.board[0][1] = 1
				else:
					self.board[0][1] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 3:
			if self.board[0][2] == 0:
				if self.player == 1:
					self.board[0][2] = 1
				else:
					self.board[0][2] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 4:
			if self.board[1][0] == 0:
				if self.player == 1:
					self.board[1][0] = 1
				else:
					self.board[1][0] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 5:
			if self.board[1][1] == 0:
				if self.player == 1:
					self.board[1][1] = 1
				else:
					self.board[1][1] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 6:
			if self.board[1][2] == 0:
				if self.player == 1:
					self.board[1][2] = 1
				else:
					self.board[1][2] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 7:
			if self.board[2][0] == 0:
				if self.player == 1:
					self.board[2][0] = 1
				else:
					self.board[2][0] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move == 8:
			if self.board[2][1] == 0:
				if self.player == 1:
					self.board[2][1] = 1
				else:
					self.board[2][1] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'
		if self.move == 9:
			if self.board[2][2] == 0:
				if self.player == 1:
					self.board[2][2] = 1
				else:
					self.board[2][2] = 2
			else:
				self.move = 0
				print '\nEssa casa ja foi escolhida!\n'

		if self.move in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
			if self.player == 1:		
				self.player = 2
			else:
				self.player = 1
		time.sleep(1)

	def CheckGameOver(self, board, ShowWinner):
		# Lines
		if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'
		if board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
			self.endgame = True
			if ShowWinner:			
				print '\nParabens! Player X Venceu!\n'
		if board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
			self.endgame = True
			if ShowWinner:			
				print '\nParabens! Player O Venceu!\n'
		if board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'
		#Coluns
		if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'
		if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'
		if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nparabens! Player O Venceu!\n'
		#Diagonals
		if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'
		if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player O Venceu!\n'

		n = 0
		for linha in board:
			for coluna in linha:
				if coluna == 0:
					n += 1
		if n == 0:
			self.endgame = True
			if ShowWinner:
				print '\nEmpate!'

	def testWinMove(self, board, player, i, j):
		board[i][j] = player
		self.CheckGameOver(board, False)
		board[i][j] = 0
		if self.endgame:
			self.endgame = False
			return True
		return False

	def testFork(self, board, player, i, j):
		winMoves = 0
		copyboard = board
		copyboard[i][j] = player
		for m in range(len(copyboard)):
			for n in range(len(copyboard[0])):
				if copyboard[m][n] == 0 and self.testWinMove(copyboard, player, m, n):
					winMoves += 1
		copyboard[i][j] = 0
		return winMoves >= 2

	#IA 
	def iaMove(self, board):
		#Se o Computador for ganhar... Jogue nessa
		#If Computer will won... Play it
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.testWinMove(board, 2, i, j):
					return self.GetIaMove(i, j)

		#Se o Player for ganhar... Jogue nessa
		#If Player will won... Play it
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.testWinMove(board, 1, i, j):
					return self.GetIaMove(i, j)

		#Procurar forcas
		#Test any fork
		playerFork = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.testFork(board, 1, i, j):
					playerFork += 1
					iaMove = self.GetIaMove(i, j)
				if board[i][j] == 0 and self.testFork(board, 2, i, j):
					return self.GetIaMove(i, j)
		if playerFork == 1:
			return iaMove
		elif playerFork == 2:
			for i in range(len(board)):
				for j in range(len(board[0])):
					if board[i][j] == 0 and self.GetIaMove(i, j) in {2, 4, 6, 8}:
						return self.GetIaMove(i, j)

		#Se ninguem ganhou... Jogue nos cantos
		#If anyone will not won... Play a corner
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.GetIaMove(i, j) in {1, 3, 7, 9}:
					return self.GetIaMove(i, j)

		#Se ninguem ganhou e todos os cantos foram jgoados... Jogue no meio
		#If anyone will not won or all corner is played... Play mid
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.GetIaMove(i, j) in {5}:
					return self.GetIaMove(i, j)

		#Se ninguem ganhou, todos os cantos foram jgoados e o meio tambem... Jogue nos lados
		#If anyone will not won or all corner and mid is played... Play a side
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 0 and self.GetIaMove(i, j) in {2, 4, 6, 8}:
					return self.GetIaMove(i, j)

	def GetIaMove(self, linha, coluna):
		if linha == 0 and coluna == 0:
			return 1
		if linha == 0 and coluna == 1:
			return 2
		if linha == 0 and coluna == 2:
			return 3
		if linha == 1 and coluna == 0:
			return 4
		if linha == 1 and coluna == 1:
			return 5
		if linha == 1 and coluna == 2:
			return 6
		if linha == 2 and coluna == 0:
			return 7
		if linha == 2 and coluna == 1:
			return 8
		if linha == 2 and coluna == 2:
			return 9

	def ShowBoard(self):
		fakeboard = [['|___', '|___|', '___|'], ['|___', '|___|', '___|'], ['|___', '|___|', '___|']]

		if self.board[0][0] == 1:
			fakeboard[0][0] = '|_X_'
		if self.board[0][0] == 2:
			fakeboard[0][0] = '|_O_'

		if self.board[0][1] == 1:
			fakeboard[0][1] = '|_X_|'
		if self.board[0][1] == 2:
			fakeboard[0][1] = '|_O_|'

		if self.board[0][2] == 1:
			fakeboard[0][2] = '_X_|'
		if self.board[0][2] == 2:
			fakeboard[0][2] = '_O_|'

		if self.board[1][0] == 1:
			fakeboard[1][0] = '|_X_'
		if self.board[1][0] == 2:
			fakeboard[1][0] = '|_O_'

		if self.board[1][1] == 1:
			fakeboard[1][1] = '|_X_|'
		if self.board[1][1] == 2:
			fakeboard[1][1] = '|_O_|'

		if self.board[1][2] == 1:
			fakeboard[1][2] = '_X_|'
		if self.board[1][2] == 2:
			fakeboard[1][2] = '_O_|'

		if self.board[2][0] == 1:
			fakeboard[2][0] = '|_X_'
		if self.board[2][0] == 2:
			fakeboard[2][0] = '|_O_'

		if self.board[2][1] == 1:
			fakeboard[2][1] = '|_X_|'
		if self.board[2][1] == 2:
			fakeboard[2][1] = '|_O_|'

		if self.board[2][2] == 1:
			fakeboard[2][2] = '_X_|'
		if self.board[2][2] == 2:
			fakeboard[2][2] = '_O_|'

		print('\n'.join([''.join(['{:4}'.format(item) for item in linha]) for linha in fakeboard]))

	def ShowHowPlay(self):
		print '\n\nOnde Deseja Jogar?\n'
		exemple =  [['|_1_', '|_2_|', '_3_|'],
					['|_4_', '|_5_|', '_6_|'], 
					['|_7_', '|_8_|', '_9_|']]
		print('\n'.join([''.join(['{:4}'.format(item) for item in linha]) for linha in exemple]))

	def clearScreen(self):
		#Pega qual o sistema operacional usado
		#Get what's SO used
		so = platform.system()
		if so == 'Windows':
			os.system('cls') #Windowns Clear
		elif so == 'Linux':
			os.system('clear') #Linux Clear
		elif so == 'Darwin':
			os.system('clear') #Mac Clear

	def start_PvsP(self):
		self.player = random.randint(1, 2)
		while(not self.gameover):
			#os.system('cls')  #Windowns Clear
			os.system('clear') #Linux    Clear
			self.CheckGameOver(self.board, True)
			if self.endgame:
				self.gameover = True
			if not self.gameover:
				self.ShowBoard()
				self.ShowHowPlay()
				self.GetMove()
				self.MakePlay()
			else:
				self.ShowBoard()
				time.sleep(2)

	def start_PvsC(self):
		self.player = random.randint(1, 2)
		while(not self.gameover):
			self.clearScreen()
			self.CheckGameOver(self.board, True)
			if self.endgame:
				self.gameover = True
			if not self.gameover:
				self.ShowBoard()
				if self.player == 1:
					self.ShowHowPlay()
					self.GetMove()
					self.MakePlay()
				else:
					self.move = self.iaMove(self.board)
					self.MakePlay()
			else:
				self.ShowBoard()
				time.sleep(2)

if __name__ == '__main__':
	while(True):
		#os.system('cls')  #Windowns Clear
		os.system('clear') #Linux    Clear
		Jogo = Game()
		print 'Bem vindo ao Jogo da Velha! by: Diogo\n\n'
		resposta = int(input('Digite a opcao desejada:\n\n[1] Player vs Player\n[2] Player vs Computador\n[3] Sair\n'))
		if resposta == 1:
			Jogo.start_PvsP()
		if resposta == 2:
			Jogo.start_PvsC()
		if resposta == 3:
			break
		else:
			print 'Opcao invalida, tente novamente!'
