import requests


class Offset:
    """CSGO offset used for Cs-Fuck"""
    def __init__(self):
        self.DATA = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

        # ENTITIES
        self.DW_ENTITY_LIST = self.DATA["signatures"]["dwEntityList"]

        # PLAYER
        self.DW_LOCAL_PLAYER = self.DATA["signatures"]["dwLocalPlayer"]

        # TEAM
        self.M_I_TEAM_NUM = self.DATA["netvars"]["m_iTeamNum"]

    def get_esp_offset(self):
        self.DW_GLOW_OBJECT_MANAGER = self.DATA["signatures"]["dwGlowObjectManager"]
        self.M_I_GLOW_INDEX = self.DATA["netvars"]["m_iGlowIndex"]

    def get_no_flash_offset(self):
        self.M_FL_FLASH_MAX_ALPHA = self.DATA["netvars"]["m_flFlashMaxAlpha"]

    def get_bhop_offset(self):
        self.DW_FORCE_JUMP = self.DATA["signatures"]["dwForceJump"]
        self.M_F_FLAGS = self.DATA["netvars"]["m_fFlags"]

    def get_third_person_offset(self):
        self.M_I_OBSERVER_MODE = self.DATA["netvars"]["m_iObserverMode"]

    def get_fov_offset(self):
        self.M_I_DEFAULT_FOV = self.DATA["netvars"]["m_iDefaultFOV"]
