import sys, pygame
from random import randint
pygame.init()
font = pygame.font.SysFont("None", 24)
main = pygame.display.set_mode((720, 480))
main.fill((255, 255, 255))
class Body:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Snake:
    bodylist=[]
    heading=0
    x=0
    y=0

    def __init__(self,x,y):
        self.heading=pygame.K_RIGHT
        self.x=x
        self.y=y
        body = Body(x-20,y)
        self.bodylist.append(body)
        bod2 = Body(x-40,y)
        self.bodylist.append(bod2)
        bod3 = Body(x-60,y)
        self.bodylist.append(bod3)

    def draw(self):
        for element in self.bodylist:
            pygame.draw.rect(main,(0,255,0),((element.x-10,element.y-10),(20,20)),0)
            pygame.draw.rect(main,(10,128,0),((self.x-10,self.y-10),(20,20)),0)

    def setheading(self,keystroke):
        self.heading=keystroke

    def collide(self):
        for bd in self.bodylist:
            if ((self.x,self.y)==(bd.x,bd.y)):
                return True
            return False

    def grow(self):
        tmpbody=self.bodylist[len(self.bodylist)-1]
        self.bodylist.append(tmpbody)

    def move(self):
        self.bodylist.insert(0,Body(self.x,self.y))
        removeBlock=self.bodylist.pop()

        pygame.draw.rect(main,(255,255,255),((removeBlock.x-10,removeBlock.y-10),(20,20)),0)
        if (self.heading==pygame.K_RIGHT):
            self.x+=20
        elif (self.heading==pygame.K_DOWN):
            self.y+=20
        elif (self.heading==pygame.K_UP):
            self.y-=20
        elif (self.heading==pygame.K_LEFT):
            self.x-=20
        elif (self.heading==pygame.K_q):
            sys.exit()
        else:
            return

    def eat(self,food):
        return ((food.x==self.x) and (food.y==self.y))

class Food:
    x=0
    y=0
    def __init__(self):
        self.x=randint(1,34)*20
        self.y=(randint(1,22)*20)+20
        self.colr=(0,0,255)

    def draw(self):
        pygame.draw.rect(main,self.colr,((self.x-10,self.y-10),(20,20)),0)

    def move(self):
        pygame.draw.rect(main,(255,255,255),((self.x-10,self.y-10),(20,20)),0)
        self.x=randint(1,34)*20
        self.y=(randint(1,22)*20)+20

class Scoreboard:
    score = 0
    def __init__(self):
        self.score=0

    def increase(self):
        self.score=self.score+1

    def display(self):
        pygame.draw.rect(main, (0,0,0), ((0,0),(720,20)),0)
        text=font.render("Score "+ str(self.score),True,(255,0,0))
        main.blit(text,(320,5))

def outofbounds(x, y):
    if ((x < 20) or (x > 710) or (y < 40) or (y > 470)):
        return True
    return False

def Main():
    scoreboard = Scoreboard()
    blueberry = Food()
    snake = Snake(100,80)
    snake.draw()
    pygame.display.update()
    while (True):
        scoreboard.display()
        blueberry.draw()
        if outofbounds(snake.x,snake.y):
            sys.exit()
        if (snake.collide()):
            sys.exit()
        if snake.eat(blueberry):
            scoreboard.increase()
            snake.grow()
            blueberry.move()

        snake.move()
        snake.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                snake.setheading(event.key)

            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        pygame.time.delay(100)

if __name__ == '__main__':
    pygame.display.set_caption("Snake Game")
    pygame.draw.rect(main, (0,0,0), ((0,0),(720,20)),0)
    pygame.draw.rect(main, (0,0,0), ((0,20),(720,460)), 16)

    Main()
