import logging
import sys
import os
import time

os.system('color')

active_game = [1, 0, 0, 2, 0, 0, 3, 0, 0,
               4, 0, 0, 5, 0, 0, 6, 0, 0,
               7, 0, 0, 8, 0, 0, 9, 0, 0,

               1, 0, 0, 2, 0, 0, 3, 0, 0,
               4, 0, 0, 5, 0, 0, 6, 0, 0,
               7, 0, 0, 8, 0, 0, 9, 0, 0,

               1, 0, 0, 2, 0, 0, 3, 0, 0,
               4, 0, 0, 5, 0, 0, 6, 0, 0,
               7, 0, 0, 8, 0, 0, 9, 0, 0]


class Colors:
    reversd = '\u001b[7m'
    brightGreen = '\u001b[32;1m'
    brightRed = '\u001b[31;1m'
    reset = '\u001b[0m'
    lineup = '\033[A'
    linedown = '\033[B'


def print_sud(lst: list, hailait: int):
    for i in range(0, 81):
        if i == hailait - 1:
            sys.stdout.write(Colors.reversd + str(lst[i]) + Colors.reset + ' ')
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

sel = 0

running = True
while running:
    command = input(Colors.lineup + Colors.lineup + "\033[2KPlease enter command: ")
    command = command.split()

    if command[0] == "exit":
        print("\033[K" + Colors.brightRed + "Exiting" + Colors.reset)
        time.sleep(2)
        running = False

    elif command[0] == "select":
        try:
            if 0 < int(command[1]) < 82:
                os.system('cls')
                print_sud(active_game, int(command[1]))
                sel = int(command[1])
                print(Colors.linedown * 2)
                print("\033[K" + Colors.brightGreen + 'Position ' + str(command[1]) + ' successfully selected' + Colors.reset)
            else:
                sys.stdout.write("\033[K" + Colors.brightRed + 'No position ' + str(command[1]) + Colors.reset + '\n')
        except ValueError:
            sys.stdout.write("\033[K" + Colors.brightRed + 'Cannot select ' + str(command[1]) + Colors.reset + '\n')

    elif command[0] == "set":
        if sel != 0:
            if 0 < int(command[1]) < 10:
                active_game.pop(sel - 1)
                active_game.insert(sel - 1, int(command[1]))
                os.system('cls')
                print_sud(active_game, 0)
                print(Colors.linedown * 2)
                print("\033[K" + Colors.brightGreen + 'Position ' + str(sel) + ' successfully changed to: ' + str(command[1]) + Colors.reset)
                sel = 0

            else:
                sys.stdout.write("\033[K" + Colors.brightRed + 'Please select a number from 1 to 9' + Colors.reset + '\n')
        else:
            sys.stdout.write("\033[K" + Colors.brightRed + 'No position selected' + Colors.reset + '\n')

    else:
        sys.stdout.write("\033[K" + Colors.brightRed + 'Command unknown' + Colors.reset + '\n')
