''' ===== ===== ===== ===== ===== ===== ===== =====

Jogo da Velha com Inteligencia Artificial.
Tic Tac Toe with Artificial Intelligence.

Inteligencia Artificial - Algoritmo Logico
GitHub - https://github.com/dfop02/JogoDaVelha
By: Diogo Fernandes

===== ===== ===== ===== ===== ===== ===== ===== '''

import os
import platform
import time
import random

#Sempre alternar quem comeca jogando
#Always change who start playing
turn = 0

class Game(object):
	def __init__(self):
		self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.player = 1
		self.winner = 0
		self.gameover = False
		self.endgame = False
		self.move = 0

	def GetMove(self):
		while True:
			try:
				self.move = int(input('\n\nOnde deseja jogar?\n'))
				break
			except:
				print 'Somente numero sao aceitos!'

	def MakePlay(self):
		if self.move == 0:
			if self.player == 1:	
				self.gameover = True
				self.winner = 1
				print '\nParabens! Player O Desistiu!\n Entao o Player X Venceu!\n'
			else:
				self.gameover = True
				self.winner = 2
				print '\nParabens! Player X Desistiu!\n Entao o Player O Venceu!\n'
			time.sleep(1)

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
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'
		if board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2	
				print '\nParabens! Player O Venceu!\n'
		if board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'
		#Coluns
		if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'
		if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'
		if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nparabens! Player O Venceu!\n'
		#Diagonals
		if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'
		if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
			self.endgame = True
			if ShowWinner:
				self.winner = 1
				print '\nParabens! Player X Venceu!\n'
		if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
			self.endgame = True
			if ShowWinner:
				self.winner = 2
				print '\nParabens! Player O Venceu!\n'

		n = 0
		for linha in board:
			for coluna in linha:
				if coluna == 0:
					n += 1
		if n == 0:
			self.endgame = True
			if ShowWinner:
				self.winner = 3
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

		n = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] != 0:
					n += 1

		#Se ninguem ganhou e nao jogou nos cantos... Jogue nos cantos 
		#If anyone will not won and dont play at mid... Play a corner
		if n <= 1 and 1 not in {board[0][0], board[0][2], board[2][0], board[2][2]}:
			for i in range(len(board)):
				for j in range(len(board[0])):
					if board[i][j] == 0 and self.GetIaMove(i, j) in {1, 3, 7, 9}:
						return self.GetIaMove(i, j)

		elif n > 1 and 1 in {board[0][0], board[0][2], board[2][0], board[2][2]}:
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
		self.player = turno
		while(not self.gameover):
			self.clearScreen()
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
		self.player = turno
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


class Placar(object):
	def __init__(self):
		#Player vs Player
		self.pontos_p1 = 0
		self.pontos_p2 = 0
		self.empatePvsP = 0
		#Player vs Computer
		self.player = 0
		self.computer = 0
		self.empatePvsC = 0

	def getScore(self, Game, mode):
		if mode == 1:
			if Game.winner == 1:
				self.pontos_p1 += 1
			elif Game.winner == 2:
				self.pontos_p2 += 1
			elif Game.winner == 3:
				self.empatePvsP += 1
		else:
			if Game.winner == 1:
				self.player += 1
			elif Game.winner == 2:
				self.computer += 1
			elif Game.winner == 3:
				self.empatePvsC += 1

	def showScore(self):
		print 'Player 1  vs  Player 2\n'
		print 'O Player 1 (X) venceu ' + str(Pontuacao.pontos_p1) + ' vezes!'
		print 'O Player 2 (O) venceu ' + str(Pontuacao.pontos_p2) + ' vezes!'
		print 'O jogo terminou em empate ' + str(Pontuacao.empatePvsP) + ' vezes!'
		print '\nPlayer  vs  Computer\n'
		print 'O Player (X) venceu ' + str(Pontuacao.player) + ' vezes!'
		print 'O Computador (O) venceu ' + str(Pontuacao.computer) + ' vezes!'
		print 'O jogo terminou em empate ' + str(Pontuacao.empatePvsC) + ' vezes!'

if __name__ == '__main__':
	turno = random.randint(1, 2)
	Pontuacao = Placar()
	while(True):
		if turno == 1:
			turno = 2
		else:
			turno = 1
		Jogo = Game()
		while True:
			Jogo.clearScreen()
			print 'Bem vindo ao Jogo da Velha! by: Diogo Fernandes\n\n'
			try:
				resposta = int(input('Digite a opcao desejada:\n\n[1] Player vs Player\n[2] Player vs Computador\n[3] Ver Pontuacao\n[4] Sair\n\nOpcao: '))
				break
			except:
				print 'Opcao invalida, tente novamente!'
				time.sleep(2)
		if resposta == 1:
			Jogo.start_PvsP()
			Pontuacao.getScore(Jogo, 1)
		if resposta == 2:
			Jogo.start_PvsC()
			Pontuacao.getScore(Jogo, 2)
		if resposta == 3:
			Jogo.clearScreen()
			Pontuacao.showScore()
			raw_input('\nAperte ENTER para voltar ao menu...')
		if resposta == 4:
			break
		else:
			print 'Opcao invalida, tente novamente!'
			time.sleep(2)
