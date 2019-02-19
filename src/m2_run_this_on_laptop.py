"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Eddie Mannan.
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

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    #teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proxy_frame, color_frame, camera_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    get_new_frame(main_frame, mqtt_sender)
#    def get_m2_beep_proxy_frame(window, mqtt_sender):
#        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#        frame.grid()
#        frame_label = ttk.Label(frame, text="Beep Proxy")
#        begin_button = ttk.Button(frame, text="Begin Beep_Proxy")
#        initial_entry = ttk.Entry(frame)
#        delta_entry = ttk.Entry(frame)
#        initial_label = ttk.Label(frame, text="Initial:")
#        delta_label = ttk.Label(frame, text="Delta:")
#        speed_label = ttk.Label(frame, text="Speed:")
#        speed_entry = ttk.Entry(frame)
#        frame_label.grid(row=0, column=1)
#        begin_button.grid(row=1, column=0)
#        initial_label.grid(row=1, column=1)
#        initial_entry.grid(row=1, column=2)
#        delta_label.grid(row=2, column=1)
#        delta_entry.grid(row=2, column=2)
#        speed_label.grid(row=3, column=1)
#        speed_entry.grid(row=3, column=2)
#        begin_button["command"] = lambda: handle_m2_beep_proximity(mqtt_sender, initial_entry, delta_entry, speed_entry)
#        return frame
#
#    def get_m2_beep_retrieve_frame(window, mqtt_sender):
#        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#        frame.grid()
#        frame_label = ttk.Label(frame, text="BEEP_Retrieve")
#        start_button = ttk.Button(frame, text="Start BEEP_Retrieve")
#        speed_entry = ttk.Entry(frame)
#        speed_label = ttk.Label(frame, text="Speed:")
#        state = tkinter.IntVar()
#        direction_check = ttk.Checkbutton(frame, variable=state)
#        direction_label = ttk.Label(frame, text="Clockwise?")
#        frame_label.grid(row=0, column=1)
#        start_button.grid(row=1, column=0)
#        speed_label.grid(row=1, column=1)
#        speed_entry.grid(row=1, column=2)
#        direction_label.grid(row=2, column=1)
#        direction_check.grid(row=2, column=2)
#        start_button["command"] = lambda: handle_m2_beep_retrieve(mqtt_sender, speed_entry, state)
#        return frame
#
#    beep_proxy_frame = get_m2_beep_proxy_frame(main_frame, mqtt_sender)
#    beep_retrieve_frame = get_m2_beep_retrieve_frame(main_frame, mqtt_sender)
#
#    # -------------------------------------------------------------------------
#    # Grid the frames.
#    # -------------------------------------------------------------------------
#    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proxy_frame, beep_proxy_frame, beep_retrieve_frame, color_frame, camera_frame)
#
#    # -------------------------------------------------------------------------
#    # The event loop:
#    # -------------------------------------------------------------------------
    root.mainloop()
#
#
#def get_shared_frames(main_frame, mqtt_sender):
#   teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
#   arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
#   control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
#   drive_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
#   sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
#   proxy_frame = shared_gui.get_proximity_frame(main_frame, mqtt_sender)
#   color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)
#   camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)
#
#   return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proxy_frame, color_frame, camera_frame
#
#
#def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame,
#                sound_frame, proxy_frame, beep_proxy_frame,
#                beep_retrieve_frame, color_frame, camera_frame):
#    teleop_frame.grid(row=0, column=0)
#    arm_frame.grid(row=1, column=0)
#    control_frame.grid(row=2, column=0)
#    drive_frame.grid(row=3, column=0)
#    sound_frame.grid(row=4, column=0)
#    proxy_frame.grid(row=0, column=1)
#    beep_proxy_frame.grid(row=1, column=1)
#    beep_retrieve_frame.grid(row=2, column=1)
#    color_frame.grid(row=3, column=1)
#    camera_frame.grid(row=4, column=1)
#
#
#def handle_m2_beep_proxy(mqtt_sender, entry_box1, entry_box2, entry_box3):
#    """
#     Tells the robot to go pick up an object,
#      beeping increasingly faster as it nears the object.
#       :type mqtt_sender: com.MqttClient
#       :type entry_box1: ttk.Entry
#       :type entry_box2: ttk.Entry
#       :type entry_box: ttk.Entry
#     """
#    print("m2_beep_proxy")
#    mqtt_sender.send_message("m2_beep_proxy", [entry_box1.get(), entry_box2.get(), entry_box3.get()])
#
#
#def handle_m2_beep_retrieve(mqtt_sender, entry_box, check):
#    """
#    Tells the robot to find an object, then to go pick up an object,
#      beeping increasingly faster as it nears the object.
#      :type mqtt_sender: com.MqttClient
#      :type entry_box: ttk.Entry
#      :type entry_box2: ttk.Entry
#    """
#    if check.get() == 1:
#        dir = "CW"
#    else:
#        dir = "CCW"
#    print("m2_beep_retrieve", dir, entry_box.get())
#    mqtt_sender.send_message("m2_beep_retrieve", [dir, entry_box.get()])


def get_new_frame(main_frame, mqtt_sender):
    find_homework = ttk.Button(main_frame, text="Find Math Homework")
    find_homework.grid()
    find_homework['command'] = lambda: mqtt_sender.send_message("m2_find_homework")

    find_games = ttk.Button(main_frame, text="Find Video Games")
    find_games.grid()
    find_games['command'] = lambda: mqtt_sender.send_message("m2_find_games")

    find_food = ttk.Button(main_frame, text="Find Food")
    find_food.grid()
    find_food['command'] = lambda: mqtt_sender.send_message("m2_find_food")

    go_to_sleep = ttk.Button(main_frame, text="Go to Sleep")
    go_to_sleep.grid()
    go_to_sleep['command'] = lambda: mqtt_sender.send_message("Go to Sleep")

    calibrate_arm = ttk.Button(main_frame, text="Calibrate Arm")
    calibrate_arm.grid()
    calibrate_arm['command'] = lambda: mqtt_sender.send_message("calibrate_arm")

    raise_arm = ttk.Button(main_frame, text="Raise Arm")
    raise_arm.grid()
    raise_arm['command'] = lambda: mqtt_sender.send_message("raise_arm")

    lower_arm = ttk.Button(main_frame, text="Lower Arm")
    lower_arm.grid()
    lower_arm['command'] = lambda: mqtt_sender.send_message("lower_arm")

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()

