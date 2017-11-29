import pygame
import time
import math
from random import*
import vefur
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
x_rand = round(randrange(0, width - 100))
y_rand = round(randrange(0, height - 100))




global counter
counter = 0


def coordinates():
    pygame.draw.rect(screen, red, (0, height / 2, width, 1))
    pygame.draw.rect(screen, green, (width / 2, 0, 1, height))


def show_score():
    global counter
    text = smallFont.render("Score: " + str(counter), True, black)
    screen.blit(text, [0, 0])


def message_to_screen(text, color, y_displace = 0, x_displace = 0, size = "small"):

    if size == "small":
        textSurface = smallFont.render(text, True, color)
    if size == "medium":
        textSurface = medFont.render(text, True, color)
    if size == "large":
        textSurface = largeFont.render(text, True, color)
    textrect= textSurface.get_rect()
    textrect.center = (width / 2) + x_displace, (height / 2) + y_displace
    screen.blit(textSurface, textrect)




def exit():
    global counter
    screen.fill(white)
    message_to_screen("score:", red, -100, -100, "large")
    message_to_screen(str(counter), red, -100, 100, "large")
    pygame.display.update()
    pygame.QUIT



class make_square():
    def __init__(self, x, y, width, height, inactive_color, active_color):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coloron = active_color
        self.coloroff = inactive_color

    def change_pos(self):
        self.x = round(randrange(200, width - 200))
        self.y = round(randrange(200, height - 200))


    def check_if_over_button(self, response = None, refresh = False):
        if self.x + self.width > m[0] > self.x and self.y + self.height > m[1] > self.y:
            pygame.draw.rect(screen, self.coloron, (self.x, self.y,self. width, self.height))
            if click[0] == 1 and refresh == True:
                global counter
                counter +=1
                self.change_pos()
            elif  click[0] == 1 and refresh == False:
                return exit()

    def draw_square(self):
        pygame.draw.rect(screen, self.coloroff, (self.x, self.y, self.width, self.height))



    def text_to_button(self, msg, size="small", color=black):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        screen.blit(textSurf, textRect)

    def text_objects(self, text, color, size):
        if size == "small":
            textSurface = smallFont.render(text, True, color)
        if size == "medium":
            textSurface = medFont.render(text, True, color)
        if size == "large":
            textSurface = largeFont.render(text, True, color)
        return textSurface, textSurface.get_rect()



class make_apple(make_square):


    def draw(self):
        pygame.draw.rect(screen, green, [x_rand, y_rand, appleThickness, appleThickness])








armValues = {1: [width / 2, height / 2, 0, 0], 2: [width / 2, height / 2, 0, 0]}


class make_arm():
    x = 0
    y = 1
    end_x = 2
    end_y = 3
    def __init__(self, name, x, y, length=200, angle=0, end_x=0, end_y=0):
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
    name = input("hvert er nafn þitt(max 6 stafir): ")
    x = 0
    y = 1
    end_x = 2
    end_y =3
    global game
    game = True
    global m
    m = [0, 0]
    #button = make_square(width - 110, 10, 100, 50, green, light_green)
    apple = make_apple(x_rand, y_rand, 30, 30, green, light_green)
    while game:
        for event in pygame.event.get():
            if m[0] >= 0 and m[0] < width and m[1] >= 0 and m[1] < height:
                global click
                click = pygame.mouse.get_pressed()
                m = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                game = False


        screen.fill(white)
        coordinates()
        show_score()
        apple.draw_square()
        apple.check_if_over_button(None, True)


        # button.draw_square()
        # button.check_if_over_button()
        # button.text_to_button("exit")

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
exit()
vefur.save(name, counter)


