from time import sleep

import keyboard
from win32gui import GetWindowText, GetForegroundWindow

from cheats import client
from cheat import Cheat


class Bhop(Cheat):
    """Hold space, bunny hop will be toggled on."""
    def bhop(self):
        client.offset.get_bhop_offset()

        while True:
            if GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                if not keyboard.is_pressed("space"):
                    return

                flags = client.process.read_int(client.local_player + client.offset.M_F_FLAGS)

                if flags & (1 << 0):
                    client.process.write_int(client.client + client.offset.DW_FORCE_JUMP, 5)
                else:
                    client.process.write_int( client.client + client.offset.DW_FORCE_JUMP, 4)

            sleep(0.008)

    def run(self):
        if (self.is_toggle):
            while not self.wait(0.2):
                self.bhop()