import pygame
import random
import math

#core class
class Core:
    def __init__(self):
        self.maxhp = 1000
        self.hp = 1000
        self.pwr = 0

    def damage(self,dmg):
        self.hp -= dmg


#wall class
class Wall:
    def __init__(self):
        print("new wall object created")
        self.hp = 200
        self.pwr = -100
        self.maxhp = 200

    def damage(self,dmg):
        self.hp -= dmg


class Node:
    def __init__(self):
        self.hp = 50
        self.pwr = 0
        self.powr = 0
        self.col = ""
        self.pulses = []
        self.above900 = False
        self.maxhp = 50

    def powercheck (self,x,y):
        global tileschecked
        self.powr = 0
        for xx in range(7):
            for yy in range(7):
                try:
                    if (x-3+xx,y-3+yy) in tileschecked:
                        pass
                    else:
                        #print("ok")
                        tileschecked.append((x-3+xx,y-3+yy))
                        self.powr += tiles[x-3+xx][y-3+yy].pwr
                except:
                    pass
        return self.powr

    def makelines(self,x,y):
        self.col = generate_cyan_shade(1000-globalpower)

        for xx in range(7):
            for yy in range(7):
                try:
                    if tiles[x-3+xx][y-3+yy] != 0 and not(isinstance(tiles[x-3+xx][y-3+yy],Wall)) and not((isinstance(tiles[x-3+xx][y-3+yy],Node))) and not((isinstance(tiles[x-3+xx][y-3+yy],Core))):
                        pygame.draw.line(screen,self.col,(x*128-xpos+64,y*128-ypos+64),((x-3+xx)*128-xpos+64,(y-3+yy)*128-ypos+64),10)
                except:
                    pass
        if globalpower >= 900 and self.above900 == False:
            self.pulses.append(1)
            self.above900 = True
        if globalpower < 900:
            self.above900 = False
            
        """

        for i in range(len(self.pulses)):
            pygame.draw.circle(screen,"#43b5ad",(x*128-xpos,y*128-ypos),self.pulses[i],2)
            self.pulses[i] += 2
            if self.pulses[i] >= 200:
                self.pulses.remove(200)
        """
        i = 0
        while i < len(self.pulses):
            pygame.draw.circle(screen,"#43b5ad",(x*128-xpos+64,y*128-ypos+64),self.pulses[i],4)
            self.pulses[i] += 2
            if self.pulses[i] >= 400:
                 self.pulses.remove(self.pulses[i])
            else:
                i += 1

    def damage(self,dmg):
        self.hp -= dmg


class Lightningtower:
    def __init__(self):
        self.hp = 75
        self.pwr = 0
        self.maxhp = 75
        self.animation = leffect
        self.current_image = None

    def strikereq(self,x,y):
        if random.randint(0,100) == 13:
            #print("STRIKE",x,y)
            self.pwr = 1000
            self.current_image = 0
        else:
            if self.pwr > 0:
                self.pwr -= 40
    
    def execute(self,x,y):
        if self.current_image != None:
            screen.blit(self.animation[self.current_image],(x*128-xpos-128,y*128-ypos-200))
            if iteration % 3 == 0:
                self.current_image += 1
            if self.current_image == len(self.animation):
                self.current_image = None

    def damage(self,dmg):
        self.hp -= dmg
            

class Battery:
    def __init__(self):
        self.hp = 75
        self.pwr = 0
        self.storedpwr = 0
        self.maxhp = 75

    def execute(self):
        self.pwr = 0

    def damage(self,dmg):
        self.hp -= dmg
        """
        if globalpower > 100 and self.storedpwr <= 10000:
            self.pwr = -100
            self.storedpwr += 100
        elif globalpower <= -100 and self.storedpwr >= 100:
            self.pwr = 100
            self.storedpwr -= 100
        print(self.storedpwr,globalpower)
        """


