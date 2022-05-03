import pymem

from cheats import client
from cheat import Cheat


class GlowEsp(Cheat):
    """Extra-Sensory Perception that displays a glow on a player."""
    def run(self):
        if (self.is_toggle):
            while not self.wait(0.01):
                client.offset.get_esp_offset()
                glow_manager = client.process.read_int(client.client + client.offset.DW_GLOW_OBJECT_MANAGER)

                player_team = client.process.read_int(client.local_player + client.offset.M_I_TEAM_NUM)

                for i in range(1, 32): # Entities 1 to 32 are reserved for players.
                    try:
                        entity = client.process.read_int(client.client + client.offset.DW_ENTITY_LIST + i * 0x10)

                        if entity:
                            entity_glow = client.process.read_int(entity + 0x10488)
                            entity_team = client.process.read_int(entity + client.offset.M_I_TEAM_NUM)

                            # Different color for both team
                            if player_team != entity_team: # Rainbow Team
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1)) # R
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) # G
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) # B
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) # Alpha
                                client.process.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                            else: # Green Team
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) # R
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) # G
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) # B
                                client.process.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) # Alpha
                                client.process.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                    except pymem.exception.MemoryReadError:
                        pass # Could not read the memory at the specific address.