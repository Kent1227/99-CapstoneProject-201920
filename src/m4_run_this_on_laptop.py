"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Ethan Mahn.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui

def main():
    basic()
    # chess()


def chess():
    mqtt_sender = com.MqttClient()  # Empty parentheses = sender (filled means reciever)
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Chess GUI")
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
        update_state(t, tkinter.IntVar(value=1), state)
    else:
        print("This space is empty!")
def update_state(loc,new,state):
    j=int(loc[0])
    k=int(loc[1])
    state[j][k]=new

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

def handle_calibrate_go():
    print("Calibrate True")

def handle_locate():
    print("Acquire Location")
    mqtt_sender.send_message("m4_led_retrieve", [dir, entry_box.get()])






# -----------------------------------------------------------------------------
# Code for basic GUI
# -----------------------------------------------------------------------------

def basic():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient() #Empty parentheses = sender (filled means reciever)
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE120 Capstone Project (EV3)")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame,camera_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    def get_m4_led_proximity_frame(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="LED_Proximity")
        start_button = ttk.Button(frame, text="Start LED_Proximity")
        initial_entry = ttk.Entry(frame)
        initial_label = ttk.Label(frame, text="Initial Rate:")
        delta_entry = ttk.Entry(frame)
        delta_label = ttk.Label(frame, text="Change in Rate:")
        speed_entry = ttk.Entry(frame)
        speed_label = ttk.Label(frame, text="Speed:")

        frame_label.grid(row=0, column=1)
        start_button.grid(row=1, column=0)
        initial_label.grid(row=1, column=1)
        initial_entry.grid(row=1, column=2)
        delta_label.grid(row=2, column=1)
        delta_entry.grid(row=2, column=2)
        speed_label.grid(row=3, column=1)
        speed_entry.grid(row=3, column=2)

        start_button["command"] = lambda: handle_m4_led_proximity(mqtt_sender, initial_entry, delta_entry,speed_entry)
        return frame

    def get_m4_led_retrieve_frame(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="LED_Retrieve")
        start_button = ttk.Button(frame, text="Start LED_Retrieve")
        speed_entry = ttk.Entry(frame)
        speed_label = ttk.Label(frame, text="Speed:")
        state=tkinter.IntVar()
        direction_check = ttk.Checkbutton(frame,variable=state)
        direction_label = ttk.Label(frame,text="Clockwise?")

        frame_label.grid(row=0, column=1)
        start_button.grid(row=1, column=0)
        speed_label.grid(row=1, column=1)
        speed_entry.grid(row=1, column=2)
        direction_label.grid(row=2, column=1)
        direction_check.grid(row=2, column=2)

        start_button["command"] = lambda: handle_m4_led_retrieve(mqtt_sender, speed_entry, state)
        return frame

    led_proximity_frame = get_m4_led_proximity_frame(main_frame, mqtt_sender)
    led_retrieve_frame = get_m4_led_retrieve_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, led_proximity_frame, led_retrieve_frame, color_frame,camera_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    drive_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame,mqtt_sender)
    proximity_frame = shared_gui.get_proximity_frame(main_frame,mqtt_sender)
    color_frame = shared_gui.get_color_frame(main_frame,mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame,mqtt_sender)
    return teleop_frame,arm_frame,control_frame,drive_frame,sound_frame,proximity_frame,color_frame,camera_frame

def grid_frames(teleop_frame, arm_frame, control_frame,drive_frame,sound_frame,proximity_frame,led_proximity_frame,led_retrieve_frame,color_frame,camera_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    sound_frame.grid(row=3, column=0)
    drive_frame.grid(row=0, column=1)
    proximity_frame.grid(row=1, column=1)
    led_proximity_frame.grid(row=1, column=2)
    led_retrieve_frame.grid(row=2, column=2)
    color_frame.grid(row=2, column=1)
    camera_frame.grid(row=3,column=1)

# -----------------------------------------------------------------------------
# Handles for m4 features:
# -----------------------------------------------------------------------------

def handle_m4_led_proximity(mqtt_sender, entry_box, entry_box2,entry_box3):
    """
    Tells the robot to go pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("m4_led_proximity",entry_box.get(), entry_box2.get(),entry_box3.get())
    mqtt_sender.send_message("m4_led_proximity", [entry_box.get(), entry_box2.get(),entry_box3.get()])

def handle_m4_led_retrieve(mqtt_sender, entry_box, check):
    """
    Tells the robot to find and then pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    if check.get()==0:
        dir = "CCW"
    else:
        dir = "CW"
    print("m4_led_retrieve", dir, entry_box.get())
    mqtt_sender.send_message("m4_led_retrieve", [dir, entry_box.get()])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()