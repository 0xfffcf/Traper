from tkinter import *
from pathlib import Path


class Menu():
    def __init__(self):
        self.atomic = Tk()
        self.is_esp_on = IntVar()
        self.is_no_flash_on = IntVar()
        self.is_bhop_on = IntVar()
        self.is_third_person_on = IntVar()
        self.is_fov_on = IntVar()
        self.is_toggle_all = IntVar()

    def build_menu(self):
        self.atomic.title("Atomic Menu")
        self.atomic.iconphoto(False, self.getIcon())
        self.atomic.geometry("400x200")

        # ESP
        esp_check = Checkbutton(self.atomic, text="ESP", variable=self.is_esp_on)
        esp_check.pack()

        # NO FLASH
        no_flash_Check = Checkbutton(self.atomic, text="No Flash", variable=self.is_no_flash_on)
        no_flash_Check.pack()

        # BHOP
        bhop_check = Checkbutton(self.atomic, text="Bunny Hop", variable=self.is_bhop_on)
        bhop_check.pack()

        # Third Person
        third_person_check = Checkbutton(self.atomic, text="Third Person", variable=self.is_third_person_on)
        third_person_check.pack()

        # FOV
        fov_check = Checkbutton(self.atomic, text="Field Of View", variable=self.is_fov_on)
        fov_check.pack()

        # ALL
        all_cheat_heck = Checkbutton(self.atomic, text="Toggle All", variable=self.is_toggle_all)
        all_cheat_heck.pack()
       
        # QUIT
        quit_button = Button(self.atomic ,text="Close", command=self.atomic.destroy)
        quit_button.place(x=200, y=170, anchor="center")

        self.atomic.mainloop()

    def getIcon(self):
        return PhotoImage(file = f"{Path(__file__).parent.absolute()}\\assets\\iconTraper.png")
