from cheats import client
from cheat import Cheat

class Fov(Cheat):
    """It is going to change the value of your Field Of View."""
    def run(self):
        if (self.is_toggle):
            client.offset.get_fov_offset()
            client.process.write_int(client.local_player + client.offset.M_I_DEFAULT_FOV, 120)
