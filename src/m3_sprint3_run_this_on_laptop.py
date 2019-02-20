"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Cleo Barmes.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
from tkinter import *
import shared_gui
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE120 Capstone Project")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = tkinter.Frame(root, borderwidth=50, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_and_claw_frame, control_frame = get_shared_frames(main_frame, mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    def get_baby_robot(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=10, relief="ridge")
        frame.grid()

        colors = {'blue', 'red', 'green', 'yellow', 'purple', 'light blue'}
        tkvar = StringVar(root)

        frame_label = ttk.Label(frame, text="Baby Robot")
        begin_button = ttk.Button(frame, text="Wake Up Baby")
        speed_label = ttk.Label(frame, text="Speed:")
        speed_slider = ttk.Scale(frame, from_=10, to=100)
        hunger_meter = ttk.Progressbar(frame)
        hunger_label = ttk.Label(frame, text="Baby's Hunger")
        color_change = ttk.OptionMenu(frame, tkvar, *colors)
        color_button = ttk.Button(frame, text="Change Color")

        frame_label.grid(row=0, column=1)
        begin_button.grid(row=3, column=1)
        speed_label.grid(row=2, column=0)
        speed_slider.grid(row=2, column=1)
        hunger_label.grid(row=1, column=0)
        hunger_meter.grid(row=1, column=1)
        color_change.grid(row=4, column=2)
        color_button.grid(row=4, column=1)

        main_frame.configure(background=tkvar.get())

        color_button["command"] = lambda: handle_change_color(main_frame, tkvar)
        begin_button["command"] = lambda: handle_baby_robot(
            mqtt_sender, speed_slider, hunger_meter, root)
        return frame

    baby_robot_frame = get_baby_robot(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_and_claw_frame, control_frame, baby_robot_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()


#accessing shared frames from shared gui
def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_and_claw_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_and_claw_frame, control_frame


#placing all frames onto the grid
def grid_frames(teleop_frame, arm_and_claw_frame, control_frame, baby_robot_frame):
    teleop_frame.grid(row=0, column=0)
    arm_and_claw_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    baby_robot_frame.grid(row=3, column=0)


def handle_baby_robot(mqtt_sender, scale, hunger_meter, root):
    """
     Tells the robot to go pick up an object,
      beeping increasingly faster as it nears the object.
       :type mqtt_sender: com.MqttClient
       :type scale: ttk.scale
       :type int: current progress of hunger_meter
     """
    print("m3_baby_robot")

    hunger_meter['maximum'] = 100
    progress_state = Progress_state()
    get_progress(mqtt_sender, progress_state, hunger_meter, root, scale)


def get_progress(mqtt_sender, progress_state, hunger_meter, root, scale):
    hunger_meter["value"] = (progress_state.progress_state)
    hunger_meter.update()

    mqtt_sender.send_message("m3_baby_robot", [scale.get(), progress_state.progress_state])

    if hunger_meter["value"] > 0:
        progress_state.progress_state = progress_state.progress_state - 1
        root.after(1000, lambda: get_progress(mqtt_sender, progress_state, hunger_meter, root, scale))
    else:
        mqtt_sender.send_message("sleep_time")
        exit()

class Progress_state(object):
    def __init__(self):
        self.progress_state = 100

def handle_change_color(main_frame, tkvar):
    main_frame.configure(background=tkvar.get())

#resets the progress bar to 100, showing that the baby has been fed.
def fed(progress_state):
    progress_state.progress_state = 100

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()