from cheats import client
from cheat import Cheat


class NoFlash(Cheat):
    """Flash Bang are disabled."""
    def run(self):
        if (self.is_toggle):
            client.offset.get_no_flash_offset()
            while not self.wait(1):
                flash_value = client.local_player + client.offset.M_FL_FLASH_MAX_ALPHA

                if client.local_player and flash_value:
                    client.process.write_float(flash_value, float(0))