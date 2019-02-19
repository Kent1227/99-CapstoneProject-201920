# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
# Author: Ethan Mahn
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Chess GUI")

# -------------------------------------------------------------------------
# The main frame, upon which the other frames are placed.
# -------------------------------------------------------------------------
def main():
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()
    state, board, command, misc = get_gui(main_frame)
    build_gui(board, command, misc)
    root.mainloop()

def get_gui(window):
    board, state = get_board_frame(window)
    command = get_command_frame(window,state)
    misc = get_misc_frame(window)
    return state, board, command, misc

def build_gui(board, command, misc):
    board.grid()
    command.grid()
    misc.grid()

def get_board_frame(window):
    # builds the chessboard gui
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Board")
    get_state = ttk.Button(frame, text="Get state")
    get_state["command"] = lambda: handle_get_state(state)
    state = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    box = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    frame_label.grid()
    get_state.grid()
    hint = {"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H"}
    for k in range(8):
        note = ttk.Label(frame, text=str(hint[str(k)]))
        note.grid(row=0, column=k+2)
    for j in range(2):
        note = ttk.Label(frame, text=str(j+1))
        note.grid(row=j+1, column=1)
        for k in range(8):
            state[j][k] = tkinter.IntVar(value=1)
            box[j][k] = ttk.Checkbutton(frame, variable=state[j][k])
            box[j][k].grid(row=j+1,column=k+2)
        note = ttk.Label(frame, text=str(j+1))
        note.grid(row=j+1, column=10)
    for j in range(2,6):
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=1)
        for k in range(8):
            state[j][k] = tkinter.IntVar()
            box[j][k] = ttk.Checkbutton(frame, variable=state[j][k])
            box[j][k].grid(row=j+1,column=k+2)
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=10)
    for j in range(6,8):
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=1)
        for k in range(8):
            state[j][k] = tkinter.IntVar(value=1)
            box[j][k] = ttk.Checkbutton(frame, variable=state[j][k])
            box[j][k].grid(row=j+1,column=k+2)
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=10)
        for k in range(8):
            note = ttk.Label(frame, text=str(hint[str(k)]))
            note.grid(row=10, column=k + 2)
    return frame,state
def get_command_frame(window,state):
    # builds the command gui
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Commands")
    frame_label.grid()
    from_label = ttk.Label(frame, text="Move from:")
    from_entry = ttk.Entry(frame)
    from_label.grid()
    from_entry.grid()
    to_label = ttk.Label(frame, text="Move to:")
    to_entry = ttk.Entry(frame)
    to_label.grid()
    to_entry.grid()
    submit = ttk.Button(frame, text="Submit")
    submit["command"]=lambda: handle_submit(to_entry.get(),from_entry.get(),state)
    submit.grid()

    return frame
def get_misc_frame(window):
    # builds the gui of miscelaneous functions
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Miscelaneous")
    frame_label.grid()
    calibrate_go = ttk.Button(frame, text="Calibrate Go")
    calibrate_go["command"] = lambda: handle_calibrate_go()
    calibrate_go.grid()
    locate = ttk.Button(frame, text="Acquire Location")
    locate["command"] = lambda: handle_locate()
    locate.grid()

    return frame


def handle_get_state(state):
    for j in range(8):
        for k in range(8):
            print(state[j][k].get(),end=" ")
        print()
    print()
def handle_submit(to,fro,state):
    let_num = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
    t = [int(to[1])-1,let_num[to[0]]]
    f = [int(fro[1])-1,let_num[fro[0]]]
    if state[f[0]][f[1]].get() == 1:
        update_state(f, tkinter.IntVar(value=0), state)
        if state[t[0]][t[1]].get() == 1:
            print("Piece captured!")
        pathfind(f, t, state)
        update_state(t, tkinter.IntVar(value=1), state)
    else:
        print("This space is empty!")
def update_state(loc,new,state):
    j=int(loc[0])
    k=int(loc[1])
    state[j][k]=new


def handle_calibrate_go():
    print("Calibrate True")
def handle_locate():
    print("Acquire Location")


def pathfind(start, end, state):
    # Finds the robot's path from one space to another.
    print(start)
    print(end)
    current = start
    changex = False
    trail = []
    while True:
        trail += current
        if current == end:
            print("Target found!")
            break
        print(current[0], " ", end[0], " ", state[current[0]+1][current[1]].get(), " ", state[current[0]-1][current[1]].get())
        print(current[1], " ", end[1], " ", state[current[0]][current[1] - 1].get(), " ", state[current[0]][current[1] + 1].get())
        current, changey = check_y_path(current, end, state)
        if changey != True:
            current, changex = check_x_path(current, end, state)
        if changex != True and changey != True:
            print("Obstruction!")
            break
        print("again")
    print(trail)
    return trail
def check_y_path(current, end, state):
    # Tells the robot to change spaces on the y axis.
    change = False
    if current[0] < end[0] and state[current[0] + 1][current[1]].get() == 0:
        current[0] += 1
        change = True
    elif current[0] > end[0] and state[current[0] - 1][current[1]].get() == 0:
        current[0] -= 1
        change = True
    return current, change
def check_x_path(current, end, state):
    # Tells the robot to change spaces on the y axis.
    change = False
    if current[1] > end[1] and state[current[0]][current[1] - 1].get() == 0:
        current[1] -= 1
        axis = 1
        change = True
    elif current[1] < end[1] and state[current[0]][current[1] + 1].get() == 0:
        current[1] += 1
        axis = 1
        change = True
    return current, change


main()