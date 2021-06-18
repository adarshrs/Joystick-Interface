import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame as pg
import pygame.joystick as pj
from TextPrint import TextPrint

# ------ Logitech Gamepad F310 -------
# Left Joystick:
#       x: Axis 0
#       y: Axis 1
# Right Joystick:
#       x: Axis 3
#       y: Axis 4
# Triggers:
#       LT: Axis 2
#       RT: Axis 5
# Buttons:
#       A: Button 0
#       B: Button 1
#       X: Button 2
#       Y: Button 3
#       LB: Button 4
#       RB: Button 5
#       BACK: Button 6
#       START: Button 7
#       Left Joy Press: Button 9
#       Right Joy Press: Button 10
# D-Pad:
#       Left: Hat0 (-1, 0)
#       Right: Hat0 (1, 0)
#       Up: Hat0 (0, 1)
#       Down: Hat0 (0, -1)


class Joystick:
    def __init__(self):
        self.deviceID = -1
        pj.init()
        pg.init()

        print("Number of Joysticks Connected: ", pj.get_count(), "\n__________________________\n")
        if pj.get_init():
            if pj.get_count() == 0:
                print("No joystick connected!\n")
                return
            elif pj.get_count() == 1:
                self.deviceID = 0
            else:
                print("Connected joysticks: ")
                for i in range(0, pj.get_count()):
                    j = pj.Joystick(i)
                    print(i, ": ", j.get_name())
                    j.quit()
                while self.deviceID == -1:
                    joy_id = int(input("\nSelect joystick id: "))
                    if 0 <= joy_id < pj.get_count():
                        self.deviceID = joy_id
                        print("__________________________\n")
                    else:
                        print("Invalid ID")
        else:
            return

        self.joystick = pj.Joystick(self.deviceID)
        print("Linked joystick:", self.joystick.get_name())
        print("Number of axis: ", self.joystick.get_numaxes())
        print("Number of buttons: ", self.joystick.get_numbuttons())

        print("__________________________\n")

    def test_joystick(self):
        screen = pg.display.set_mode((500, 700))
        pg.display.set_caption(self.joystick.get_name())
        clock = pg.time.Clock()

        textPrint = TextPrint()

        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

            screen.fill("BLACK")
            textPrint.reset()

            for i in range(self.joystick.get_numaxes()):
                axis = self.joystick.get_axis(i)
                textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))

            for i in range(self.joystick.get_numbuttons()):
                button = self.joystick.get_button(i)
                textPrint.tprint(screen, "Button {:>2} value: {}".format(i, button))

            for i in range(self.joystick.get_numhats()):
                hat = self.joystick.get_hat(i)
                textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))

            pg.display.flip()
            clock.tick(20)

        pg.quit()

    def get_axis(self, num):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        return self.joystick.get_axis(num)

    def get_button(self, num):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        return self.joystick.get_button(num)

    def get_hat(self, num):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        return self.joystick.get_hat(num)