class Turret:
    def __init__(self):
        self.hp = 100
        self.pwr = 0
        self.maxhp = 100

    def execute(self,x,y):
        if (x,y) in tileschecked:
            
            if globalpower >= 100 or globalstored > 0:
                targets = []
                self.pwr = -10
                #print("S")
                for i in range(len(enemys)):
                    enemypos = (enemys[i].xpos, enemys[i].ypos)
                    turpos = (x*128+64,y*128+64)
                    if math.dist(turpos,enemypos) <= 512:
                        targets.append(math.dist(turpos,enemypos))
                        #print("targetinrange")
                if len(targets) >= 0:
                    self.pwr = -100
                for i in range(len(targets)):
                    if min(targets) == targets[i]:
                        enemypos = (enemys[i].xpos-xpos+32, enemys[i].ypos-ypos+32)
                        #print(turpos,enemypos)
                        pygame.draw.line(screen, "#de0202", (turpos[0]-xpos,turpos[1]-ypos),enemypos,10)
                        enemys[i].dmg(1)
                    
                    try:
                        if enemys[i].lp <= 0:
                            enemys.pop(i)

                    except:
                        pass
            else:
                self.pwr = 0

    def damage(self, dmg):
        self.hp -= dmg


class Mender:
    def __init__(self):
        self.hp = 75
        self.pwr = 0
        self.maxhp = 75

    def execute(self,x,y):
        if (x,y) in tileschecked:

            if globalpower >= 100 or globalstored > 0:
                self.pwr = -100
                if iteration % 1 == 0:
                    for xx in range(5):
                        for yy in range(5):
                            try:
                                if tiles[x-2+xx][y-2+yy].hp < tiles[x-2+xx][y-2+yy].maxhp:
                                    print(type(tiles[x-2+xx][y-2+yy]),tiles[x-2+xx][y-2+yy].hp)
                                    tiles[x-2+xx][y-2+yy].damage(-5)
                                    pygame.draw.line(screen, "#017d09", ((x-2+xx)*128-xpos+64,(y-2+yy)*128-ypos+64),(x*128-xpos+64,y*128-ypos+64),10)
                            except:
                                pass

    def damage(self,dmg):
        self.hp -= dmg



class Spawner:
    def __init__(self):
        self.hp = 100000000
        self.pwr = 0

    def summon(self,wave):
        global enemys
        for i in range(wave):
            enemys.append(Enemy())


class Enemy:
    def __init__(self):
        self.lp = 100
        self.xpos = 13*128+32 + random.randint(-64,64)
        self.ypos = 0 + + random.randint(-64,64)
    def dmg(self,dmg):
        self.lp -= dmg
        

    def execute(self):
        screen.blit(enemytex, (self.xpos-xpos,self.ypos-ypos))
        #print(int(self.xpos/128),int(self.ypos/128))
        if tiles[int(self.xpos/128)][int(self.ypos/128)] != 0 and not isinstance(tiles[int(self.xpos/128)][int(self.ypos/128)], Spawner):
            tiles[int(self.xpos/128)][int(self.ypos/128)].damage(5)
            #print(tiles[int(self.xpos/128)][int(self.ypos/128)].hp, tiles[int(self.xpos/128)][int(self.ypos/128)])
            #print(tiles[int(self.xpos/128)+1][int(self.ypos/128)].hp)   
        else:
            self.xpos, self.ypos = move_towards_target((self.xpos,self.ypos),(13*128+32,21*128), 2)

        #da enemy can only walk at 2 coordinates per tick



def move_towards_target(current_position, target_position, max_movement):
    direction = calculate_direction(current_position, target_position)
    dx = direction[0] * max_movement
    dy = direction[1] * max_movement
    new_position = (current_position[0] + dx, current_position[1] + dy)
    return new_position

def calculate_direction(current_position, target_position):
    dx = target_position[0] - current_position[0]
    dy = target_position[1] - current_position[1]
    angle = math.atan2(dy, dx)
    return math.cos(angle), math.sin(angle)








def generate_cyan_shade(input_number):
    # Ensure input_number is within the range [0, 1000]
    input_number = max(0, min(input_number, 1000))
    if input_number >= 1000:
        return (0,0,0)
    if input_number <= 0:
        return (255,255,255)

    # Calculate the RGB values based on the input number
    # Cyan has RGB values (0, 255, 255)
    # We'll adjust the intensity of the blue and green channels
    blue_intensity = 255 - int(input_number * 255 / 1000)
    green_intensity = 255 - int(input_number * 255 / 1000)

    # Construct the RGB tuple
    cyan_rgb = (0, green_intensity, blue_intensity)

    return cyan_rgb



#Initialise basics
pygame.display.set_caption('Terra Nova')
pygame.display.set_icon(pygame.image.load("Images/icon.png"))
running = True
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None,72)

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
tileschecked = []
globalstored = 0
tiles[13][0] = Spawner()
iteration = 0
enemys = list()
globalstored = 35000

