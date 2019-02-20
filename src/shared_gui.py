"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Kent Smith, Eddie Mannan, Cleo Barmes, and Ethan Mahn.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to drive the robot using sensors (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")
    go_straight_for_seconds_button = ttk.Button(frame, text="Drive using seconds")
    go_straight_for_inches_time_button = ttk.Button(frame, text="Drive using time")
    go_straight_for_inches_encoder_button = ttk.Button(frame, text="Drive using encoder")
    in_entry = ttk.Entry(frame)
    in_label = ttk.Label(frame, text="Inches:")
    sec_entry = ttk.Entry(frame)
    sec_label = ttk.Label(frame, text="Seconds:")
    sp_entry = ttk.Entry(frame)
    sp_label = ttk.Label(frame, text="Speed:")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    go_straight_for_seconds_button.grid(row=1, column=0)
    go_straight_for_inches_time_button.grid(row=2, column=0)
    go_straight_for_inches_encoder_button.grid(row=3, column=0)
    sec_entry.grid(row=1, column=2)
    sec_label.grid(row=1, column=1)
    in_entry.grid(row=2, column=2)
    in_label.grid(row=2, column=1)
    sp_entry.grid(row=3, column=2)
    sp_label.grid(row=3, column=1)

    # Set the Button callbacks:
    go_straight_for_seconds_button["command"] = lambda: handle_go_straight_seconds(mqtt_sender, sec_entry,sp_entry)
    go_straight_for_inches_time_button["command"] = lambda: handle_go_straight_inches_time(mqtt_sender, in_entry,sp_entry)
    go_straight_for_inches_encoder_button["command"] = lambda: handle_go_straight_inches_encoder(mqtt_sender, in_entry,sp_entry)

    return frame


