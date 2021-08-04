import random
import tkinter
import time

from tkinter import *
import tkinter.messagebox

from time import sleep

root=Tk()
tkinter.messagebox.showinfo('Roulette Wheel', 'Roulette wheel is now active')
root.mainloop()

accbal = 100

with open(r"C:\Users\LukeF\Documents\GitHub\Roulette\account.txt", "a") as f:
    f.write('%d' % accbal)

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
colours = ['R', 'B', 'G']

print(numbers)
print(colours)

chosenBetType = input('Choose bet type: ')

if chosenBetType == 'Number':
    chosenNumber = int(input('Choose number: '))
    print('Spinning wheel...')
    sleep(3)
    winningNumber = random.choice(numbers)
    print('Winning number is: ', winningNumber)
    if chosenNumber == winningNumber:
        print('You win!')
    else:
        print('You lose')

if chosenBetType == 'Colour':
    chosenColour = input('Choose colour: ')
    print('Spinning wheel...')
    sleep(3)
    winningColour = random.choice(colours)
    print('Winning colour is: ', winningColour)
    if chosenColour == winningColour:
        print('You win!')
    else:
        print('You lose')