#getting Images
hotbar = pygame.image.load("Images/hotbar.png")
emptytile = pygame.image.load("Images/emptytile.png")
coretile = pygame.image.load("Images/core.png")
walltile = pygame.image.load("Images/wall.png")
nodetile = pygame.image.load("Images/node.png")
delete = pygame.image.load("Images/delete.png")
lightningtower_tile = pygame.image.load("Images/lightningtower.png")
batterytile = pygame.image.load("Images/battery.png")
enemytex = pygame.image.load("Images/enemy.png")
turrettile = pygame.image.load("Images/turret.png")
mendertile = pygame.image.load("Images/mender.png")
topbar = pygame.image.load("Images/topbar.png")
nobuild = pygame.image.load("Images/nobuild.png")

leffect = []

for i in range(12):
    filepath = "Images/Lightning Strike Animation/background-remover/lightning-form-effect-{}.png".format(i+1)
    img = pygame.image.load(filepath)
    leffect.append(img)


c = Core()
tiles[13][21] = c

while running:
    iteration += 1
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
        ypos += 10
    if keys[pygame.K_w] and ypos > 0:
        ypos -= 10
    if keys[pygame.K_a] and xpos > 0:
        xpos -= 10
    if keys[pygame.K_d] and xpos +380 < 2300:
        xpos += 10

    #cursor pos
    xcurs, ycurs = pygame.mouse.get_pos()


    tileschecked = []
    #rendering tiles
    for x in range(25):
        for y in range(25):
            try:
                if tiles[x][y].hp <= 0:
                    #print(tiles[x][y],tiles[x][y].hp)
                    tiles[x][y] = 0
            except:
                pass

            if tiles[x][y] == 0 or isinstance(tiles[x][y], Spawner):
                tile = emptytile
            elif isinstance(tiles[x][y], Core):
                tile = coretile
            elif isinstance(tiles[x][y], Wall):
                tile = walltile
            elif isinstance(tiles[x][y], Node):
                tile = nodetile
                globalpower += tiles[x][y].powercheck(x,y)
            elif isinstance(tiles[x][y], Lightningtower):
                tile = lightningtower_tile
                tiles[x][y].strikereq(x,y)
            elif isinstance(tiles[x][y], Battery):
                tile = batterytile
            elif isinstance(tiles[x][y], Turret):
                tile = turrettile
            elif isinstance(tiles[x][y], Mender):
                tile = mendertile

            screen.blit(tile,(x*128-xpos,y*128-ypos))
  


    count = 0
    for x in range(25):
        for y in range(25):
            if isinstance(tiles[x][y], Node):
                tiles[x][y].makelines(x,y)
            elif isinstance(tiles[x][y], Battery):
                count += 1
            
    try:
        
        if globalpower < 0 and globalstored > 0:
            for i in range(count):
                if globalpower < 100*count:
                    globalstored -= (0-globalpower/count)
                    globalpower += (0-globalpower/count)
        
        if globalpower > 0:
            for i in range(count):
                if globalstored < count*50000:
                    globalstored += (globalpower/count)
                    globalpower -= (globalpower/count)

    except:
        pass
    for x in range(25):
        for y in range(25):
            #Stuff other than power
            if isinstance(tiles[x][y], Turret) or isinstance(tiles[x][y], Mender) or isinstance(tiles[x][y], Lightningtower):
                tiles[x][y].execute(x,y)

    #print(globalpower, globalstored)


    #Summon waves
    if iteration % 1000 == 0:
        print("WAVE", int(iteration/1000))
        tiles[13][0].summon(int((iteration/1000)**1.1))
    for i in range(len(enemys)):
        enemys[i].execute()



    #print("Current animation frames:", animation_frames)


    #checking for positioning
    if mousedown and carrying != False and tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] == 0:
        #print(f"placing object {type(carrying)}")
        tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] = carrying
        
        #if isinstance(carrying,Node):
        #    tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)].birth()

        if keys[pygame.K_LSHIFT] == False:
            carrying = False
        else:
            if isinstance(carrying, Wall) and globalstored > 30000:
                carrying = Wall()
                price = 30000
            elif isinstance(carrying, Node) and globalstored > 5000:
                carrying = Node()
                price = 5000
            elif isinstance(carrying, Lightningtower) and globalstored > 10000:
                carrying = Lightningtower()
                price = 10000
            elif carrying == 1:
                carrying = 1
            elif isinstance(carrying, Battery) and globalstored > 10000:
                carrying = Battery()
                price = 10000
            elif isinstance(carrying, Turret) and globalstored > 50000:
                carrying = Turret()
                price = 50000
            elif isinstance(carrying, Mender) and globalstored > 100000:
                carrying = Mender()
                price = 100000
            else:
                carrying = False
    
        globalstored -= price

    if mousedown and carrying != False and tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] != 0 and carrying == 1:
        tiles[int((xpos+xcurs)/128)][int((ypos+ycurs)/128)] = 0
        if keys[pygame.K_LSHIFT] == False:
            carrying = False
    
    screen.blit(topbar,(0,-50))
    
    
    
    col = globalstored / (count * 50000 + 0.0000001)
    if col > 1:
        col = 1


    red_value = min(255, int(((1 - col) / 1) * 255))
    green_value = min(255, int((col / 1) * 255))
    col = (red_value, green_value, 0)

    try:
        if globalstored/100 < 1000:
            st = font.render(str(int(globalstored/100)),True, col)
        else:
            st = font.render(str(int(globalstored/10000)/10)+"k",True, col)


        screen.blit(st, (550,30))

    except:
        pass





    #hotbar
    screen.blit(hotbar,(0,590))
    screen.blit(walltile,(10,600))
    screen.blit(nodetile,(143,600))
    screen.blit(lightningtower_tile,(286,600))
    screen.blit(delete,(1145,600))
    screen.blit(batterytile,(420,600))
    screen.blit(turrettile,(560,600))
    screen.blit(mendertile,(700,600))
    if globalstored < 30000:
        screen.blit(nobuild,(10,600))
    if globalstored < 5000:
        screen.blit(nobuild,(143,600))
    if globalstored < 10000:
        screen.blit(nobuild,(286,600))
    if globalstored < 10000:
        screen.blit(nobuild,(420,600))
    if globalstored < 50000:
        screen.blit(nobuild,(560,600))
    if globalstored < 100000:
        screen.blit(nobuild,(700,600))










    if mousedown and 10 < xcurs < 138 and 610 < ycurs < 738 and globalstored >= 30000:
        carrying = Wall()
        price = 30000
    if mousedown and 143 < xcurs < 271 and 610 < ycurs < 738 and globalstored >= 5000:
        carrying = Node()
        price = 5000
    if mousedown and 286 < xcurs < 414 and 610 < ycurs < 738 and globalstored >= 10000:
        carrying = Lightningtower()
        price = 10000
    if mousedown and 420 < xcurs < 548 and 610 < ycurs < 738 and globalstored >= 10000:
        carrying = Battery()
        price = 10000
    if mousedown and 560 < xcurs < 688 and 610 < ycurs < 738 and globalstored >= 50000:
        carrying = Turret()
        price = 50000
    if mousedown and 700 < xcurs < 828 and 610 < ycurs < 738 and globalstored >= 100000:
        carrying = Mender()
        price = 100000
    if mousedown and 1145 < xcurs < 1273 and 610 < ycurs < 738:
        carrying = 1
        price = 0

    if carrying != False:
        if isinstance(carrying, Wall):
            screen.blit(walltile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying, Node):
            pygame.draw.polygon(screen,"#ffffff", ((xcurs+448,ycurs+448),(xcurs+448,ycurs-448),(xcurs-448,ycurs-448),(xcurs-448,ycurs+448)),5)
            screen.blit(nodetile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying, Lightningtower):
            screen.blit(lightningtower_tile,(xcurs-64,ycurs+-64))
        elif carrying == 1:
            screen.blit(delete,(xcurs-64,ycurs+-64))
        elif isinstance(carrying, Battery):
            screen.blit(batterytile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying, Turret):
            pygame.draw.circle(screen, "#ffffff", (xcurs,ycurs), 512, 5)
            screen.blit(turrettile,(xcurs-64,ycurs+-64))
        elif isinstance(carrying, Mender):
            pygame.draw.polygon(screen,"#ffffff", ((xcurs+320,ycurs+320),(xcurs+320,ycurs-320),(xcurs-320,ycurs-320),(xcurs-320,ycurs+320)),5)
            screen.blit(mendertile,(xcurs-64,ycurs+-64))
    #print(tiles[13][21])
    
    if not isinstance(tiles[13][21],Core):
        print("FF")
        break










    clock.tick(30)
    pygame.display.flip()

            

pygame.quit()

