import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colliding Blocks")

#Background colour
BG = (178, 190, 181)
BLUE = (0, 71, 171)
RED = (199, 0, 57)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Block:
    def __init__(self, x ,y, height, width, mass, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.mass = mass
        self.color = color

        self.velocity = 0

    def draw(self, win):
        x = self.x
        y = self.y
        pygame.draw.rect(win, self.color, (x, y, self.height, self.width))

    def collide(self, other) -> bool:
        return not(self.x + self.width < other.x or self.x > other.x + other.width)
    
    def wall_collide(self) -> bool:
        return (self.x <= 0)

    def bounce(self, other) -> float:
        #m1 + m2
        add_v = self.mass + other.mass
        #m1 - m2
        sub_v = self.mass - other.mass

        #v1
        new_v1 = ((sub_v/add_v) * self.velocity) + (((2*other.mass)/add_v) * other.velocity)

        return new_v1


    def update_pos(self):
        self.x += self.velocity


def main():
    #Collision count
    COUNT = 0
    is_running = True
    clock = pygame.time.Clock()


    #Create our counter
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    #Create the blocks and then add them into a list so that we can draw them
    first_block = Block(200, 550, 50, 50, 1, WHITE)
    second_block = Block(600, 400, 200, 200, 100, WHITE)
    second_block.velocity = -3

    blocks = [first_block, second_block]

    while is_running:
        #Setting max FPS at 60
        clock.tick(60)
        WIN.fill(BLACK)

        #Draw the text for our counter
        text = font.render(str(COUNT), True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (50, 50)
        WIN.blit(text, textRect)

        #Allows us to exit game safely using the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        #Draw the blocks
        for block in blocks:
            block.update_pos()
            block.draw(WIN)

        if(first_block.wall_collide()):
            first_block.x = 0
            first_block.velocity *= -1
            COUNT += 1

        if(first_block.collide(second_block)):
            COUNT += 1
            v1 = first_block.bounce(second_block)
            v2 = second_block.bounce(first_block)
            first_block.velocity = v1
            second_block.velocity = v2
        

        pygame.display.update()

    pygame.quit()
    
main()
