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
    # basic()
    chess()


def chess():
    """Main function for the chess program. Setup and GUI."""
    mqtt_sender = com.MqttClient(FromRobot)  # Empty parentheses = sender (filled means reciever)
    mqtt_sender.mqtt = mqtt_sender
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Chess GUI")
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()
    board, command, misc = get_gui(main_frame, mqtt_sender)
    build_gui(board, command, misc)
    handle_init(mqtt_sender)
    root.mainloop()


class FromRobot(object):
    """MQTT reciever to get updates from robot."""

    def __init__(self, mqtt=None):
        self.mqtt = mqtt
        self.leave = False

    def update_location(self, loc):
        self.mqtt.robopos[0] = loc[0]
        self.mqtt.robopos[1] = loc[1]

    def remote_init(self):
        self.mqtt.robopos = [3, 0, 1]


# GUI construction functions
def get_gui(window, mqtt_sender):
    """Generates the tkinter gui."""
    board = get_board_frame(window, mqtt_sender)
    command = get_command_frame(window, mqtt_sender)
    misc = get_misc_frame(window, mqtt_sender)
    return board, command, misc


def build_gui(board, command, misc):
    """Puts the tkinter GUI on the main window. Procedurally generates the chessboard and builds the array that tracks the locations of pieces."""
    board.grid(row=0, column=0)
    command.grid(row=0, column=1)
    misc.grid(row=0, column=2)


def get_board_frame(window, mqtt_sender):
    """Builds the chessboard GUI."""
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Board")
    get_state = ttk.Button(frame, text="Get state")
    get_state["command"] = lambda: handle_get_state(mqtt_sender)
    mqtt_sender.state = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
    box = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    frame_label.grid()
    get_state.grid()
    hint = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H"}
    for k in range(8):
        note = ttk.Label(frame, text=str(hint[str(k)]))
        note.grid(row=0, column=k + 2)
    for j in range(2):
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=1)
        for k in range(8):
            mqtt_sender.state[j][k] = tkinter.IntVar(value=1)
            box[j][k] = ttk.Checkbutton(frame, variable=mqtt_sender.state[j][k])
            box[j][k].grid(row=j + 1, column=k + 2)
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=10)
    for j in range(2, 6):
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=1)
        for k in range(8):
            mqtt_sender.state[j][k] = tkinter.IntVar()
            box[j][k] = ttk.Checkbutton(frame, variable=mqtt_sender.state[j][k])
            box[j][k].grid(row=j + 1, column=k + 2)
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=10)
    for j in range(6, 8):
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=1)
        for k in range(8):
            mqtt_sender.state[j][k] = tkinter.IntVar(value=1)
            box[j][k] = ttk.Checkbutton(frame, variable=mqtt_sender.state[j][k])
            box[j][k].grid(row=j + 1, column=k + 2)
        note = ttk.Label(frame, text=str(j + 1))
        note.grid(row=j + 1, column=10)
        for k in range(8):
            note = ttk.Label(frame, text=str(hint[str(k)]))
            note.grid(row=10, column=k + 2)
    return frame


def get_command_frame(window, mqtt_sender):
    """Builds the frame for sending commands/inputting moves."""
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
    submit["command"] = lambda: handle_submit(mqtt_sender, to_entry.get(), from_entry.get())
    submit.grid()
    return frame


