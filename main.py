import sys
import os
import time
import random
import tkinter
from tkinter import *
from tkinter import ttk

os.system('color')

# init window
window = Tk()


all_games = [[0, 3, 7, 1, 0, 6, 4, 9, 8,
              1, 2, 0, 8, 9, 0, 3, 7, 0,
              8, 0, 9, 3, 4, 7, 0, 2, 5,

              0, 8, 3, 0, 5, 4, 2, 0, 9,
              2, 4, 0, 6, 3, 0, 0, 8, 7,
              9, 0, 5, 2, 1, 8, 6, 4, 3,

              0, 1, 8, 0, 6, 3, 9, 0, 2,
              3, 0, 2, 9, 0, 1, 7, 6, 4,
              4, 9, 0, 5, 7, 2, 0, 3, 1]]

all_games_solution = [[5, 3, 7, 1, 2, 6, 4, 9, 8,
                       1, 2, 4, 8, 9, 5, 3, 7, 6,
                       8, 6, 9, 3, 4, 7, 1, 2, 5,

                       6, 8, 3, 7, 5, 4, 2, 1, 9,
                       2, 4, 1, 6, 3, 9, 5, 8, 7,
                       9, 7, 5, 2, 1, 8, 6, 4, 3,

                       7, 1, 8, 4, 6, 3, 9, 5, 2,
                       3, 5, 2, 9, 8, 1, 7, 6, 4,
                       4, 9, 6, 5, 7, 2, 8, 3, 1]]


class Colors:
    reversd = '\u001b[7m'
    brightGreen = '\u001b[32;1m'
    brightRed = '\u001b[31;1m'
    reset = '\u001b[0m'
    lineup = '\033[A'
    linedown = '\033[B'


# Variables
sel = 0

finished = False
game = random.randint(0, 0)
active_game = all_games[game]
active_game_solution = all_games_solution[game]


def print_sud(lst: list, hailait: int):
    for i in range(0, 81):
        if i == hailait - 1:
            if lst[i] == 0:
                sys.stdout.write(Colors.reversd + " " + Colors.reset + ' ')
            else:
                sys.stdout.write(Colors.reversd + str(lst[i]) + Colors.reset + ' ')
        else:
            if lst[i] == 0:
                sys.stdout.write("  ")
            else:
                sys.stdout.write(str(lst[i]) + " ")
        if i % 27 == 26:
            if not i == 80:
                sys.stdout.write("\n" + ("-" * 21) + "\n")
                continue

        if i % 9 == 8:
            sys.stdout.write("\n")

        if i % 3 == 2:
            if not i % 9 == 8:
                sys.stdout.write("| ")


print_sud(active_game, 0)
print("\n\n\n")

x = 0
for i in range(11):
    for j in range(11):
        if i == 3 or i == 7:
            frame = tkinter.Frame(
                master=window,
                relief=tkinter.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            line = tkinter.Label(master=frame, width=3, justify="center", text="---", borderwidth=0)
            line.pack()

        else:
            frame = tkinter.Frame(
                    master=window,
                    relief=tkinter.RAISED,
                    borderwidth=1
                )

            frame.grid(row=i, column=j)
            if j == 3 or j == 7:
                frame.grid(row=i, column=j)
                line = tkinter.Label(master=frame, width=3, justify="center", text="|", borderwidth=0)
                line.pack()
            elif active_game[x] == 0:
                label = tkinter.Entry(master=frame, width=3, justify="center")
                label.insert(0, " ")
                label.pack()
                x += 1
            else:
                label = tkinter.Label(master=frame, width=3, justify="center", text=str(active_game[x]))
                label.pack()
                x += 1


window.mainloop()


running = True
while running:
    command = input(Colors.lineup + Colors.lineup + "\033[2KPlease enter command: ")
    command = command.split()

    if command[0] == "check":
        if active_game == active_game_solution:
            print(Colors.lineup + Colors.lineup + Colors.brightGreen + "\033[KCongratulations, you won!" + Colors.reset)
            finished = True
            continue
    if command[0] == "next":
        if finished:
            finished = False
            game = random.randint(0, len(all_games) - 1)
            active_game = all_games[game]
            active_game_solution = all_games_solution[game]
            continue
        else:
            sys.stdout.write("\033[K" + Colors.brightRed + "Please finish the Sudoku first\n" + Colors.reset)
            continue

    if command[0] == "exit":
        print("\033[K" + Colors.brightRed + "Exiting" + Colors.reset)
        time.sleep(2)
        running = False
        continue

    elif command[0] == "select":
        try:
            if 0 < int(command[1]) < 82:
                os.system('cls')
                print_sud(active_game, int(command[1]))
                sel = int(command[1])
                print(Colors.linedown * 2)
                print("\033[K" + Colors.brightGreen + 'Position ' + str(
                    command[1]) + ' successfully selected' + Colors.reset)
            else:
                sys.stdout.write("\033[K" + Colors.brightRed + 'No position ' + str(command[1]) + Colors.reset + '\n')
        except ValueError:
            sys.stdout.write("\033[K" + Colors.brightRed + 'Cannot select ' + str(command[1]) + Colors.reset + '\n')

    elif command[0] == "set":
        if sel != 0:
            if 0 <= int(command[1]) <= 9:
                active_game.pop(sel - 1)
                active_game.insert(sel - 1, int(command[1]))
                os.system('cls')
                print_sud(active_game, 0)
                print(Colors.linedown * 2)
                print("\033[K" + Colors.brightGreen + 'Position ' + str(sel) + ' successfully changed to: ' + str(
                    command[1]) + Colors.reset)
                sel = 0

            else:
                sys.stdout.write(
                    "\033[K" + Colors.brightRed + 'Please select a number from 1 to 9' + Colors.reset + '\n')
        else:
            sys.stdout.write("\033[K" + Colors.brightRed + 'No position selected' + Colors.reset + '\n')

    else:
        sys.stdout.write("\033[K" + Colors.brightRed + 'Command unknown' + Colors.reset + '\n')
