import pygame, sys, time
from JogoDaVelha import Game, Placar
import random
from pygame.locals import *

pygame.init()

tela_width = 600
tela_height = 400

#Medidas do desenho do jogo
lado = 400
parte = lado/4

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

gameTela = pygame.display.set_mode((tela_width ,tela_height))
pygame.display.set_caption('Jogo da Velha')
clock = pygame.time.Clock()
FPS = 30
gameTela.fill(white)

def mensagem_tela(text):
    simpleText = pygame.font.Font('freesansbold.ttf',32)
    TextSurf, TextRect = text_objects(text, simpleText)
    TextRect.center = ((tela_width/2),((tela_height/2)+150))
    gameTela.blit(TextSurf, TextRect)

def desenha_X(position):
	x, y = 150, 25
	#lado = 400
	#parte = lado/4
	if position == 1:
		pygame.draw.line(gameTela, red, [x + 5, y], [x + parte - 10, y + parte - 5], 10)
		pygame.draw.line(gameTela, red, [x + 5, y + parte - 5], [x + parte - 10, y], 10)
	if position == 2:
		pygame.draw.line(gameTela, red, [x + parte + 10, y], [x + 2*parte - 10, y + parte - 5], 10)
		pygame.draw.line(gameTela, red, [x + parte + 10, y + parte - 5], [x + 2*parte - 10, y], 10)
	if position == 3:
		pygame.draw.line(gameTela, red, [x + 2*parte + 10, y], [x + 3*parte - 5, y + parte - 5], 10)
		pygame.draw.line(gameTela, red, [x + 2*parte + 10, y + parte - 5], [x + 3*parte - 5, y], 10)
	if position == 4:
		pygame.draw.line(gameTela, red, [x + 5, y + parte], [x + parte - 10, y + 2*parte - 5], 10)
		pygame.draw.line(gameTela, red, [x + 5, y + 2*parte - 5], [x + parte - 5, y + parte], 10)
	if position == 5:
		pygame.draw.line(gameTela, red, [x + parte + 5, y + parte], [x + 2*parte - 5, y + 2*parte], 10)
		pygame.draw.line(gameTela, red, [x + parte + 5, y + 2*parte], [x + 2*parte - 5, y + parte], 10)
	if position == 6:
		pygame.draw.line(gameTela, red, [x + 2*parte + 5, y + parte], [x + 3*parte - 5, y + 2*parte - 5], 10)
		pygame.draw.line(gameTela, red, [x + 2*parte + 10, y + 2*parte - 5], [x + 3*parte - 5, y + parte + 5], 10)
	if position == 7:
		pygame.draw.line(gameTela, red, [x + 5, y + 2*parte + 5], [x + parte - 10, y + 3*parte], 10)
		pygame.draw.line(gameTela, red, [x + 5, y + 3*parte], [x + parte - 5, y + 2*parte], 10)
	if position == 8:
		pygame.draw.line(gameTela, red, [x + parte + 5, y + 2*parte], [x + 2*parte - 10, y + 3*parte], 10)
		pygame.draw.line(gameTela, red, [x + parte + 10, y + 3*parte], [x + 2*parte - 10, y + 2*parte + 5], 10)
	if position == 9:
		pygame.draw.line(gameTela, red, [x + 2*parte + 5, y + 2*parte], [x + 3*parte - 5, y + 3*parte], 10)
		pygame.draw.line(gameTela, red, [x + 2*parte + 10, y + 3*parte], [x + 3*parte - 5, y + 2*parte + 5], 10)

def desenha_O(position):
	x, y = 150, 25
	dif = 50

	if position == 1:
		pygame.draw.circle(gameTela, blue, [x + dif, y + dif], 45, 10)
	if position == 2:
		pygame.draw.circle(gameTela, blue, [x + parte + dif, y + dif], 45, 10)
	if position == 3:
		pygame.draw.circle(gameTela, blue, [x + 2*parte + dif, y + dif], 45, 10)
	if position == 4:
		pygame.draw.circle(gameTela, blue, [x + dif, y + parte + dif], 45, 10)
	if position == 5:
		pygame.draw.circle(gameTela, blue, [x + parte + dif, y + parte + dif], 45, 10)
	if position == 6:
		pygame.draw.circle(gameTela, blue, [x + 2*parte + dif, y + parte + dif], 45, 10)
	if position == 7:
		pygame.draw.circle(gameTela, blue, [x + dif, y + 2*parte + dif], 45, 10)
	if position == 8:
		pygame.draw.circle(gameTela, blue, [x + parte + dif, y + 2*parte + dif], 45, 10)
	if position == 9:
		pygame.draw.circle(gameTela, blue, [x + 2*parte + dif, y + 2*parte + dif], 45, 10)

