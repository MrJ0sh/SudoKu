import tkinter

active_game = [0, 3, 7, 1, 0, 6, 4, 9, 8,
               1, 2, 0, 8, 9, 0, 3, 7, 0,
               8, 0, 9, 3, 4, 7, 0, 2, 5,

               0, 8, 3, 0, 5, 4, 2, 0, 9,
               2, 4, 0, 6, 3, 0, 0, 8, 7,
               9, 0, 5, 2, 1, 8, 6, 4, 3,

               0, 1, 8, 0, 6, 3, 9, 0, 2,
               3, 0, 2, 9, 0, 1, 7, 6, 4,
               4, 9, 0, 5, 7, 2, 0, 3, 1]
window = tkinter.Tk()

x = 0
for i in range(9):
    for j in range(9):
        frame = tkinter.Frame(
            master=window,
            relief=tkinter.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        if active_game[x] == 0:
            label = tkinter.Label(master=frame, text=" ")
            label.pack()
            x += 1
        else:
            label = tkinter.Label(master=frame, text=str(active_game[x]))
            label.pack()
            x += 1

window.mainloop()
