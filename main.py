import pygame

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

#getting Images
hotbar = pygame.image.load("Images/hotbar.png")
emptytile = pygame.image.load("Images/emptytile.png")
coretile = pygame.image.load("Images/core.png")
walltile = pygame.image.load("Images/wall.png")


#core class
class Core:
    def __init__(self):
        self.hp = 100
c = Core()
tiles[13][21] = c

#wall class
class Wall:
    def __init__(self):
        self.hp = 200




while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #key check
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        ypos += 5
    if keys[pygame.K_w]:
        ypos -= 5
    if keys[pygame.K_a]:
        xpos -= 5
    if keys[pygame.K_d]:
        xpos += 5




    #rendering tiles
    for x in range(25):
        for y in range(25):
            if tiles[x][y] == 0:
                tile = emptytile

            elif isinstance(tiles[x][y],Core):
                tile = coretile

            elif isinstance(tiles[x][y],Wall):
                tile = walltile



            screen.blit(tile,(x*128-xpos,y*128-ypos))
    





    #hotbar
    screen.blit(hotbar,(0,600))
    screen.blit(walltile,(10,610))


    pygame.display.flip()
    clock.tick(60)







pygame.quit()





