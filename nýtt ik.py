import pygame
import time
import math
from random import*
#import vefur
pygame.init()
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

blue = (0, 0, 200)
light_blue = (0, 0, 255)

width, height = 1000, 800
smallFont=pygame.font.SysFont("comicsansms", 25)
medFont=pygame.font.SysFont("comicsansms", 50)
largeFont=pygame.font.SysFont("comicsansms", 80)

screen = pygame.display.set_mode((width, height))

global x_rand, y_rand
global appleThickness
appleThickness = 30

x_rand = round(randrange(0, width - appleThickness))
y_rand = round(randrange(0, height - appleThickness))


global counter
counter = 0

class background():

    def coordinates():
        pygame.draw.rect(screen, red, (0, height / 2, width, 1))
        pygame.draw.rect(screen, green, (width / 2, 0, 1, height))

    def show_score():
        global counter
        counter += 1
        text = smallFont.render("Score: " + str(counter), True, black)
        screen.blit(text, [0, 0])


class make_square():
    


    def button(text, x, y, width, height, inactive_color, active_color, action=None):
        cursor = pygame.mouse.get_pos()
        global click
        click = pygame.mouse.get_pressed()
        if x + width > cursor[0] > x and y + height > cursor[1] > y:
            pygame.draw.rect(screen, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "exit":
                    global game
                    game = False
                    return game

        else:
            pygame.draw.rect(screen, inactive_color, (x, y, width, height))
        background.text_to_button(text, x, y, width, height)

    def text_to_button(msg, button_x, button_y, button_width, button_height, size="small", color=black):
        textSurf, textRect = background.text_objects(msg, color, size)
        textRect.center = ((button_x + (button_width / 2)), (button_y + (button_height / 2)))
        screen.blit(textSurf, textRect)

    def text_objects(text, color, size):
        if size == "small":
            textSurface = smallFont.render(text, True, color)
        if size == "medium":
            textSurface = medFont.render(text, True, color)
        if size == "large":
            textSurface = largeFont.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def message_to_screen(msg, color, y_displace=0, x_displace=0, size="small"):
        textSurface, textRect = background.text_objects(msg, color, size)

        textRect.center = (width / 2) + x_displace, (height / 2) + y_displace
        screen.blit(textSurface, textRect)




    def exit():
        global counter
        screen.fill(white)
        background.message_to_screen("score:", red, -100, -100, "large")
        background.message_to_screen(str(counter), red, -100, 100, "large")
        pygame.display.update()


class make_apple():
    count = 0
    def __init__(self, size = 30):
        self.size = size


    def new(self, first = count):
        if first == 0:
            self.x_rand = round(randrange(0, width - self.size))
            self.y_rand = round(randrange(0, height - self.size))
        make_apple.count = 1

    def check_if_eat(self):
        if self.x_rand+ self.size > m[0] > self.x_rand and self.y_rand + self.size > m[1] > self.y_rand:
            if click[0] and action != None:
                print("ja")
                self.new(0)
        #if m[0] > self.x_rand and m[0] < self.x_rand + size or m[1] > self.y_rand and m[1] < self.y_rand + size :

    def draw(self):
        pygame.draw.rect(screen, green, [x_rand, y_rand, appleThickness, appleThickness])







# armlist2 = x1, y1
armValues = {1: [width / 2, height / 2, 0, 0], 2: [width / 2, height / 2, 0, 0], 3: [width / 2, height / 2, 0, 0]}


class make_arm():
    x = 0
    y = 1
    end_x = 2
    end_y = 3
    def __init__(self, name, x, y, length=300, angle=0, end_x=0, end_y=0):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle
        self.end_x = end_x
        self.end_y = end_y

    def point_at(self, x, y):
        # distance between target x and arm x
        dx = x - self.x
        dy = y - self.y
        # angle between vectors
        self.angle = math.atan2(dy, dx)

    def drag(self, x, y):
        self.point_at(x, y)

        self.x = x - math.cos(self.angle) * self.length
        self.y = y - math.sin(self.angle) * self.length

    def get_end_xy(self):
        self.end_x = self.x + math.cos(self.angle) * self.length
        self.end_y = self.y + math.sin(self.angle) * self.length

    def change(self, change=0):
        # put in dictionary
        armValues.setdefault(self.name, [self.x, self.y, self.end_x, self.end_y])

        if self.name in armValues:
            if change != 0:
                x = 0
                y = 1
                end_x = 2
                end_y = 3
                # ef x != end_x á fyrri línu "make it happen"
                num = self.name+1
                self.x, self.y = armValues[num][end_x], armValues[num][end_y]
                #svo reikna út aftur end_x á seinni línu
                self.get_end_xy()

            armValues[self.name] = [self.x, self.y, self.end_x, self.end_y]

    def draw(self):


        for arm in armValues:
            baseLine = pygame.draw.aaline(screen, black, [self.x, self.y], [self.end_x, self.end_y], 100)





def loop():
    global name
    #name = input("hvert er nafn þitt(max 6 stafir): ")
    x = 0
    y = 1
    end_x = 2
    end_y =3
    global game
    game = True

    m = [0, 0]
    while game:
        for event in pygame.event.get():
            if m[0] >= 0 and m[0] < width and m[1] >= 0 and m[1] < height:
                m = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                game = False


        screen.fill(white)
        background.coordinates()
        background.show_score()
        background.button("exit", width-110, 10, 100, 50, green, light_green, action="exit")
        epli = make_apple()
        epli.new()
        epli.draw()

        arm = make_arm(1, armValues[2][end_x], armValues[2][end_y])


        arm.drag(m[0], m[1])
        arm.get_end_xy()
        arm.change()

        arm2 = make_arm(2, armValues[2][x], armValues[2][y])
        arm2.point_at(armValues[1][x], armValues[1][y])

        arm2.get_end_xy()
        arm2.change()


        try:# ef self.x, self.y  != end_x,end_y ´á strikinu á undan  sendir það i change
            if armValues[1][x] != armValues[2][end_x] and armValues[1][y] != armValues[2][end_y]:
                arm.change(1)
        except:
            pass



        arm.draw()
        arm2.draw()
        

        pygame.display.update()







loop()
background.exit()
#vefur.save(name, counter)
vefur.go()