def desenha_jogo():
	x, y = -50, 75

	pygame.draw.line(gameTela, blue, [parte - x, 2*parte - y], [4*parte - x, 2*parte - y], 10)
	pygame.draw.line(gameTela, blue, [parte - x, 3*parte - y], [4*parte - x, 3*parte - y], 10)

	pygame.draw.line(gameTela, blue, [2*parte - x, parte - y], [2*parte - x, 4*parte - y], 10)
	pygame.draw.line(gameTela, blue, [3*parte - x, parte - y], [3*parte - x, 4*parte - y], 10)

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def game_intro():
	largeText = pygame.font.Font('freesansbold.ttf', 60)
	TextSurf, TextRect = text_objects("Jogo da Velha", largeText)
	TextRect.center = ((tela_width/2),(tela_height/4))
	gameTela.blit(TextSurf, TextRect)

	simpleText = pygame.font.Font('freesansbold.ttf', 30)
	options = ['Player vs Player', 'Player vs Computer', 'Pontuacao', 'Sair']
	x, y = 190, 175
	for i in range(len(options)):
		option = simpleText.render(options[i], True, black)
		gameTela.blit(option, (x, y))
		y += 50
	pygame.draw.rect(gameTela, black, (180, 175, 250, 40), 5)
	pygame.draw.rect(gameTela, black, (180, 225, 300, 40), 5)
	pygame.draw.rect(gameTela, black, (180, 275, 170, 40), 5)
	pygame.draw.rect(gameTela, black, (180, 325, 80, 40), 5)

def faz_Jogada(posicao, turno, Jogo):
	Jogo.move = posicao
	Jogo.MakePlay()

	if turno == 1:
		desenha_X(posicao)
	else:
		desenha_O(posicao)

	if turno == 1:
		turno = 2
	else:
		turno = 1

	return turno

