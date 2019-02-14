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
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    def get_m3_beep_proximity_frame(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="Beep Proximity")
        begin_button = ttk.Button(frame, text="Begin Beep_Proximity")
        initial_entry = ttk.Entry(frame)
        delta_entry = ttk.Entry(frame)
        initial_label = ttk.Label(frame, text="Range:")
        delta_label = ttk.Label(frame, text="Delta:")

        frame_label.grid(row=0, column=1)
        begin_button.grid(row=1, column=0)
        initial_label.grid(row=1, column=1)
        initial_entry.grid(row=1, column=2)
        delta_label.grid(row=2, column=1)
        delta_entry.grid(row=2, column=2)

        begin_button["command"] = lambda: handle_m3_beep_proximity(
            mqtt_sender, initial_entry, delta_entry)
        return frame

    def get_m3_beep_retrieve_frame(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="BEEP_Retrieve")
        start_button = ttk.Button(frame, text="Start BEEP_Retrieve")
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

        start_button["command"] = lambda: handle_m3_beep_retrieve(mqtt_sender, speed_entry, state)
        return frame

    def get_m3_led_proximity_frame(window, mqtt_sender):
        frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
        frame.grid()

        frame_label = ttk.Label(frame, text="LED_Proximity")
        start_button = ttk.Button(frame, text="Start LED_Proximity")
        initial_entry = ttk.Entry(frame)
        initial_label = ttk.Label(frame, text="Initial Rate:")
        delta_entry = ttk.Entry(frame)
        delta_label = ttk.Label(frame, text="Change in Rate:")

        frame_label.grid(row=0, column=1)
        start_button.grid(row=1, column=0)
        initial_label.grid(row=1, column=1)
        initial_entry.grid(row=1, column=2)
        delta_label.grid(row=2, column=1)
        delta_entry.grid(row=2, column=2)

        start_button["command"] = lambda: handle_m3_led_proximity(mqtt_sender, initial_entry, delta_entry)
        return frame

    def get_m3_led_retrieve_frame(window, mqtt_sender):
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

        start_button["command"] = lambda: handle_m3_led_retrieve(mqtt_sender, speed_entry, state)
        return frame

    beep_proximity_frame = get_m3_beep_proximity_frame(main_frame, mqtt_sender)
    beep_retrieve_frame = get_m3_beep_retrieve_frame(main_frame, mqtt_sender)
    led_proximity_frame = get_m3_led_proximity_frame(main_frame, mqtt_sender)
    led_retrieve_frame = get_m3_led_retrieve_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame,
                proximity_frame, beep_proximity_frame, beep_retrieve_frame, led_proximity_frame, led_retrieve_frame)

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

    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame


def grid_frames(teleop_frame, arm_frame, control_frame,drive_frame,
                sound_frame, proximity_frame, beep_proximity_frame,
                beep_retrieve_frame, led_proximity_frame,led_retrieve_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=3, column=0)
    sound_frame.grid(row=4, column=0)
    proximity_frame.grid(row=0, column=1)
    beep_proximity_frame.grid(row=1, column=1)
    beep_retrieve_frame.grid(row=2, column=1)
    led_proximity_frame.grid(row=3, column=1)
    led_retrieve_frame.grid(row=4, column=1)

def handle_m3_beep_proximity(mqtt_sender, entry_box1, entry_box2):
    """
     Tells the robot to go pick up an object,
      beeping increasingly faster as it nears the object.
       :type mqtt_sender: com.MqttClient
       :type entry_box1: ttk.Entry
       :type entry_box2: ttk.Entry
     """
    print("beep_proximity")
    mqtt_sender.send_message("beep_proximity",
                             [entry_box1.get(), entry_box2.get()])

def handle_m3_beep_retrieve(mqtt_sender, entry_box, check):
    """
    Tells the robot to find an object, then to go pick up an object,
      beeping increasingly faster as it nears the object.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    if check.get()==1:
        dir = "CW"
    else:
        dir = "CCW"
    print("beep_retrieve",entry_box.get(), dir)
    mqtt_sender.send_message("beep_retrieve", [entry_box.get(), dir])

def handle_m3_led_proximity(mqtt_sender, entry_box, entry_box2):
    """
    Tells the robot to go pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("led_proximity",entry_box.get(), entry_box2.get())
    mqtt_sender.send_message("led_proximity", [entry_box.get(), entry_box2.get()])

def handle_m3_led_retrieve(mqtt_sender, entry_box, check):
    """
    Tells the robot to find and then pick up an object, flashing leds to indicate closeness.
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    if check.get()==1:
        dir = "CW"
    else:
        dir = "CCW"
    print("led_retrieve",entry_box.get(), dir)
    mqtt_sender.send_message("led_retrieve", [entry_box.get(), dir])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()