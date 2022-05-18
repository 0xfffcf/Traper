from cheats import client
from cheat import Cheat

from time import sleep

import keyboard


class ThirdPerson(Cheat):
    """Press \ to toggle third-person on/off"""
    def third_person(self):
        client.offset.get_third_person_offset()
        try:
            is_third_person = client.process.read_int(client.local_player + client.offset.M_I_OBSERVER_MODE)
        except:
            exit(1)

        while True:
            if not keyboard.is_pressed('\\'):
                return

            if is_third_person == 0:
                client.process.write_int(client.local_player + client.offset.M_I_OBSERVER_MODE, 1)
            elif is_third_person == 1:
                client.process.write_int(client.local_player + client.offset.M_I_OBSERVER_MODE, 0)
            sleep(0.5)

    def run(self):
        if (self.is_toggle):
            while not self.wait(0.05):
                self.third_person()