def get_misc_frame(window, mqtt_sender):
    """Builds the gui of miscelaneous functions."""
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Calibration")
    frame_label.grid()
    calibrate_arm = ttk.Button(frame, text="Calibrate Arm")
    calibrate_arm["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    calibrate_arm.grid()
    locate = ttk.Button(frame, text="Acquire Location")
    locate["command"] = lambda: handle_locate(mqtt_sender)
    locate.grid()
    loc_label = ttk.Label(frame, text="Robot Location")
    loc_label.grid()
    loc = ttk.Entry(frame)
    loc.grid()
    roboloc = ttk.Button(frame, text="Set Robot Location")
    roboloc["command"] = lambda: handle_roboloc(loc.get(), mqtt_sender)
    roboloc.grid()
    init = ttk.Button(frame, text="Reset Robot")
    init["command"] = lambda: handle_init(mqtt_sender)
    init.grid()
    return frame


# Primary functions
def handle_get_state(mqtt_sender):
    """Prints the current state of the board and the robot's location information."""
    for j in range(8):
        for k in range(8):
            print(mqtt_sender.state[j][k].get(), end=" ")
        print()
    print()
    print(mqtt_sender.robopos)


def handle_submit(mqtt_sender, to, fro):
    """Runs the proper commands to execute the move the user put in."""
    let_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    t = [int(to[1]) - 1, let_num[to[0]]]
    f = [int(fro[1]) - 1, let_num[fro[0]]]
    if mqtt_sender.state[f[0]][f[1]].get() == 1:
        if mqtt_sender.state[t[0]][t[1]].get() == 1:
            print("Piece captured!")
            update_state(t, tkinter.IntVar(value=0), mqtt_sender.state)
            retrieve_piece(t, mqtt_sender)
            dispose(mqtt_sender)
        update_state(f, tkinter.IntVar(value=0), mqtt_sender.state)
        retrieve_piece(f, mqtt_sender)
        place_piece(t, mqtt_sender)
        update_state(t, tkinter.IntVar(value=1), mqtt_sender.state)
    else:
        print("This space is empty!")
    print("Move executed!")


def update_state(loc, new, state):
    """Changes the filled state of the given space."""
    j = int(loc[0])
    k = int(loc[1])
    state[j][k] = new


# Pathfinding functions
def pathfind(start, end, state):
    """Finds the robot's path from one space to another, as a series of spaces that it will
     pass through (outputs list, alternating x/y coordinates of each space in the sequence)."""
    current = start
    obs = 0
    trail = []
    while True:
        trail += current
        if current == end:
            print("Target found!")
            break
        current, change = path(current, end, state, obs % 2)
        if change != True:
            print("Obstruction!")
            obs += 1
        if obs > 5:
            print("Stuck!")
            break
    print(trail)
    return trail


def path(current, end, state, obs):
    """Used in pathfinding for finding new spaces to move to. Alternates between prioritized axes upon finding obstruction (detected in pathfinding)."""
    change = False
    if obs == 0:
        current, change = check_y_path(current, end, state)
        if change != True:
            current, change = check_x_path(current, end, state)
    elif dir == 1:
        current, change = check_x_path(current, end, state)
        if change != True:
            current, change = check_y_path(current, end, state)
    return current, change


def check_y_path(current, end, state):
    """Tells the robot to change spaces on the y axis."""
    change = False
    if current[0] < end[0] and state[current[0] + 1][current[1]].get() == 0:
        current[0] += 1
        change = True
    elif current[0] > end[0] and state[current[0] - 1][current[1]].get() == 0:
        current[0] -= 1
        change = True
    return current, change


def check_x_path(current, end, state):
    """Tells the robot to change spaces on the x axis."""
    change = False
    if current[1] > end[1] and state[current[0]][current[1] - 1].get() == 0:
        current[1] -= 1
        change = True
    elif current[1] < end[1] and state[current[0]][current[1] + 1].get() == 0:
        current[1] += 1
        change = True
    return current, change


def path_dir(path):
    """Converts the space coordinates given by pathfind into movement directions (0:N, 1:E, 2:S, 3:W)."""
    commands = []
    for k in range(0, len(path) - 3, 2):
        if path[k] > path[k + 2]:
            commands += [0]
        elif path[k] < path[k + 2]:
            commands += [2]
        else:
            if path[k + 1] > path[k + 3]:
                commands += [3]
            elif path[k + 1] < path[k + 3]:
                commands += [1]
    print(commands)
    return commands


def dir_com(dir, initial):
    """converts the movement directions from path_dir into actual movements/commands the robot can make."""
    commands = []
    if dir[0] - initial == 0:
        pass
    elif dir[0] - initial == 1 or dir[0] - initial == -3:
        commands += ["right"]
    elif dir[0] - initial == 2 or dir[0] - initial == -2:
        commands += ["reverse"]
    elif dir[0] - initial == 3 or dir[0] - initial == -1:
        commands += ["left"]
    for k in range(len(dir) - 1):
        if dir[k] - dir[k + 1] == 0:
            commands += ["straight"]
        elif dir[k] - dir[k + 1] == 1 or dir[k] - dir[k + 1] == -3:
            commands += ["straight"]
            commands += ["left"]
        elif dir[k] - dir[k + 1] == 2 or dir[k] - dir[k + 1] == -2:
            commands += ["straight"]
            commands += ["reverse"]
        elif dir[k] - dir[k + 1] == 3 or dir[k] - dir[k + 1] == -1:
            commands += ["straight"]
            commands += ["right"]
    commands += ["straight"]
    print(commands)
    return commands, dir[-1]


# Action functions
def retrieve_piece(target, mqtt_sender):
    """Runs the commands to have the robot move and pick up a piece."""
    print(target, mqtt_sender.robopos)
    path = pathfind([mqtt_sender.robopos[0], mqtt_sender.robopos[1]], target, mqtt_sender.state)
    dir = path_dir(path)
    coms = list(dir_com(dir, mqtt_sender.robopos[2]))
    print(coms)
    del coms[-1]
    del coms[0][-1]
    print(coms)
    mqtt_sender.send_message("retrieve_piece", [coms])
    mqtt_sender.robopos = [path[-4], path[-3], dir[-1]]
    print(target, mqtt_sender.robopos)


def place_piece(target, mqtt_sender):
    """Runs the commands to have the robot move and place a piece it's holding."""
    print(target, mqtt_sender.robopos)
    path = pathfind([mqtt_sender.robopos[0], mqtt_sender.robopos[1]], target, mqtt_sender.state)
    dir = path_dir(path)
    coms = list(dir_com(dir, mqtt_sender.robopos[2]))
    print(coms)
    del coms[-1]
    del coms[0][-1]
    print(coms)
    mqtt_sender.send_message("place_piece", [coms])
    mqtt_sender.robopos = [path[-4], path[-3], dir[-1]]
    print(target, mqtt_sender.robopos)


def dispose(mqtt_sender):
    """Runs the commands to have the robot dispose (remove from the board) of the piece its holding."""
    target = find_dump(mqtt_sender)
    print(target, mqtt_sender.robopos)
    path = pathfind([mqtt_sender.robopos[0], mqtt_sender.robopos[1]], target, mqtt_sender.state)
    dir = path_dir(path)
    coms = dir_com(dir, mqtt_sender.robopos[2])
    mqtt_sender.send_message("dispose_piece", [coms])
    mqtt_sender.robopos = [target[0], target[1], dir[-1]]
    print(target, mqtt_sender.robopos)


def find_dump(mqtt_sender):
    """Finds the target space for disposing of captured pieces."""
    target = [0, 0]
    while True:
        if target[0] > 7:
            break
        elif mqtt_sender.state[target[0]][0].get() == 1:
            target[0] += 1
        elif mqtt_sender.state[target[0]][0].get() == 0:
            break
    print(target)
    return target


# Miscelaneous functions
def handle_roboloc(loc, mqtt_sender):
    """Sets the location of the robot"""
    mqtt_sender.robopos[0] = loc[0]
    mqtt_sender.robopos[1] = loc[1]
    mqtt_sender.robopos[2] = loc[2]


def handle_locate(mqtt_sender):
    """Has the robot find its location again."""
    print("Acquire Location")
    mqtt_sender.send_message("locate", [])


def handle_init(mqtt_sender):
    """Resets the robot's position to default."""
    print("Robot reset")
    mqtt_sender.robopos = [4, 0, 1]


def handle_calibrate_arm(mqtt_sender):
    """Tells the robot to calibrate the arm."""
    print("Calibrate Arm")
    mqtt_sender.send_message("calibrate_arm", [])


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
    mqtt_sender = com.MqttClient()  # Empty parentheses = sender (filled means reciever)
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
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame, camera_frame = get_shared_frames(
        main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    def get_m4_led_proximity_frame(window, mqtt_sender):
        """Builds the Basic GUi frame for the led_proximity function"""
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

        start_button["command"] = lambda: handle_m4_led_proximity(mqtt_sender, initial_entry, delta_entry, speed_entry)
        return frame

    def get_m4_led_retrieve_frame(window, mqtt_sender):
        """Builds the Basic GUi frame for the led_retrieve function"""
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="LED_Retrieve")
        start_button = ttk.Button(frame, text="Start LED_Retrieve")
        speed_entry = ttk.Entry(frame)
        speed_label = ttk.Label(frame, text="Speed:")
        state = tkinter.IntVar()
        direction_check = ttk.Checkbutton(frame, variable=state)
        direction_label = ttk.Label(frame, text="Clockwise?")

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

    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, led_proximity_frame,
                led_retrieve_frame, color_frame, camera_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
    proximity_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame, camera_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, led_proximity_frame,
                led_retrieve_frame, color_frame, camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    sound_frame.grid(row=3, column=0)
    drive_frame.grid(row=0, column=1)
    proximity_frame.grid(row=1, column=1)
    led_proximity_frame.grid(row=1, column=2)
    led_retrieve_frame.grid(row=2, column=2)
    color_frame.grid(row=2, column=1)
    camera_frame.grid(row=3, column=1)


# -----------------------------------------------------------------------------
# Handlers for m4 features:
# -----------------------------------------------------------------------------

def handle_m4_led_proximity(mqtt_sender, entry_box, entry_box2, entry_box3):
    """
    Tells the robot to go pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("m4_led_proximity", entry_box.get(), entry_box2.get(), entry_box3.get())
    mqtt_sender.send_message("m4_led_proximity", [entry_box.get(), entry_box2.get(), entry_box3.get()])


def handle_m4_led_retrieve(mqtt_sender, entry_box, check):
    """
    Tells the robot to find and then pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    if check.get() == 0:
        dir = "CCW"
    else:
        dir = "CW"
    print("m4_led_retrieve", dir, entry_box.get())
    mqtt_sender.send_message("m4_led_retrieve", [dir, entry_box.get()])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