def start_PvsP(Jogo):
	jogo = True
	turno = random.randint(1, 2)

	while jogo:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1 or event.key == pygame.K_KP1:
						turno = faz_Jogada(1, turno, Jogo)
				elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
						turno = faz_Jogada(2, turno, Jogo)
				elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
						turno = faz_Jogada(3, turno, Jogo)
				elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
						turno = faz_Jogada(4, turno, Jogo)
				elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
						turno = faz_Jogada(5, turno, Jogo)
				elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
						turno = faz_Jogada(6, turno, Jogo)
				elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
						turno = faz_Jogada(7, turno, Jogo)
				elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
						turno = faz_Jogada(8, turno, Jogo)
				elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
						turno = faz_Jogada(9, turno, Jogo)
				elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
					print('Botao 0')
			if event.type == pygame.MOUSEBUTTONUP:
				# Button 1 = Botao esquerdo do mouse
				if event.button == 1:
					# Primeira linha
					if pygame.Rect(100, 25, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(1, turno, Jogo)
					if pygame.Rect(230, 25, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(2, turno, Jogo)
					if pygame.Rect(380, 25, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(3, turno, Jogo)
					# Segunda linha
					if pygame.Rect(100, 130, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(4, turno, Jogo)
					if pygame.Rect(230, 130, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(5, turno, Jogo)
					if pygame.Rect(380, 130, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(6, turno, Jogo)
					# Terceira linha
					if pygame.Rect(100, 230, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(7, turno, Jogo)
					if pygame.Rect(230, 230, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(8, turno, Jogo)
					if pygame.Rect(380, 230, 121, 96).collidepoint(event.pos):
						turno = faz_Jogada(9, turno, Jogo)

		desenha_jogo()
		mensagem_tela('Onde deseja jogar?')
		pygame.display.update()
		Jogo.player = turno
		Jogo.CheckGameOver(Jogo.board, True)
		clock.tick(FPS)
		if Jogo.endgame == True:
			jogo = False
			if Jogo.player == 1:
				Jogo.player = 2
			else:
				Jogo.player = 1
			gameTela.fill(white)
			mensagem_tela('Parabens! O Player ' + str(Jogo.player) + 'Venceu!')
			pygame.display.update()
			time.sleep(2)

def start_PvsC(Jogo):
	jogo = True
	turno = random.randint(1, 2)

	while jogo:
		if Jogo.player == 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1 or event.key == pygame.K_KP1:
							turno = faz_Jogada(1, turno, Jogo)
					elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
							turno = faz_Jogada(2, turno, Jogo)
					elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
							turno = faz_Jogada(3, turno, Jogo)
					elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
							turno = faz_Jogada(4, turno, Jogo)
					elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
							turno = faz_Jogada(5, turno, Jogo)
					elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
							turno = faz_Jogada(6, turno, Jogo)
					elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
							turno = faz_Jogada(7, turno, Jogo)
					elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
							turno = faz_Jogada(8, turno, Jogo)
					elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
							turno = faz_Jogada(9, turno, Jogo)
					elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
						print('Botao 0')
				if event.type == pygame.MOUSEBUTTONUP:
					# Button 1 = Botao esquerdo do mouse
					if event.button == 1:
						# Primeira linha
						if pygame.Rect(100, 25, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(1, turno, Jogo)
						if pygame.Rect(230, 25, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(2, turno, Jogo)
						if pygame.Rect(380, 25, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(3, turno, Jogo)
						# Segunda linha
						if pygame.Rect(100, 130, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(4, turno, Jogo)
						if pygame.Rect(230, 130, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(5, turno, Jogo)
						if pygame.Rect(380, 130, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(6, turno, Jogo)
						# Terceira linha
						if pygame.Rect(100, 230, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(7, turno, Jogo)
						if pygame.Rect(230, 230, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(8, turno, Jogo)
						if pygame.Rect(380, 230, 121, 96).collidepoint(event.pos):
							turno = faz_Jogada(9, turno, Jogo)
		else:
			turno = faz_Jogada(Jogo.iaMove(Jogo.board), turno, Jogo)

		desenha_jogo()
		mensagem_tela('Onde deseja jogar?')
		pygame.display.update()
		Jogo.player = turno
		Jogo.CheckGameOver(Jogo.board, True)
		clock.tick(FPS)
		if Jogo.endgame == True:
			jogo = False
			if Jogo.player == 1:
				Jogo.player = 2
			else:
				Jogo.player = 1
			gameTela.fill(white)
			mensagem_tela('Parabens! O Player ' + str(Jogo.player) + 'Venceu!')
			pygame.display.update()
			time.sleep(2)

def pontos(Pontuacao):
	gameTela.fill(white)
	pygame.display.update()
	simpleText = pygame.font.Font('freesansbold.ttf', 20)
	options = ['Player vs Player', 'O Player 1 venceu ' + str(Pontuacao.pontos_p1) + ' vezes', 'O Player 2 venceu ' + str(Pontuacao.pontos_p1) + ' vezes', 'Empatou ' + str(Pontuacao.empatePvsP) + ' vezes', 'Player  vs  Computer', 'O Player venceu ' + str(Pontuacao.player) + ' vezes', 'O Computador venceu ' + str(Pontuacao.computer) + ' vezes', 'Empatou ' + str(Pontuacao.empatePvsC) + ' vezes']
	x, y = 150, 40
	for i in range(len(options)):
		option = simpleText.render(options[i], True, black)
		gameTela.blit(option, (x, y))
		y += 40
	pygame.display.update()
	time.sleep(5)

def game_loop():
	menu = True
	Pontuacao = Placar()
	while menu:
		Jogo = Game()
		gameTela.fill(white)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1 or event.key == pygame.K_KP1:
					gameTela.fill(white)
					start_PvsP(Jogo)
					Pontuacao.getScore(Jogo, 1)
				elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
					gameTela.fill(white)
					start_PvsC(Jogo)
					Pontuacao.getScore(Jogo, 2)
				elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
					gameTela.fill(white)
					pontos(Pontuacao)
				elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
					pygame.quit()
					quit()
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if pygame.Rect(180, 175, 250, 40).collidepoint(event.pos):
						gameTela.fill(white)
						start_PvsP(Jogo)
						print Jogo.winner
						Pontuacao.getScore(Jogo, 1)
					elif pygame.Rect(180, 225, 300, 40).collidepoint(event.pos):
						gameTela.fill(white)
						start_PvsC(Jogo)
						Pontuacao.getScore(Jogo, 2)
					elif pygame.Rect(180, 275, 170, 40).collidepoint(event.pos):
						gameTela.fill(white)
						pontos(Pontuacao)
					elif pygame.Rect(180, 325, 80, 40).collidepoint(event.pos):
						pygame.quit()
						quit()

		game_intro()
		pygame.display.update()
		clock.tick(FPS)

game_loop()
pygame.quit()
quit()
