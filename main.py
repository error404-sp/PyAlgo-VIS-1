import display
import pygame
from algs import algorithmsDict, run_alogorithm
from random import randint

# Global Variables: numBars, delay, toDraw, button
# They were declared in display.py


def main():
    numbers = []
    running = True
    # Add default values
    display.sizeBox.text = '256'
    display.algorithmBox.add_options(list(algorithmsDict.keys()))
    # display.algorithmBox.text = 'mergesort'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display.sizeBox.update(event)
            display.delayBox.update()
            display.algorithmBox.update()
            display.startButton.update()
            a_list = list(range(0, display.numBars))

            if display.startButton.active:
                # Set the values given by the user
                display.numBars = int(display.sizeBox.text)
                display.delay =\
                    display.delayBox.value - display.delayBox.rect.x - 6
                algorithm = display.algorithmBox.get_active_option()
                # Generates a random list
                numbers = [randint(10, 500) for i in range(display.numBars)]
                # Executes the chosen algorithm
                run_alogorithm(algorithm.lower(), numbers)
                display.toDraw = True
        display.drawInterface(numbers, -1, -1, -1, -1, greenRows = a_list)

if __name__ == '__main__':
    main()