def get_sound_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to execute certain sound functions (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sound")
    beep_button = ttk.Button(frame, text="Beep for number of times")
    tone_button = ttk.Button(frame, text="Play Tone for given duration")
    speak_button = ttk.Button(frame, text="Speak a phrase")
    freq_entry = ttk.Entry(frame)
    duration_entry = ttk.Entry(frame)
    num_entry = ttk.Entry(frame)
    phrase_entry = ttk.Entry(frame)
    freq_label = ttk.Label(frame, text="Frequency:")
    duration_label = ttk.Label(frame, text="Duration:")
    num_label = ttk.Label(frame, text="Number of times:")
    phrase_label = ttk.Label(frame, text="Phrase:")

    frame_label.grid(row=0, column=1)
    beep_button.grid(row=1, column=0)
    num_label.grid(row=1, column=1)
    num_entry.grid(row=1, column=2)
    tone_button.grid(row=2, column=0)
    freq_label.grid(row=2, column=1)
    freq_entry.grid(row=2, column=2)
    duration_label.grid(row=3, column=1)
    duration_entry.grid(row=3, column=2)
    speak_button.grid(row=4, column=0)
    phrase_label.grid(row=4, column=1)
    phrase_entry.grid(row=4, column=2)

    beep_button["command"] = lambda: handle_beep_number_of_times(mqtt_sender, num_entry)
    tone_button["command"] = lambda: handle_play_tone(mqtt_sender, freq_entry, duration_entry)
    speak_button["command"] = lambda: handle_speak(mqtt_sender, phrase_entry)

    return frame


def get_proximity_frame(window, mqtt_sender):

    # range
    # delta
    # button_drive_forward_until_in_range
    # button_drive_backward_until_out_of_range
    # button_drive_until_within_range_+_or_-_delta
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Proximity Sensor")
    forward_button = ttk.Button(frame, text="Drive Forward until in Range")
    backward_button = ttk.Button(frame, text="Drive Backward until out of Range")
    range_button = ttk.Button(frame, text="Drive until within Range +/- Delta")
    range_entry = ttk.Entry(frame)
    delta_entry = ttk.Entry(frame)
    range_label = ttk.Label(frame, text="Range:")
    delta_label = ttk.Label(frame, text="Delta:")
    speed_entry = ttk.Entry(frame)
    speed_label = ttk.Label(frame, text="Speed:")

    frame_label.grid(row=0, column=1)
    forward_button.grid(row=1, column=0)
    range_label.grid(row=1, column=1)
    range_entry.grid(row=1, column=2)
    backward_button.grid(row=2, column=0)
    delta_label.grid(row=2, column=1)
    delta_entry.grid(row=2, column=2)
    range_button.grid(row=3, column=0)
    speed_label.grid(row=3, column=1)
    speed_entry.grid(row=3, column=2)

    forward_button["command"] = lambda: handle_proximity_forward(mqtt_sender, range_entry, speed_entry)
    backward_button["command"] = lambda: handle_proximity_backward(mqtt_sender, range_entry, speed_entry)
    range_button["command"] = lambda: handle_proximity_range(mqtt_sender, range_entry, delta_entry, speed_entry)

    return frame


def get_color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Color Sensor")
    int_greater_button = ttk.Button(frame, text="Drive Forward until Intensity is Greater Than:")
    int_lesser_button = ttk.Button(frame, text="Drive Backward until Intensity is Less Than:")
    col_is_button = ttk.Button(frame, text="Drive until Color Is:")
    col_not_button = ttk.Button(frame, text="Drive until Color is Not:")
    intensity_entry = ttk.Entry(frame)
    color_entry = ttk.Entry(frame)
    intensity_label = ttk.Label(frame, text="Intensity:")
    color_label = ttk.Label(frame, text="Color:")
    speed_entry = ttk.Entry(frame)
    speed_label = ttk.Label(frame, text="Speed:")

    frame_label.grid(row=0, column=1)
    int_greater_button.grid(row=1, column=0)
    intensity_label.grid(row=1, column=1)
    intensity_entry.grid(row=1, column=2)
    int_lesser_button.grid(row=2, column=0)
    color_label.grid(row=2, column=1)
    color_entry.grid(row=2, column=2)
    col_is_button.grid(row=3, column=0)
    col_not_button.grid(row=4, column=0)
    speed_label.grid(row=3, column=1)
    speed_entry.grid(row=3, column=2)

    int_greater_button["command"] = lambda: handle_intensity_greater(mqtt_sender, intensity_entry, speed_entry)
    int_lesser_button["command"] = lambda: handle_intensity_lesser(mqtt_sender, intensity_entry, speed_entry)
    col_is_button["command"] = lambda: handle_color_is(mqtt_sender, color_entry, speed_entry)
    col_not_button["command"] = lambda: handle_color_not(mqtt_sender, color_entry, speed_entry)

    return frame


def get_camera_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Camera")
    cw_button = ttk.Button(frame, text="Spin Clockwise until Object Found")
    ccw_button = ttk.Button(frame, text="Spin Counterclockwise until Object Found")
    data_button = ttk.Button(frame, text="Camera Data")
    area_entry = ttk.Entry(frame)
    area_label = ttk.Label(frame, text="Object Area:")
    speed_entry = ttk.Entry(frame)
    speed_label = ttk.Label(frame, text="Speed:")

    frame_label.grid(row=0, column=1)
    cw_button.grid(row=1, column=0)
    area_label.grid(row=1, column=1)
    area_entry.grid(row=1, column=2)
    ccw_button.grid(row=2, column=0)
    data_button.grid(row=3, column=0)
    speed_label.grid(row=2, column=1)
    speed_entry.grid(row=2, column=2)

    cw_button["command"] = lambda: handle_camera_cw(mqtt_sender, area_entry, speed_entry)
    ccw_button["command"] = lambda: handle_camera_ccw(mqtt_sender, area_entry, speed_entry)
    data_button["command"] = lambda: handle_camera_data(mqtt_sender)

    return frame


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

    begin_button["command"] = lambda: handle_m3_proximity(
        mqtt_sender, initial_entry, delta_entry)
    return frame


def get_m1_dance_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Make the robot dance!")
    frame_label2 = ttk.Label(frame, text="Dance")
    disco_button = ttk.Button(frame, text="Disco")
    raise_the_roof_button = ttk.Button(frame, text="Raise the Roof")
    shake_button = ttk.Button(frame, text="Shake")
    spin_button = ttk.Button(frame, text="Spin")

    frame_label.grid(row=1, column=1)
    frame_label2.grid(row=0, column=1)
    disco_button.grid(row=2, column=0)
    raise_the_roof_button.grid(row=2, column=2)
    shake_button.grid(row=3, column=0)
    spin_button.grid(row=3, column=2)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################


###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop")
    mqtt_sender.send_message("stop")


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("raise_arm")
    mqtt_sender.send_message("raise_arm")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lower_arm")
    mqtt_sender.send_message("lower_arm")


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("calibrate_arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("move_arm_to_position")
    mqtt_sender.send_message("move_arm_to_position", [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()


###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################
def handle_go_straight_seconds(mqtt_sender, entry_box,entry_box2):
    """
    Tells the robot to go straight for a given amount of seconds
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
    """
    print("go straight for seconds")
    mqtt_sender.send_message("go_straight_for_seconds", [entry_box.get(), entry_box2.get()])


def handle_go_straight_inches_time(mqtt_sender, entry_box, entry_box2):
    """
    Tells the robot to go straight for a given amount of time
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
    """
    print("go straight for inches using time")
    mqtt_sender.send_message("go_straight_for_inches_using_time", [entry_box.get(), entry_box2.get()])


def handle_go_straight_inches_encoder(mqtt_sender, entry_box,entry_box2):
    """
    Tells the robot to go straight for a given amount of time
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
    """
    print("go straight for inches using encoder")
    mqtt_sender.send_message("go_straight_for_inches_using_encoder", [entry_box.get(), entry_box2.get()])


###############################################################################
# Handlers for Buttons in the Sound frame.
###############################################################################
def handle_beep_number_of_times(mqtt_sender, entry_box):
    """
    Tells the robot to go straight for a given amount of time
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
    """
    print("beep number of times")
    mqtt_sender.send_message("beep_number_of_times", [entry_box.get()])


def handle_play_tone(mqtt_sender, entry_box, entry_box2):
    """
    Tells the robot to go straight for a given amount of time
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("play tone")
    mqtt_sender.send_message("play_tone", [entry_box.get(), entry_box2.get()])


def handle_speak(mqtt_sender, entry_box):
    """
    Tells the robot to go straight for a given amount of time
      :type mqtt_sender: com.MqttClient
      :type entry_box: ttk.Entry
    """
    print("speak")
    mqtt_sender.send_message("speak", [entry_box.get()])

###############################################################################
# Handlers for Buttons in the Proximity frame.
###############################################################################

def handle_proximity_forward(mqtt_sender, entry_box1, entry_box2):
    """
    Tells the robot to go forward until within range using proximity sensor.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("use_proximity_to_move_forward")
    mqtt_sender.send_message("use_proximity_to_move_forward",
                             [entry_box1.get(), entry_box2.get()])


def handle_proximity_backward(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to go backward until out of range using proximity sensor.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("use_proximity_to_move_backward")
    mqtt_sender.send_message("use_proximity_to_move_backward",
                             [entry_box1.get(), entry_box2.get()])


def handle_proximity_range(mqtt_sender, entry_box1, entry_box2, entry_box3):
    """
     Tells the robot to go an exact range +/- the delta using proximity sensor.
       :type mqtt_sender: com.MqttClient
       :type entry_box1: ttk.Entry
       :type entry_box2: ttk.Entry
       :type entry_box3: ttk.Entry
     """
    print("use_proximity_to_move_exact_range")
    mqtt_sender.send_message("use_proximity_to_move_exact_range",
                             [entry_box1.get(), entry_box2.get(), entry_box3.get()])

###############################################################################
# Handlers for Buttons in the Color frame.
###############################################################################

def handle_intensity_greater(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to go until the reflected light intensity is greater than the given value.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("intensity_greater")
    mqtt_sender.send_message("intensity_greater",[entry_box1.get(), entry_box2.get()])

def handle_intensity_lesser(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to go until the reflected light intensity is less than the given value.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("intensity_lesser")
    mqtt_sender.send_message("intensity_lesser",[entry_box1.get(), entry_box2.get()])

def handle_color_is(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to go until the ground is the given color.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("color_is")
    mqtt_sender.send_message("color_is",[entry_box1.get(), entry_box2.get()])

def handle_color_not(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to go until the ground is not the given color.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("color_not")
    mqtt_sender.send_message("color_not",[entry_box1.get(), entry_box2.get()])

###############################################################################
# Handlers for Buttons in the Camera frame.
###############################################################################

def handle_camera_cw(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to spin clockwise until an object larger than the given area is found.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("camera_cw")
    mqtt_sender.send_message("camera_cw",[entry_box1.get(), entry_box2.get()])

def handle_camera_ccw(mqtt_sender, entry_box1, entry_box2):
    """
   Tells the robot to spin counterclockwise until an object larger than the given area is found.
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("camera_ccw")
    mqtt_sender.send_message("camera_ccw",[entry_box1.get(), entry_box2.get()])

def handle_camera_data(mqtt_sender):
    """
   Retrieves data about the object the camera sees
      :type mqtt_sender: com.MqttClient
      :type entry_box1: ttk.Entry
      :type entry_box2: ttk.Entry
    """
    print("camera_data")
    mqtt_sender.send_message("camera_data",[])

# m3

