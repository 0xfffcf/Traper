import pymem

from config.offset import Offset


class Client:
    """The client that is running."""
    def __init__(self):
        self.process = self.__get_process("csgo.exe")
        self.client = self.__get_module("client.dll")
        self.offset = Offset()

        self.local_player = self.process.read_int(self.client + self.offset.DW_LOCAL_PLAYER)

    def __get_process(self, process):
        """(Private) Get a process."""
        return pymem.Pymem(process)

    def __get_module(self, module):
        """(Private) Get a module."""
        return pymem.process.module_from_name(self.process.process_handle, module).lpBaseOfDll