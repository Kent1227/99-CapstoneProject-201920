"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Kent Smith.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


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
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
#
#   # -------------------------------------------------------------------------
#   # Sub-frames for the shared GUI that the team developed:
#   # -------------------------------------------------------------------------
#   teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, dance_frame = get_shared_frames(main_frame, mqtt_sender)
#
#   # -------------------------------------------------------------------------
#   # Frames that are particular to my individual contributions to the project.
#   # -------------------------------------------------------------------------
#   # DONE: Implement and call get_my_frames(...)

    get_my_frames(main_frame, mqtt_sender)

#   # -------------------------------------------------------------------------
#   # Grid the frames.
#   # -------------------------------------------------------------------------
#   grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, dance_frame)
#
#   # -------------------------------------------------------------------------
#   # The event loop:
#   # -------------------------------------------------------------------------
    root.mainloop()
#
#
# def get_shared_frames(main_frame, mqtt_sender):
#   teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
#   arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
#   control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
#   drive_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
#   sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
#   proximity_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)
#   dance_frame = shared_gui.get_m1_dance_frame(main_frame, mqtt_sender)
#
#   return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, dance_frame
#
#
# def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, dance_frame):
#   teleop_frame.grid(row=0, column=0)
#   arm_frame.grid(row=1, column=0)
#   control_frame.grid(row=2, column=0)
#   drive_frame.grid(row=3, column=0)
#   sound_frame.grid(row=0, column=1)
#   proximity_frame.grid(row=1, column=1)
#   dance_frame.grid(row=3, column=1)


def get_my_frames(main_frame, mqtt_sender):
    return shared_gui.get_m1_dance_frame(main_frame, mqtt_sender)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()
