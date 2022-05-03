from threading import Event, Thread


class Cheat(Thread):
    def __init__(self, is_toggle):
        super().__init__()
        self.event = Event()
        self.is_toggle = is_toggle


    def wait(self, timeout):
        return self.event.wait(timeout)

    def stop(self):
        self.event.set()