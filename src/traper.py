from os import system

from pyfade import Fade, Colors

from cheats.multi_hack import multi_hack


def __traper_banner():
    print(Fade.Horizontal(Colors.blue_to_purple,
    """
                                                    ╔╦╗╦═╗╔═╗╔═╗╔═╗╦═╗
                                                    ║ ╠╦╝╠═╣╠═╝║╣ ╠╦╝
                                                    ╩ ╩╚═╩ ╩╩  ╚═╝╩╚═
    """
    ))


def __run():
    """(Private) Main Thread where the extensions get run."""
    system("cls")
    __traper_banner()
    multi_hack()


if __name__ == "__main__":
    __run()
