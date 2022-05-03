from cheats.esp import GlowEsp
from cheats.no_flash import NoFlash
from cheats.bhop import Bhop
from cheats.third_person import ThirdPerson
from cheats.fov import Fov
from menu import Menu


def multi_hack():
    menu = Menu()
    menu.build_menu()

    if menu.is_toggle_all.get() == 0:
        GlowEsp(menu.is_esp_on.get()).start()
        NoFlash(menu.is_no_flash_on.get()).start()
        Bhop(menu.is_bhop_on.get()).start()
        ThirdPerson(menu.is_third_person_on.get()).start()
        Fov(menu.is_fov_on.get()).start()
    else:
        GlowEsp(menu.is_toggle_all.get()).start()
        NoFlash(menu.is_toggle_all.get()).start()
        Bhop(menu.is_toggle_all.get()).start()
        ThirdPerson(menu.is_toggle_all).start()
        Fov(menu.is_toggle_all.get()).start()

