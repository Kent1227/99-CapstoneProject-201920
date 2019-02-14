# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
#This is Cleo Barmes's sandbox. There better not be any other cats using my litt... I mean sandbox!
#Lets get that that bread!

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def go_forward_beeping(self, inital, delta):
    """
    Goes forward at the given speed until the robot is less than
    the given number of inches from the nearest object that it senses.
    """
    ps = InfraredProximitySensor(4)
    wait_time = ps.get_distance()
    self.go(20, 20)
    while ps.get_distance_in_inches() >= int(1):
        self.beep()
        break
    self.stop()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()