import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("space ke rakshak")
icon = pygame.image.load("spaceship.png")
background = pygame.image.load("back.jpg")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("shootership.png")
playercoordX = 268
playercoordY = 400
playercoordX_change=0
playercoordY_change=0 

enemyImg = pygame.image.load("alien.png")
enemycoordX = random.randint(0,536)
enemycoordY = random.randint(0,150)
enemycoordX_change= 4
enemycoordY_change= 20

bulletImg = pygame.image.load("bullet.png")
bulletcoordX = 0
bulletcoordY = 400
bulletcoordX_change= 0
bulletcoordY_change= 5
bulletstate = "ready"

score = 0 
font = pygame.font.Font('freesansbold.ttf', 32)


def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x,y):
	screen.blit(enemyImg, (x,y))

def bullet_fire(x,y):
	global bulletstate
	bulletstate = "fire"
	screen.blit(bulletImg,(x,y))

def colliding(bulletcoordX,bulletcoordY,enemycoordX,enemycoordY):
	distance = math.sqrt( math.pow((bulletcoordX - enemycoordX) , 2) + math.pow ((bulletcoordY - enemycoordY) , 2) )
	if distance < 40:
		return True
def showscore(x,y):
	scorevalue = font.render("Score : " + str(score), True , (0,255,0))
	screen.blit(scorevalue , (x,y)) 

def gameover(x,y):
	overtext = font.render("GAMEOVER",True , (0,0,0))
	screen.blit(overtext , (x,y))


#keep it running
running = True
while running:

	screen.fill((100,100,150))
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playercoordX_change = -3

			if event.key == pygame.K_RIGHT:
				playercoordX_change = 3
			if event.key == pygame.K_SPACE:
				if bulletstate is "ready":
					bulletcoordX = playercoordX
					bullet_fire(bulletcoordX,playercoordY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playercoordX_change = 0



	
	playercoordX+=playercoordX_change			

	if playercoordX <=0:
		playercoordX = 0
	elif playercoordX>536:
		playercoordX = 536


	enemycoordX+=enemycoordX_change

	if enemycoordX <= 0:
		enemycoordX_change = 4
		enemycoordY += enemycoordY_change

	elif enemycoordX >=536:
		enemycoordX_change = -4
		enemycoordY += enemycoordY_change

	if enemycoordY >=350:
		enemycoordY = 700
		gameover(200,250)

	if bulletcoordY < 0:
		bulletstate = "ready"
		bulletcoordY = 400
		
	if bulletstate is "fire":
		bullet_fire(bulletcoordX,bulletcoordY)
		bulletcoordY -= bulletcoordY_change

	if(colliding(bulletcoordX,bulletcoordY,enemycoordX,enemycoordY)):
		bulletstate = "ready"
		bulletcoordY = 400
		score = score + 1
		enemycoordX = random.randint(0,536)
		enemycoordY = random.randint(0,150)	

	player(playercoordX,playercoordY)

	enemy(enemycoordX,enemycoordY)
	showscore(10,10)
	pygame.display.update()