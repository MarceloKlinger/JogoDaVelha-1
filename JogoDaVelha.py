''' ===== ===== =====

Jogo da Velha com Inteligencia Artificial.

Artificial Intelligence - MiniMax Algorithm
GitHub - https://github.com/dfop02/study
Code Contributor - Diogo Fernandes

===== ===== ===== '''

import os
import time
import random

class Game(object):
	def __init__(self):
		self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.player = 1
		self.gameover = False
		self.endgame = False
		self.move = 0
		self.IA_move = dict()

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
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 2:
			if self.board[0][1] == 0:
				if self.player == 1:
					self.board[0][1] = 1
				else:
					self.board[0][1] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 3:
			if self.board[0][2] == 0:
				if self.player == 1:
					self.board[0][2] = 1
				else:
					self.board[0][2] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 4:
			if self.board[1][0] == 0:
				if self.player == 1:
					self.board[1][0] = 1
				else:
					self.board[1][0] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 5:
			if self.board[1][1] == 0:
				if self.player == 1:
					self.board[1][1] = 1
				else:
					self.board[1][1] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 6:
			if self.board[1][2] == 0:
				if self.player == 1:
					self.board[1][2] = 1
				else:
					self.board[1][2] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 7:
			if self.board[2][0] == 0:
				if self.player == 1:
					self.board[2][0] = 1
				else:
					self.board[2][0] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 8:
			if self.board[2][1] == 0:
				if self.player == 1:
					self.board[2][1] = 1
				else:
					self.board[2][1] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)
		if self.move == 9:
			if self.board[2][2] == 0:
				if self.player == 1:
					self.board[2][2] = 1
				else:
					self.board[2][2] = 2
			else:
				print '\nEssa casa ja foi escolhida!\n'
				time.sleep(1)

		if self.player == 1:		
			self.player = 2
		else:
			self.player = 1

	def CheckGameOver(self, board, ShowWinner):
		# Lines
		if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
			self.endgame = True
			if ShowWinner:
				print '\nParabens! Player X Venceu!\n'
		if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
			self.endgame = True
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

	#Loop Error in minimax
	def minimax(self, copyboard, depth, player):
		if depth != 0:
			self.CheckGameOver(copyboard, False)
			if self.endgame:
				self.endgame = False
				return self.score(depth, player)

		# Max
		if player == 1:
			MaxScore = 0

			for i in range(len(copyboard)):
				for j in range(len(copyboard[0])):
					if copyboard[i][j] == 0:
						copyboard[i][j] = 1
						
						CurrentScoreMax = self.minimax(copyboard, depth + 1, 2)

						if CurrentScoreMax > MaxScore:
							MaxScore = CurrentScoreMax
							self.IA_Move[MaxScore] = GetIaMove(self, i, j)

						copyboard[i][j] = 0

			return MaxScore
		# Min
		else:
			MinScore = 0

			for m in range(len(copyboard)):
				for n in range(len(copyboard[0])):
					if copyboard[m][n] == 0:
						copyboard[m][n] = 2

						CurrentScoreMin = self.minimax(copyboard, depth + 1, 1)

						if CurrentScoreMin < MinScore:
							MinScore = CurrentScoreMin
							self.IA_Move[MinScore] = GetIaMove(self, m, n)

						copyboard[m][n] = 0

			return MinScore		

	def score(self, depth, player):
		if player == 1:
		    return 10 - depth
		elif player == 2:
		    return depth - 10
		return 0

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

	def start_PvsP(self):
		self.player = random.randint(0, 2)
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
		self.player = random.randint(0, 2)
		while(not self.gameover):
			#os.system('cls')  #Windowns Clear
			os.system('clear') #Linux    Clear
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
					copyboard = self.board
					bestscore = self.minimax(copyboard, 0, self.player)
					for k, v in self.IA_move.iteritems():
						print 'Key: ' + k + ' Value: ' + v
						time.sleep(2)
#						if bestscore < v:
#							bestscore = v
#							self.move = k
#					self.MakePlay()
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
