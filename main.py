import pygame
import random

#core class
class Core:
    def __init__(self):
        self.hp = 100
        self.pwr = 0


#wall class
class Wall:
    def __init__(self):
        self.hp = 200
        self.pwr = 0


class Node:
    def __init__(self):
        self.hp = 50
        self.pwr = 0
        self.powr = 0
    
    def powercheck (self,x,y):
        self.powr = 0
        for xx in range(7):
            for yy in range(7):
                try:
                    self.powr += tiles[x-3+xx][y-3+yy].pwr
                except:
                    pass
        return self.powr



class Lightningtower:
    def __init__(self):
        self.hp = 75
        self.pwr = 0
    def strikereq(self,x,y):
        if random.randint(0,100) == 13:
            print("STRIKE",x,y)
            self.pwr = 1000
        else:
            self.pwr = 0
        







#Initialise basics
pygame.display.set_caption('Terra Nova')
pygame.display.set_icon(pygame.image.load("Images/icon.png"))
running = True
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#Initialise Game Stuff
tiles = []
for x in range(25):
    tiles.append([])
    for y in range(25):
        tiles[x].append(0)
xpos = 1600
ypos = 1600
carrying = False
mousedown = False
networks = []
globalpower = 0

#getting Images
hotbar = pygame.image.load("Images/hotbar.png")
emptytile = pygame.image.load("Images/emptytile.png")
coretile = pygame.image.load("Images/core.png")
walltile = pygame.image.load("Images/wall.png")
nodetile = pygame.image.load("Images/node.png")
delete = pygame.image.load("Images/delete.png")
lightningtower = pygame.image.load("Images/lightningtower.png")



c = Core()
tiles[13][21] = c

while running:
    globalpower = 0
    if mousedown:
        mousedown = False




    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousedown = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            carrying = False
    #key check
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] and ypos - 180 < 2300:
        ypos += 5
    if keys[pygame.K_w] and ypos > 0:
        ypos -= 5
    if keys[pygame.K_a] and xpos > 0:
        xpos -= 5
    if keys[pygame.K_d] and xpos +380 < 2300:
        xpos += 5

    #cursor pos
    xcurs, ycurs = pygame.mouse.get_pos()


    #rendering tiles
    for x in range(25):
        for y in range(25):
            if tiles[x][y] == 0:
                tile = emptytile

            elif isinstance(tiles[x][y],Core):
                tile = coretile

            elif isinstance(tiles[x][y],Wall):
                tile = walltile
            elif isinstance(tiles[x][y],Node):
                tile = nodetile
                globalpower += tiles[x][y].powercheck(x,y)
            elif isinstance(tiles[x][y],Lightningtower):
                tile = lightningtower
                tiles[x][y].strikereq(x,y)

            screen.blit(tile,(x*128-xpos,y*128-ypos))









    #checking for positioning
    if mousedown and carrying != False and tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] == 0:
        tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] = carrying
        
        #if isinstance(carrying,Node):
        #    tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)].birth()


        if keys[pygame.K_LSHIFT] == False:
            carrying = False





    
    if mousedown and carrying != False and tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] != 0 and carrying == 1:
        tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] = 0
        if keys[pygame.K_LSHIFT] == False:
            carrying = False
    




    #hotbar
    screen.blit(hotbar,(0,600))
    screen.blit(walltile,(10,610))
    screen.blit(nodetile,(143,610))
    screen.blit(lightningtower,(286,610))
    screen.blit(delete,(1145,610))
    
    if mousedown and 10 < xcurs < 138 and 610 < ycurs < 738:
        carrying = Wall()
    if mousedown and 143 < xcurs < 271 and 610 < ycurs < 738:
        carrying = Node()
    if mousedown and 286 < xcurs < 414 and 610 < ycurs < 738:
        carrying = Lightningtower()
    if mousedown and 1145 < xcurs < 1273 and 610 < ycurs < 738:
        carrying = 1

    if carrying != False:
        if isinstance(carrying,Wall):
            screen.blit(walltile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying,Node):
            screen.blit(nodetile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying,Lightningtower):
            screen.blit(lightningtower,(xcurs-64,ycurs+-64))
        elif carrying == 1:
            screen.blit(delete,(xcurs-64,ycurs+-64))
    






    clock.tick(60)
    pygame.display.flip()
    print(globalpower)

            



pygame.quit()



