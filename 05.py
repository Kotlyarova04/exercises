'''import sys
import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit()

    x += vx * dt
    y += vy * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()'''
import random

import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

running = True


class Molecule:
    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.radius > window_width or self.x - self.radius < 0:
            self.speed_x *= -1

        if self.y + self.radius > window_height or self.y - self.radius < 0:
            self.speed_y *= -1

        for molecule in molecules:
            if molecule != self:
                distance = ((self.x - molecule.x) ** 2 + (self.y - molecule.y) ** 2) ** 0.5
                if distance <= self.radius + molecule.radius:
                    self.speed_x, molecule.speed_x = molecule.speed_x, self.speed_x
                    self.speed_y, molecule.speed_y = molecule.speed_y, self.speed_y



molecules = []


for _ in range(20):
    x = random.randint(20, 600)
    y = random.randint(20, 400)
    speed_x = random.uniform(0.5, 2)
    speed_y = random.uniform(0.5, 2)
    radius = random.randint(10, 40)
    color = [WHITE, RED, GRAY, LIGHT_BLUE, GREEN, YELLOW, PINK]
    colour = random.choice(color)
    molec = Molecule(x, y, speed_x, speed_y, radius, colour)
    molecules.append(molec)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    for molecule in molecules:
        molecule.update()
        molecule.draw()

    pygame.display.flip()

pygame.quit()