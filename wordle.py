import pygame , sys , words_list , random

WIDTH = 480
HEIGHT = 576

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (222, 222, 25)
GREEN = (0, 255, 100)

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("bold", 110)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Wordle")
programIcon = pygame.image.load('wirdo_icon.png')
pygame.display.set_icon(programIcon)
CodeKeys = "113 119 101 114 116 121 117 105 111 112 97 115 100 102 103 104 106 107 108 122 120 99 118 98 110 109".split()
KeyboardKeys = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split()
column = 0
index = 0

def bilt(letter,index,column):
    text = font.render(letter.upper(),False,WHITE)
    screen.blit(text,( index , column ))

def Trace():
    for i in range(-1,HEIGHT,96):
        pygame.draw.rect(screen,WHITE,( i,0, 3,HEIGHT ))
        pygame.draw.rect(screen,WHITE,( 0,i, WIDTH,3 ))

keybord = []
world = list(random.choice(words_list.worlds))
#print(world) #if you need 
while True:
    for event in pygame.event.get():
        Trace()
        if event.type == pygame.KEYDOWN:
            key = str(event.key)
            if key in CodeKeys:
                letter = KeyboardKeys[CodeKeys.index(key)]
                bilt(letter,(index*96)+17,(column*96)+15)
                if index != 5:
                    keybord.append( letter )
                    index += 1

            elif key == "8" and index != 0:
                pygame.draw.rect(screen,BLACK,( (index-1)*96,column*96, 96,96 ))
                keybord = keybord[0:-1]
                index -= 1
                
            elif key == "13" and index == 5 and "".join(keybord) in words_list.worlds:
                for i in range(len(keybord)):
                    if keybord[i] in world:
                        pygame.draw.rect(screen,YELLOW,( i*96,column*96, 96,96 ))
                        bilt(world[world.index(keybord[i])],(i*96)+17,(column*96)+15)

                    if keybord[i] == world[i]:
                        pygame.draw.rect(screen,GREEN,( i*96,column*96, 96,96 ))
                        bilt(world[i],(i*96)+17,(column*96)+15)

                if keybord == world:
                    print("You win !")
                keybord = []
                index = 0
                column += 1

        elif event.type == pygame.QUIT:
            print("".join(world))
            sys.exit()
            
    pygame.display.update()