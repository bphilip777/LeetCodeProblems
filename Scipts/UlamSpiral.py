import pygame as pg
import numpy as np

class Primes():
    def __init__(self):
        # Initialize variables
        self.primesList = []  # 0 and 1 are not prime numbers

    def isPrime(self, n:int) -> bool:
        sqrtN = int(np.sqrt(n))  # This will always round down
        if n < 2:
            return False
        if len(self.primesList) > 0:
            for i in self.primesList:
                if i <= sqrtN:
                    val = n / i
                    if val.is_integer():
                        return False
            self.primesList.append(n)
            return True
        elif n > 1:
            self.primesList.append(n)
            return True

colors = {"black": (0, 0, 0),
          "white": (255, 255, 255),
          "red": (255, 0, 0),
          "blue":(25, 25, 112)}

vals = 100

pg.init()  # Initialize modules
pg.font.init()  # Initialize fonts
# Screen properties - based on the number of values to be printed
H, W = 800, 600
screen = pg.display.set_mode((H, W))
screen.fill(colors["black"])

# Numbers to input into the spiral
numbers = np.linspace(1, vals, vals)
primes = Primes()  # Will store prime numbers

fr = 0  # Frame rate
i = 0   # Loop counter to prevent crashing when we reach the end of the number line
# How much should we shift in the X or Y Position
dX, dY = 50, 50

state = 0
stepSize = np.log10(vals)*10
currStep = 0
numSteps = 1
reached = False

# Starting position
xPos, yPos = H // 2, W // 2
states = {0: (stepSize, 0),  # Move Right
          1: (0, -stepSize), # Move Up
          2: (-stepSize, 0), # Move Left
          3: (0, stepSize)}  # Move Down

# Circle props
r = 10
w = 0

# Main loop
run = True
while run:
    # Enable quitting program
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    pg.display.flip()

    if fr % 60 == 0:  # Framerate
        if i < numbers.shape[0]:
            # Draw a circle around the number if the number is a prime number
            isPrime = primes.isPrime(numbers[i])
            if isPrime:
                pg.draw.circle(screen, colors["blue"], (xPos, yPos), r, w)

            # Initialize text variable
            myFont = pg.font.SysFont("Times New Roman", 18)
            numText = myFont.render(f"{int(numbers[i])}", True, colors["white"])
            Rect_numText = numText.get_rect(center=(xPos, yPos))

            # Visualize text
            screen.blit(numText, Rect_numText)
            dX, dY = states[state]
            xPos += dX
            yPos += dY

            currStep += 1
            if currStep % numSteps == 0:
                state += 1
                currStep = 0
                # Update the size of numSteps
                if reached:
                    numSteps += 1
                reached = not reached  # Update this for next loop

            # Resets
            if state == 4:
                state = 0  # Reset

            # Prevents bug of while loop
            i += 1
    # Loop counter = Controls framerate
    fr += 1

print(primes.primesList)